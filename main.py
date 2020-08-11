import game
import cv2


if __name__ == '__main__':
    env = game.environment.Environment()
    while True:
        screen = env.get_screen()
        active_keys = env.console.controller.get_active_keys()

        cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
