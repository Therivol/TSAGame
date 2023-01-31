import asyncio

from game.Game import Game


async def main():

    game = Game()
    game.start()

    while not game.should_close:
        game.poll_events()
        game.start_frame()
        game.early_update()
        game.update()
        game.late_update()
        game.draw()
        game.calculate_dt()

        await asyncio.sleep(0)

    game.quit()


asyncio.run(main())
