import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.newEnemy import NewEnemy


class EnemyManger:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)


        # if len(self.enemies) == 0:
        #     pass

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def add_enemy(self):
        enemy_type = random.randint(0, 1)
        if enemy_type == 0:
            enemy = Enemy()
        elif enemy_type == 1:
            enemy = NewEnemy()
        if len(self.enemies) < 3:
            self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)