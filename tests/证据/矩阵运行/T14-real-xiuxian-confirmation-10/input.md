# T14-real-xiuxian-confirmation-10 固定测试输入

- 运行 ID：`T14-real-xiuxian-confirmation-10`
- 题材边界：修仙成长 + 情境/角色喜剧
- 通用边界：测试数据只描述当前小说，执行器不绑定本书
- 章节范围：`[1, 10]`
- 故事单元状态：`completed`

## 项目资料

# 《剑阵今天只认收据》

## 定位

- 修仙成长 + 外门剑阵维护职业线 + 情境/角色喜剧。
- 固定首单元 10 章：阵务学徒姜守必须在外门演武前修复误伤候选人的乙字训练剑阵，查明维护签、灵钉缺口与口令错位的责任边界，并取得带条件的阵堂小考资格。
- 喜剧来自剑阵字面执行口令、姜守把推诿写成维修工单、同伴把帮助说成事故隔离；笑点必须改变劳动、证词、资源或关系，不能取消伤势、器损和资格风险。

## 角色

- 姜守 `jiang-shou`：炼气二层，阵务学徒，擅长基础吐纳、灵纹辨识、低强度校阵；说话像维修清单。开篇活动伤势 `left-palm-burn`：左掌阵火灼伤，持续导灵会刺痛和灵纹失稳。开篇活动限制 `live-array-contact-ban`：伤势解除前不得直接接触运行阵眼。伤势必须跨章加重、部分恢复、解除，全部复用稳定 ID。
- 苏叶 `su-ye`：炼气一层，同组学徒，熟背安全条款。开篇误信 `command-slip-tamperer`：她认为姜守为了催缴维修贡献，主动改写了阵法口令签。该误信最终必须被新事实淘汰。
- 赵矩 `zhao-ju`：炼气三层，阵务管事，先看事故栏和签押，表格完整时也必须按同一流程让步。
- 闻岚 `wen-lan`：炼气四层，阵堂巡验弟子，只认灵纹、领用、时辰和后果，不替姜守免除违规带伤校阵责任。
- 袁客 `yuan-ke`：炼气二层，同批竞争者，熟悉灵钉领用；本单元最多坐实他未登记借走三枚定向灵钉，不揭开阵材长期短缺背后的全部关系。

## 异常与边界

- 乙字训练剑阵把“后退三步，停剑”错读成“追后三步再停”，木剑会多追一段；口令错位只能由维护签、灵纹磨损、灵钉方向和现场记录共同核验。
- 一面回声阵牌会复述最近收到的完整口令，但不知道谁下令、何时下令，也不能单独定责。
- 姜守确实曾带伤私自做过一次低强度校阵，违规责任保留。
- 已裂的校准镜不能恢复，必须计赔。

## 单元硬要求

- 真实受挫：姜守带伤接触运行阵眼，`left-palm-burn` 加重，阵法多放一轮木剑并打裂校准镜，扣2点贡献、资格冻结。
- 伤势经历加重、部分恢复、解除；`live-array-contact-ban` 在解除前有效，解除后仍有两日不得独立启动整阵的新限制。
- 苏叶的 `command-slip-tamperer` 必须用 `supersedes_fact_ids` 淘汰。
- 最终修复阵法并取得带条件阵堂小考资格，但镜子赔偿、带伤校阵处分、贡献扣减和阵材短缺保留。

## 禁止

- 回声阵牌不得直接说出责任人。
- 闻岚不得无证据保人。
- 不得恢复裂镜、退还已扣贡献或用修为升级抹掉处分。
- 本单元不突破境界，不获得新破案能力。
- 不使用网络热梗、围观震惊、全员降智或旁白解释笑点。

## 故事单元

