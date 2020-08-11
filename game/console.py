from game.controller import Controller
import psutil
import os


class Console:
    def __init__(self):
        self.path_to_rom: str = 'ROM/Mario Kart 64 (USA).z64'
        if not self.emulator_is_running():
            self.launch_rom(self.path_to_rom)

        self.controller = Controller()

    def launch_rom(self, path_to_rom: str):
        os.startfile(path_to_rom)

    def emulator_is_running(self):
        if 'Project64.exe' in (p.name() for p in psutil.process_iter()):
            print('Emulator is currently running...')
            return True

        return False
