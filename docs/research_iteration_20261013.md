# 2026-10-13 十二路径研究：实际执行股票贡献验收

## 开轮反思

已读取最近三轮10/09、10/10、10/12的反思、scorecard、实验账本及九plan。10/12完成A3保护消融与HK固定集合配权，但逐日股票贡献runner和Path2跨池过滤尚未实现，本轮继续，取消重复hold/entry/base/hybrid相邻扩参。10/09资金恒等式修复及10/10传导诊断已经落实，不重复计算为本轮成果。

初始guard as_of=2026-10-12，Path2缺798/828，上轮同10/09为716/828；截止推进导致当前截止覆盖回落，不是新增候选失败。首20-ID严格按guard执行；正式Path2冻结。预算因coverage和归因实现回落12–18；先保留A3与HK2五窗参数确认预算，额外路径只有证据支持才扩大，不为数量复活已reject候选。

A股问题：hold0/hold6的2023风险开启期收益差能否被实际执行股票贡献重构，并定位过早退出或敞口差？HK问题：entry10/entry11的2026差值主要由不同股票还是共有股票权重造成？先实现隔离逐日runner，实际调仓后持仓、复权价格和现金重构净NAV；每日贡献及所有引擎期末NAV最大绝对误差≤1e-6。若验收失败，归因结论fail closed。冻结端点10/12，五窗同成本比较，若中窗CAGR损失>3pp、MaxDD恶化>5pp或Sharpe下降>0.3则reject/keep_watch。股票差分只是描述性证据，不能冒充因果；贡献来自共有股票或费用则否定入口换股解释，无新证据停止扩参。

## 十二路径结果

两市冻结截止10/12；有效参数竞争2项（A3/HK2），参照2项、20-ID补缺及Path5成熟度另计。五窗CAGR/Sharpe/MaxDD/turnover、代码真实相邻窗口锚点与全部精确命令见scorecard；九plan四段完整。

### ashare_path1

主线冻结buffered/buffered_asym13检查风险阶段目标与实投；core_multifactor冻结shape_control/risk_graft检查2020损失来自年度/股票贡献还是形态风控。停止小因子权重扩参。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

主线：周仓位三形态未同端点实跑；core_multifactor：64/64覆盖仅表示窗口存在，冻结shape_control/risk_graft，不新增小权重变体。

当前内部robust近窗或minCAGR为负，进入观察位，不是强稳定 winner。

下一轮第一条命令及候选池：`docs/path1_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### ashare_path2

落实growth_elastic明确池来源过滤，缺失/跨池行不参与排名；只按最终guard精确补缺，不以partial robust晋级。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

当前内部robust近窗或minCAGR为负，进入观察位，不是强稳定 winner。

下一轮第一条命令及候选池：`docs/path2_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### ashare_path3

hold0常规观察第三轮无跨窗实质改善，archive；冻结hold0/hold6仅用于共有持仓权重/持有时序诊断，禁止相邻hold搜索。

`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly` 对 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`，五窗实际重放与成交归因；判定 **archive**。2020/2023 CAGR差 -2.57/-2.50pp，2026候选CAGR 19.01%。第三轮观察仍无跨窗防守改善：中窗净CAGR下降约2.57/2.50pp，2023MaxDD恶化约4.50pp；虽未触强制稳定性阈值，停止常规刷新并归档，只保留冻结归因对照。

当前内部robust近窗或minCAGR为负，进入观察位，不是强稳定 winner。

下一轮第一条命令及候选池：`docs/path3_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### ashare_path4

冻结leader_gate_ablation与当前robust，按年度领先股票贡献和单票集中度检查theme_signal_quality；不因低敞口直接放大cap。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

当前内部robust近窗或minCAGR为负，进入观察位，不是强稳定 winner。

下一轮第一条命令及候选池：`docs/path4_emergent_theme_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### hkconnect_path1

冻结biweekly_lowvol与机制消融，先比较2020/2023风险阶段与成本，不扩大entry/hold。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

下一轮第一条命令及候选池：`docs/path1_plan_hkconnect.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### hkconnect_path2

取消base/hybrid比例族；冻结entry10/entry11。近窗不同实际持仓段主导，下一轮先检查03328/00857贡献跨年度与入口/退出事件，不做事后股票过滤。

`hkconnect_path2_theme_entry10_20261006` 对 `hkconnect_path2_theme_entry11_20261007`，五窗实际重放与成交归因；判定 **keep_watch**。2020/2023 CAGR差 -2.05/-1.49pp，2026候选CAGR 17.27%。中窗CAGR落后2.05/1.49pp，近窗高2.60pp；跨窗收益晋级假设不支持，近窗贡献主要来自独有持仓段，保留观察但不扩entry参数。

下一轮第一条命令及候选池：`docs/path2_plan_hkconnect.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### hkconnect_path3

冻结theme_risk52与机制消融，检查换股事件及gross/net成本贡献；不再相邻hold/cap。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

下一轮第一条命令及候选池：`docs/path3_plan_hkconnect.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### hkconnect_path4

冻结v47与mechanism，检查2026负收益是否集中在risk-on股票；观察位不晋级。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

当前内部robust近窗或minCAGR为负，进入观察位，不是强稳定 winner。

下一轮第一条命令及候选池：`docs/hkconnect_strategy_expansion_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### hkconnect_path5

冻结frozen_shape与满额mechanism，核对risk-on gross损失/实际股票仓位；维持停止补cap修复假设。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

当前内部robust近窗或minCAGR为负，进入观察位，不是强稳定 winner。

下一轮第一条命令及候选池：`docs/hkconnect_strategy_expansion_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### hkconnect_path6

冻结lowvol_hold18与mechanism，监控2017、中窗回撤以及集中度/换手，不相邻hold搜索。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

