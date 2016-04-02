from AIPlayer import AIPlayer
from Map import Map


def main():
    # initialize map
    map = Map()

    player = AIPlayer(map)
    map.setPlayer(player)

    map.mapLoop() # map's main loop event


if __name__ == "__main__":
    main()

