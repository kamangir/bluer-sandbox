import os
import subprocess
import threading

from bluer_objects.env import abcli_path_git

from bluer_sandbox.logger import logger


# https://chatgpt.com/c/68057837-9dc0-8005-86aa-24eb66f6a4ab
class LlamaCppInterface:
    def __init__(
        self,
        model_path,
        n_tokens=300,
        temp=0.7,
    ):
        self.model_path = model_path
        self.n_tokens = n_tokens
        self.temp = temp
        self.process = None
        self.lock = threading.Lock()

        logger.info(
            "{}: model: {}, n_tokens={}, temp={:.2f}".format(
                self.__class__.__name__,
                model_path,
                n_tokens,
                temp,
            )
        )

    def initialize(self):
        self.process = subprocess.Popen(
            [
                "./build/bin/llama-cli",
                "-m",
                self.model_path,
                "-p",
                "",  # will send prompts later
                "-n",
                str(self.n_tokens),
                "--color",
                "--temp",
                str(self.temp),
                "-no-cnv",
            ],
            cwd=os.path.join(
                abcli_path_git,
                "llama.cpp",
            ),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        # Consume any initial output
        self._drain_output()

        logger.info(f"{self.__class__.__name__} initialized")

    def send_prompt(self, prompt):
        logger.info(
            "{}.send_prompt({})".format(
                self.__class__.__name__,
                prompt,
            )
        )

        with self.lock:
            self.process.stdin.write(prompt + "\n")
            self.process.stdin.flush()
            return self._read_response()

    def shutdown(self):
        logger.info("{}.shutdown".format(self.__class__.__name__))

        if self.process:
            self.process.terminate()
            self.process.wait()
            self.process = None

    def _read_response(self):
        response_lines = []
        while True:
            line = self.process.stdout.readline()
            if not line:
                break
            response_lines.append(line)
            if line.strip() == "":  # crude end detection
                break

        output = "".join(response_lines).strip()

        logger.info(
            "{}.response: {}".format(
                self.__class__.__name__,
                output,
            )
        )

        return output

    def _drain_output(self):
        logger.info(
            "{}.drain_output".format(
                self.__class__.__name__,
            )
        )

        while self.process.stdout.readline().strip():
            continue