下一轮第一条命令及候选池：`docs/hkconnect_strategy_expansion_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### hkconnect_path7

冻结cap08与v7，先核对2026正收益来源与风险敞口；不照抄旧v7负收益标签，不相邻cap搜索。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

下一轮第一条命令及候选池：`docs/hkconnect_strategy_expansion_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

### ashare_path5

v0冻结来源与成员；v1仅为完成来源、成本统一后的实现任务，未注册不写执行ID。

未新增/确认回测：三轮相邻扩参已停止；本轮优先兑现实际贡献验收与池口径修复，尚无预登记新结构理由。未耗尽整日预算，未达缩量目标。

下一轮第一条命令及候选池：`docs/path5_event_knowledge_graph_plan.md`；同窗口条件回放见scorecard.next_backtest_replay_commands。

## 反思与下一轮决策

1. **上轮决策落实**：已实现并验收逐日实际股票贡献runner，A3 hold0/hold6、HK entry10/entry11各五窗同10/12真实参数确认；净NAV/实际成交/现金/费用最大误差小于1.5e-15。已落实Path2池过滤，跨池/缺失来源行停止参与growth_elastic排名，raw coverage仍保留。固定父集合base/hybrid扩参取消。A1与其它路径的股票事件归因尚未执行，继续冻结诊断设计，不冒充本轮实跑。

2. **本轮认知变化**：A股2023净对数差-0.08556，共有实际持仓贡献-0.11087、独有段+0.02490、费用+0.000404；对称敞口项+0.00493，股票组合收益项-0.08307，否定“主要只是低总敞口或费用”的解释。但共有股票差包含权重/持有时序，尚不能称退出因果。300308单股贡献差-0.09774，警惕单票依赖。HK2026净对数差+0.01546，独有段+0.01660，共有段-0.00123、费用+0.000088，支持持仓差异优先于配权/费用解释；03328与00857合计+0.01624超过总增益，不能泛化为入口广度普遍有效。中窗entry10仍落后，keep_watch。

3. **失败与自我检查**：Path2是当前截止覆盖问题，10/09→10/12覆盖回落不能归因于策略机制。默认10/13触freshness拒绝，保留guard ID/窗口只显式冻结10/12重试。排名跨池是评价口径缺陷，非成长信号失败。A3损失为实际组合/权重路径而非费用，可替代解释为单票主导、保护释放时序及交易缓冲；HK可替代解释为少数银行/石油股票阶段性收益，不是entry阈值因果。下一步最小验证均为事件联接+年度/剔除最大贡献股票诊断，不把事后股票排除写成交易条件。初版A股runner挂错输出入口，写到了这些已选ID的常规backtest目录；已改为build_pool_output_dir隔离，完整五窗重跑并补保存真实成交输入，初版不作为最终证据。没有修改或晋级正式角色。检查并停止弱参照改善、短窗晋级、相邻微调及忽略费用。

4. **停止与改变**：A3 hold0经历10/09、10/12、10/13三轮观察无跨窗实质改善，本轮archive并加入PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS，停止常规刷新，历史与显式归因可重放；不再扫描hold邻值。HK停止base/hybrid与entry相邻搜索，entry10仅keep_watch。实际2项确认、0新ID低于12–18缩量及24–36常规配额，原因是有证据机制闭环和无新结构理由，未声称coverage耗尽全天；其余路径均有候选设计与首命令，未满足配额明确披露。

5. **下一轮决策**：A股最高优先先把hold0/hold6的实际共有股票权重、保护状态和退出事件逐日联接，做预先规定的单票剔除贡献敏感性；若300308剔除后认识逆转，停止泛化保护机制。HK最高优先entry10/entry11实际入口/保留/退出联接，按年度与共同风险组解释03328/00857持仓差；若优势只依赖近窗两股或中窗独有段持续为负，否定普遍入口优势。尚无新候选ID，先实现上述审计；验收为PIT/执行日期明确、净NAV重构≤1e-6、股票+费用差可加总。只做一次诊断，未支持不扩参。具体首命令、冻结回放、预期、证伪及停止规则已经落实九plan和scorecard.next_priority。

Path2当前缺 778/828，仍block，正式winner/robust/tracked冻结；其它目标scope见最终guard。Path5成熟度复核仍不足以晋级。kb-web复用9/16盈利快照30条、哈希验证通过，0新增调用/0credits；既有首次pilot已完成，无新字段假设。

本轮排名口径补充：guard完整50/828仅指同截止行存在；growth_elastic有效排名45个。跨池/缺来源行不进入排名，正式Path2身份冻结。

## 同步与验收

weighted/HK artifacts、live42、public55榜项与135新生成详情均已执行，最终guard仍唯一Path2 block缺778/828、warning0，其它目标scope pass。恢复22份历史详情与用户HK三图/Path6/HK8/README/HISTORY；正式window winner/robust身份未变。中文贡献图已目视验收（初稿字体路径不存在，改用系统实际STHeiti字体）。13项定向测试、两卡五窗同成本、执行NAV误差及九plan/focus验收已通过；原始逐日股票/真实成交/turnover留本地，全文件哈希与可审计摘要随提交。

收尾辅助校验说明：首次114文件完整白名单/用户基线验收通过。第二次清单构建只看未暂存差异，漏列此前已暂存的public_snapshot、experiments、report/state和两份comparison共6个合法文件，校验报错；shell未在失败时停止，仍提交并推送fa95a74d。这是本轮执行控制错误。随后逐项审计已提交114文件，6个均属于本轮固定目标，无用户改动混入；校验清单构建已改为并入已暂存差异。补充报告单独校验后提交，未重写历史或丢弃工作树。