```json
{
  "unit_id": "unit-0001",
  "chapter_range": [
    1,
    10
  ],
  "goal": "姜守必须在外门演武前修复乙字训练剑阵的口令错位，查清维护签、灵纹磨损、定向灵钉缺口与现场记录之间的责任边界，并在不突破炼气二层、不抹掉处分的前提下取得带条件的阵堂小考资格。",
  "entry_state": [
    "姜守为炼气二层阵务学徒，拥有基础吐纳、灵纹辨识、低强度校阵能力，但受 left-palm-burn 影响导灵刺痛、抖动并导致灵纹失稳。",
    "live-array-contact-ban 生效：left-palm-burn 解除前，姜守不得直接接触运行阵眼。",
    "乙字训练剑阵把“后退三步，停剑”错读成“追后三步再停”，已误伤外门演武候选人，姜守的维护签被列入事故核查重点。",
    "姜守资源为 low-spirit-stone 3枚、contribution-point 8点、burn-salve 1份；阵堂账面 direction-spirit-nail 12枚。",
    "苏叶误信 command-slip-tamperer：她认为姜守为了催缴维修贡献主动改写了阵法口令签。",
    "赵矩怀疑 jiang-shou-liability：姜守带伤校阵和维护签足以先冻结资格。",
    "袁客隐瞒 spirit-nail-borrowing：他未登记借走三枚定向灵钉，并试图让核查停在口令签上。",
    "闻岚只按灵纹、领用、时辰和后果判断资格，不会无证据替姜守免除带伤校阵责任。"
  ],
  "closing_state": [
    "乙字训练剑阵已在停阵监督下完成修复，现场测试中“后退三步，停剑”不再被执行成“追后三步再停”。",
    "姜守仍为炼气二层，未突破境界，修复依靠记录核验、停阵测试、苏叶协助和闻岚监督完成。",
    "left-palm-burn 经加重、使用 burn-salve、稳定吐纳和闻岚巡验确认后解除；live-array-contact-ban 随伤势解除失效。",
    "姜守新增限制：伤势解除后两日内不得独立启动完整剑阵，只能在监督下参与停阵或局部低强度校阵。",
    "姜守的 calibration-mirror 已裂且不能恢复，赔偿责任保留。",
    "姜守因带伤接触运行阵眼和造成多放一轮木剑被扣 contribution-point 2点，余额为6点，已扣贡献不退还。",
    "姜守阵堂小考资格由冻结改为带条件准入：须完成裂镜赔偿排期、两日内不得独立启动整阵、接受带伤校阵处分记录。",
    "苏叶的 command-slip-tamperer 误信被新事实 supersedes_fact_ids 淘汰：回声阵牌只证明完整口令曾被收到，维护签拓印、磨损方向和三枚定向灵钉缺口共同证明姜守没有主动改写口令签。",
    "赵矩被同一事故表约束，必须在表内承认已核事实：维护签不能单独定责、三枚定向灵钉未登记缺口成立、姜守仍承担带伤违规责任。",
    "袁客最多被坐实未登记借走三枚 direction-spirit-nail，阵材长期短缺背后的全部关系没有揭开。",
    "阵材短缺、裂镜赔偿、带伤校阵处分和姜守后续资格条件均保留为后续问题。"
  ],
  "main_obstacle": "事故流程先把姜守的维护签和带伤校阵责任锁定为资格冻结依据，而真正的口令错位需要把维护签拓印、灵纹磨损、定向灵钉方向、回声阵牌复述和领用时辰拼合核验；姜守又因 left-palm-burn 与 live-array-contact-ban 不能直接接触运行阵眼，调查和修复都受限。",
  "progression_change": [
    "姜守没有突破炼气二层，但从单纯依赖低强度校阵，转为能在停阵或监督条件下把灵纹辨识、记录核验和安全流程组合使用。",
    "姜守对乙字训练剑阵的认知从“维护签可能出错”推进到“口令错位由维护签歧义、灵纹磨损、三枚定向灵钉方向缺口和现场记录共同触发”。",
    "left-palm-burn 先因违规接触运行阵眼加重，随后通过 burn-salve、停用运行阵眼、基础吐纳和巡验确认部分恢复并解除。",
    "苏叶从只按条款怀疑姜守，转为用安全条款为修复设置隔离流程并付出证词时间成本。",
    "姜守获得带条件阵堂小考资格，但新增两日不得独立启动完整剑阵的限制，修炼与职业进度推进但不越界。"
  ],
  "resource_change": [
    {
      "owner_id": "jiang-shou",
      "resource_id": "burn-salve",
      "change": -1,
      "final_amount": 0,
      "unit": "份",
      "reason": "姜守在 left-palm-burn 加重后使用唯一一份灼伤膏，只能缓解并配合吐纳恢复，不能瞬间治愈。"
    },
    {
      "owner_id": "jiang-shou",
      "resource_id": "contribution-point",
      "change": -2,
      "final_amount": 6,
      "unit": "点",
      "reason": "姜守带伤接触运行阵眼导致阵法多放一轮木剑并打裂校准镜，按事故表扣2点贡献。"
    },
    {
      "owner_id": "jiang-shou",
      "resource_id": "low-spirit-stone",
      "change": 0,
      "final_amount": 3,
      "unit": "枚",
      "reason": "本单元未消耗或获得低阶灵石。"
    },
    {
      "owner_id": "formation-hall",
      "resource_id": "direction-spirit-nail",
      "change": -3,
      "final_amount": 9,
      "unit": "枚",
      "reason": "核查坐实袁客未登记借走三枚定向灵钉，阵堂账面应有12枚，现场可核对仅剩9枚。"
    }
  ],
  "relationship_change": [
    "姜守与苏叶从互相防备转为有限协作：苏叶不再相信姜守主动篡改口令签，但仍坚持记录他的带伤违规。",
    "姜守与赵矩从被单方面压表冻结，转为利用同一事故表迫使赵矩承认已核事实；双方关系仍是流程内对立。",
    "姜守与闻岚建立有限职业信任：闻岚认可他的证据链和修复过程，但不替他免除处分和资格条件。",
    "姜守与袁客形成明确矛盾：袁客未登记借走三枚定向灵钉被坐实，但他仍把阵材长期短缺推成集体问题。",
    "苏叶因把帮忙称为隔离共同事故，必须留下作证并参与停阵记录，和姜守形成带成本的同组责任关系。"
  ],
  "comedy_plan": [
    "前段使用 repair-order：姜守把赵矩、苏叶和袁客的推诿逐条写进维修工单，导致每个说过“可以查”的人都必须承担一项查验、隔离或签收工作。",
    "前中段使用口令字面错位：乙字训练剑阵在安全测试中把“后退三步，停剑”执行成追击动作，迫使众人改变站位、增加隔离绳和记录人手，笑点直接增加劳动成本。",
    "中段使用 shared-incident：苏叶把协助称为“隔离共同事故”，结果按条款必须留下时辰证词、看守停阵牌并承担半日排查，改变她与姜守的关系。",
    "中后段使用 form-return：赵矩先用事故表冻结资格，后续同一事故表的栏位要求他补填灵钉缺口、回声阵牌限制和已核灵纹事实，迫使他流程内让步。",
    "后段使用袁客回避数量与姜守逐项填数的反差：袁客说“大家都缺一点”，姜守只问“缺几枚、谁领、何时还”，最终把圆滑说法压成三枚未登记事实。"
  ],
  "required_setback": "姜守带伤接触运行阵眼，left-palm-burn 加重，乙字训练剑阵多放一轮木剑并打裂 calibration-mirror，姜守被扣 contribution-point 2点且阵堂小考资格冻结。",
  "required_payoff": "闻岚在停阵复验后确认乙字训练剑阵口令恢复正常、left-palm-burn 解除，并裁定姜守取得带条件阵堂小考资格：两日内不得独立启动完整剑阵，裂镜赔偿和带伤校阵处分继续保留。",
  "must_not_resolve": [
    "不得揭开阵材长期短缺背后的全部关系，只能坐实袁客未登记借走三枚 direction-spirit-nail。",
    "不得恢复 calibration-mirror 或免除裂镜赔偿。",
    "不得退还姜守已扣的2点 contribution-point。",
    "不得用突破境界、新破案能力或闻岚无证据担保解决资格问题。",
    "不得让回声阵牌直接说出责任人。",
    "不得取消姜守带伤私自低强度校阵的违规处分。"
  ],
  "beats": [
    "事故后姜守立即赶到乙字训练剑阵外围，发现木剑仍按“追后三步再停”的轨迹残留灵纹；赵矩先按事故栏冻结姜守小考资格，姜守把“先查维护签、再查灵钉、再查现场口令”的推诿写成维修工单，迫使赵矩给出临时查验编号。",
    "苏叶依据安全条款拦住姜守靠近运行阵眼，并公开说出 command-slip-tamperer 的误信；姜守为证明不是自己主动改签，提出只做外围灵纹辨识和停阵拓印，苏叶把协助称为“隔离共同事故”，因此必须留下记录时辰和隔离范围。",
    "袁客试图把问题引向姜守维护签，说灵钉“向来都不齐”；姜守在工单上要求填写具体缺口数量，袁客回避签字，反而让姜守获得“灵钉领用需核账”的明确调查方向。",
    "第一次低强度测试前，回声阵牌复述最近收到的完整口令“后退三步，停剑”，但不能说明谁下令、何时下令；闻岚到场后只确认阵牌限制和现场后果，要求继续核验灵纹磨损、维护签拓印和灵钉方向，姜守获得不能靠阵牌单独定责的新认知。",
    "姜守急于保住小考资格，趁停阵间隙误判阵眼余灵为安全，带伤接触运行阵眼，left-palm-burn 加重，乙字训练剑阵多放一轮木剑并打裂 calibration-mirror，姜守被扣 contribution-point 2点且阵堂小考资格冻结。",
    "受挫后姜守无法再直接碰运行阵眼，burn-salve 消耗1份后只能缓解刺痛；苏叶按条款接管隔离牌和时辰记录，姜守改用口述维修清单指挥停阵拓印，关系从指责转为有成本协作。",
    "姜守、苏叶在闻岚监督下比对维护签拓印和磨损灵纹，确认维护签字迹有歧义但不足以单独造成追击三步；同时三处定向灵钉孔位方向与账面不符，事故原因从“姜守改签”推进为“签、纹、钉、记录共同核验”。",
    "赵矩试图维持资格冻结结论，姜守提交同一事故表的补充栏：回声阵牌不能定人、灵纹磨损可验、灵钉缺口未填；赵矩被 form-return 反制，只能承认已核事实并允许在监督下做停阵修复测试，但保留姜守带伤违规栏。",
    "袁客再次把三枚定向灵钉说成“临时周转”，姜守让他按维修工单填写“临时几枚、周转到哪、何时归还”，闻岚核对领用时辰后坐实袁客未登记借走三枚 direction-spirit-nail，但不继续追查阵材长期短缺背后的全部关系。",
    "在苏叶记录、赵矩签验、闻岚巡验的监督下，姜守不接触运行阵眼，只用停阵低强度校阵调回局部灵纹并补正定向灵钉方向；测试中木剑按“后退三步，停剑”停止，left-palm-burn 经巡验确认解除，姜守获得带条件阵堂小考资格，同时裂镜赔偿、扣点、处分和两日不得独立启动整阵的新限制全部留下。"
  ],
  "status": "completed",
  "updated_at": "2026-07-21T13:01:22.216380+00:00"
}
```

