class GameStats:
    """追踪游戏的统计信息"""

    def __init__(self, ai_settings):
        self.level = None
        self.score = None
        self.ships_left = None
        self.ai_settings = ai_settings
        # 在任何情况下都不应重置最高分
        self.high_score = 0
        # 游戏刚启动时处于活动状态
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        