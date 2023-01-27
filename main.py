import asyncio

from game.Game import Game
import pygbag


async def main():

    game = Game()
    game.start()

    while not game.should_close:
        game.calculate_dt()
        game.poll_events()
        game.early_update()
        game.update()
        game.late_update()
        game.draw()

        await asyncio.sleep(0)

    game.quit()

asyncio.run(main())