## 初始结构化状态

```json
{
  "schema_version": "1.0",
  "cultivation": [
    {
      "subject_id": "jiang-shou",
      "stage": "炼气二层",
      "abilities": [
        "基础吐纳",
        "灵纹辨识",
        "低强度校阵"
      ],
      "injuries": [
        {
          "state_id": "left-palm-burn",
          "description": "左掌阵火灼伤，导灵时会刺痛、抖动并导致灵纹失稳"
        }
      ],
      "limits": [
        {
          "state_id": "live-array-contact-ban",
          "description": "left-palm-burn 解除前不得接触运行阵眼"
        }
      ]
    },
    {
      "subject_id": "su-ye",
      "stage": "炼气一层",
      "abilities": [
        "基础吐纳",
        "安全条款记忆"
      ],
      "injuries": [],
      "limits": [
        "不能独立校阵"
      ]
    },
    {
      "subject_id": "zhao-ju",
      "stage": "炼气三层",
      "abilities": [
        "基础阵法",
        "事故验收"
      ],
      "injuries": [],
      "limits": [
        "必须服从正式事故记录"
      ]
    },
    {
      "subject_id": "wen-lan",
      "stage": "炼气四层",
      "abilities": [
        "阵纹巡验",
        "基础御剑"
      ],
      "injuries": [],
      "limits": [
        "不能越过阵堂考核程序直接给资格"
      ]
    },
    {
      "subject_id": "yuan-ke",
      "stage": "炼气二层",
      "abilities": [
        "基础吐纳",
        "熟悉灵钉领用"
      ],
      "injuries": [],
      "limits": [
        "不能正面对抗巡验弟子"
      ]
    }
  ],
  "resources": [
    {
      "owner_id": "jiang-shou",
      "resource_id": "low-spirit-stone",
      "amount": 3,
      "unit": "枚"
    },
    {
      "owner_id": "jiang-shou",
      "resource_id": "contribution-point",
      "amount": 8,
      "unit": "点"
    },
    {
      "owner_id": "jiang-shou",
      "resource_id": "burn-salve",
      "amount": 1,
      "unit": "份"
    },
    {
      "owner_id": "formation-hall",
      "resource_id": "direction-spirit-nail",
      "amount": 12,
      "unit": "枚"
    }
  ],
  "knowledge": [
    {
      "character_id": "jiang-shou",
      "fact_id": "array-command-error-cause",
      "state": "investigating",
      "belief": "追后三步的错误不只来自自己的维护签，阵眼方向和灵钉数量也有异常"
    },
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "believes_false",
      "belief": "姜守为了催缴维修贡献主动改写了阵法口令签"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "jiang-shou-liability",
      "state": "suspects",
      "belief": "姜守带伤校阵和维护签足以先冻结资格"
    },
    {
      "character_id": "yuan-ke",
      "fact_id": "spirit-nail-borrowing",
      "state": "conceals",
      "belief": "自己未登记借走三枚定向灵钉，必须让核查停在口令签上"
    },
    {
      "character_id": "wen-lan",
      "fact_id": "qualification-result",
      "state": "investigating",
      "belief": "姜守的资格由修复过程、伤势处置和责任记录决定"
    }
  ]
}
```

