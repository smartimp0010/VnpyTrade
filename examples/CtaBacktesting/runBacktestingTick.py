# encoding: UTF-8

"""
展示如何执行策略回测。
"""

from __future__ import division

from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, TICK_DB_NAME

if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategyTickOne import TickOneStrategy

    # plotting
    turn_on_plot = True

    # Sql
    data_from_sql = False
    data_from_csv = True

    # 创建回测引擎
    engine = BacktestingEngine()

    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.HYBER_MODE)

    # 設置成交模擬器
    engine.setSimulatingMode(engine.TRADEFILLED_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20180101')

    # 设置产品相关参数
    engine.setSlippage(0)  # 股指1跳
    engine.setRate(0)  # 万0.3
    engine.setSize(200)  # 股指合约大小
    engine.setPriceTick(1)  # 股指最小价格变动

    # 设置使用的历史数据库
    engine.setDatabase(TICK_DB_NAME, 'TXF01')

    # 在引擎中创建策略对象
    d = {}
    engine.initStrategy(TickOneStrategy, d)

    # 开始跑回测
    if data_from_sql:
        engine.runBacktestingSql()
    elif data_from_csv:
        engine.runBacktestingCsv()
    else:
        engine.runBacktesting()

    # 显示回测结果
    engine.showBacktestingResult()
    if turn_on_plot:
        engine.plotResult()