## 修炼体系

```json
{
  "schema_version": "1.0",
  "realms": [
    {
      "stage": "炼气一层",
      "requirements": [
        "基础引气"
      ],
      "boundaries": [
        "只能低强度导灵"
      ]
    },
    {
      "stage": "炼气二层",
      "requirements": [
        "小周天稳定"
      ],
      "boundaries": [
        "可做低强度校阵，不能独立启动完整剑阵"
      ]
    },
    {
      "stage": "炼气三层",
      "requirements": [
        "阵纹控制与灵气储量达标"
      ],
      "boundaries": [
        "本单元姜守不得突破到此境界"
      ]
    }
  ],
  "resources": [
    {
      "resource_id": "low-spirit-stone",
      "unit": "枚",
      "rules": [
        "获得和消耗必须记余额"
      ]
    },
    {
      "resource_id": "contribution-point",
      "unit": "点",
      "rules": [
        "扣减与冻结使用同一资源 ID"
      ]
    },
    {
      "resource_id": "burn-salve",
      "unit": "份",
      "rules": [
        "只能缓解阵火灼伤，不能瞬间治愈"
      ]
    },
    {
      "resource_id": "direction-spirit-nail",
      "unit": "枚",
      "rules": [
        "阵堂公物，领用和归还必须留记录"
      ]
    }
  ],
  "techniques": [
    {
      "technique_id": "basic-breathing",
      "name": "基础吐纳",
      "effects": [
        "稳定灵气"
      ],
      "limits": [
        "不能修复裂镜"
      ]
    },
    {
      "technique_id": "pattern-reading",
      "name": "灵纹辨识",
      "effects": [
        "辨认磨损和导灵方向"
      ],
      "limits": [
        "不能判断谁移动过灵钉"
      ]
    },
    {
      "technique_id": "low-array-calibration",
      "name": "低强度校阵",
      "effects": [
        "在停阵或监督下微调局部灵纹"
      ],
      "limits": [
        "伤势未解除不得接触运行阵眼",
        "不能独立启动整阵"
      ]
    }
  ],
  "artifacts": [
    {
      "artifact_id": "calibration-mirror",
      "name": "校准镜",
      "limits": [
        "裂损后不可自行恢复"
      ]
    },
    {
      "artifact_id": "echo-command-plate",
      "name": "回声阵牌",
      "limits": [
        "只复述完整口令，不记录说话者和时间"
      ]
    }
  ],
  "injury_rules": [
    {
      "state_id": "left-palm-burn",
      "name": "左掌阵火灼伤",
      "symptoms": [
        "刺痛",
        "导灵抖动",
        "灵纹失稳"
      ],
      "recovery": [
        "停用运行阵眼",
        "使用灼伤膏",
        "稳定吐纳",
        "巡验确认"
      ],
      "hard_rule": "所有更新和解除复用同一 state_id"
    }
  ],
  "breakthrough_rules": [],
  "power_boundaries": [
    "姜守全单元保持炼气二层",
    "修复依靠记录、停阵测试和协作，不靠临时升级"
  ],
  "exceptions": []
}
```

## 喜剧圣经

```json
{
  "schema_version": "1.0",
  "density": "medium",
  "protagonist_role": "姜守把推诿和口头承诺写成维修工单，迫使说话者承担具体工作",
  "character_contrasts": [
    "姜守按故障项说话，苏叶按风险条款说话",
    "赵矩用事故表压人，同一事故表也会限制他",
    "闻岚面对荒谬口令仍只查灵纹、时辰和后果",
    "袁客把具体领用说成大家都缺，姜守要求填具体数量"
  ],
  "allowed_mechanisms": [
    "维修工单字面执行",
    "安全条款反差",
    "口令字面错位",
    "规章回调",
    "阵法测试导致行动连锁"
  ],
  "forbidden_humor": [
    "伤势或器损被笑话取消",
    "回声阵牌万能破案",
    "网络热梗",
    "全员降智",
    "围观震惊"
  ],
  "language_boundaries": [
    "姜守短句列项",
    "苏叶先说风险再行动",
    "赵矩引用栏位",
    "闻岚短句定边界",
    "袁客圆滑回避数量"
  ],
  "callbacks": [
    {
      "callback_id": "repair-order",
      "setup": "推诿被写成维修工单",
      "rule": "回调时说话者必须承担一项工作"
    },
    {
      "callback_id": "shared-incident",
      "setup": "苏叶把帮忙称为隔离共同事故",
      "rule": "她必须付出时间或证词代价"
    },
    {
      "callback_id": "form-return",
      "setup": "赵矩用事故表冻结资格",
      "rule": "同一表格后续必须要求他承认已核事实"
    }
  ],
  "fatigued_mechanisms": [],
  "serious_scene_limits": [
    "伤势加重、裂镜、扣点、资格裁定降低笑点密度"
  ]
}
```
