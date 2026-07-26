# 逐章正式状态事件

## 第 1 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0001",
  "chapter": 1,
  "source_draft": "chapters/0001/draft.final.md",
  "source_sha256": "c5bf5606f76f37aa481922aa6bb0a6275d50a8495a6982a8ee322f3d78d1867d",
  "entity_changes": [
    {
      "change": "乙字训练剑阵在演练中将“后退三步，停剑”执行为继续追击并造成候选人右肩受伤。",
      "source_evidence": "候选人进两步，侧身避过第一剑，随即依照演练册喊道：“后退三步，停剑！”\n\n木剑本该在他退满三步时垂落。\n\n第一步落下，十二柄木剑却齐齐向前。\n\n第二步，剑阵追近半尺。\n\n第三步，候选人刚要停，最前一柄木剑猛地多窜出一段，拍中他的右肩。他踉跄半步，背后两柄木剑又接连撞来，将他打出白线。"
    },
    {
      "change": "乙字训练剑阵因事故被临时停用并封场隔离。",
      "source_evidence": "“先封场。”赵矩已经起身，“候选人送药堂验伤，乙字剑阵临时停用！”"
    },
    {
      "change": "候选人的右肩木剑击伤已被姜守写入旁录，候选人停止演练并送药堂验看。",
      "source_evidence": "候选人被扶出场时回头看了一眼。姜守将“右肩木剑击伤，停止演练，送药堂验看”写进旁录，随后看着杂役在场地四角插下停用牌。"
    }
  ],
  "relationship_changes": [
    {
      "change": "赵矩依据维护签上的姜守签押，将姜守临时列为事故首要说明人。",
      "source_evidence": "赵矩从夹板中抽出维护签。纸签末尾确有“姜守”二字，旁边还压着阵务小印。\n\n他用笔尖点住签押：“事故先认记录。姜守，暂列首要说明人。”"
    },
    {
      "change": "苏叶因隔离工单成为乙字剑阵测试区隔离协助人，负责看守红绳并阻止姜守违规接触运行阵眼。",
      "source_evidence": "姜守换了一栏：“后续任务二：隔离乙字剑阵测试区。协助人，苏叶。职责：拉设隔离绳，阻止无关人员入内，阻止姜守违规接触运行阵眼。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "左掌阵火灼伤被写入事故记录，症状明确为导灵时刺痛、抖动，可能导致灵纹失稳。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他另起一行写道：“姜守，左掌阵火灼伤，导灵时刺痛、抖动，可能致灵纹失稳。伤势解除前，不得直接接触运行阵眼。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "伤势解除前不得直接接触运行阵眼的禁令被赵矩确认即刻适用。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他另起一行写道：“姜守，左掌阵火灼伤，导灵时刺痛、抖动，可能致灵纹失稳。伤势解除前，不得直接接触运行阵眼。”\n\n赵矩抬头确认：“禁令即刻适用。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "believes_false",
      "belief": "姜守为了催缴维修贡献，主动改写口令签，想让候选人吃苦头。",
      "supersedes_fact_ids": [],
      "change": "苏叶当面说出并维持对姜守改写口令签的误信。",
      "source_evidence": "苏叶正在整理安全册，闻言冷声道：“你最会拿流程把自己摘干净。前日你催候选人补维修贡献，今日口令就从停剑变成追后三步。姜守，是不是你为了催缴，主动改写了口令签，想让他们吃些苦头？”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "command-slip-verification-lead",
      "state": "investigating",
      "belief": "需要通过维护签拓印、原签时辰及现场记录核验苏叶关于他改写口令签的判断。",
      "supersedes_fact_ids": [],
      "change": "姜守将苏叶的指控转化为待核验事项。",
      "source_evidence": "姜守低头续写：“苏叶提出风险判断，待以维护签拓印、原签时辰及现场记录核验。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "jiang-shou-liability",
      "state": "suspects",
      "belief": "维护签上有姜守签押，因此姜守须作为首要说明人在演武前提交可核验说明，否则按签押上报。",
      "supersedes_fact_ids": [],
      "change": "赵矩将对姜守的责任怀疑落实为首要说明人身份和提交说明的期限要求。",
      "source_evidence": "赵矩将维护签锁进木匣，贴上封条：“拿批签去阵务柜调拓印。明日申时前，给我一份阵堂能核的说明。若只有‘不是我’，我便照签押上报。”"
    }
  ],
  "thread_changes": [
    {
      "change": "姜守获得调取前日维护签拓印及原签存档时辰的正式工单入口。",
      "source_evidence": "“已构成任务依据。”姜守将工单推到他面前，“后续任务一：调取前日维护签拓印及原签存档时辰，请管事批准。”"
    },
    {
      "change": "赵矩批准调取维护签拓印，但限定必须柜房见证且不得碰运行阵眼。",
      "source_evidence": "片刻后，他在“调取维护签拓印”后重重签下一个“准”。\n\n“只准调拓印，柜房见证。不得碰运行阵眼。”"
    },
    {
      "change": "姜守下一步将前往阵务柜调取维护签拓印。",
      "source_evidence": "姜守拿着批签转身走向阵务柜。维护签拓印，是他在不能碰阵眼的情况下，唯一能先查的东西。"
    },
    {
      "change": "姜守手中已有候选人受伤记录、事故口令和两项工单。",
      "source_evidence": "姜守把候选人受伤记录、事故口令和两项工单夹进旁录簿。左掌仍在灰布下刺痛，最直接的试阵办法已经被禁令封死。"
    }
  ],
  "comedy_changes": [
    {
      "change": "姜守将赵矩“先把能证明的都写清”的推诿话写成任务依据，迫使赵矩面对流程。",
      "source_evidence": "姜守当即在下一栏写道：“赵矩管事指示：先把能证明的都写清。”\n\n赵矩眼角一跳：“这句不必记。”\n\n“已构成任务依据。”姜守将工单推到他面前，“后续任务一：调取前日维护签拓印及原签存档时辰，请管事批准。”"
    },
    {
      "change": "姜守把苏叶的安全条款提醒写入工单依据，使她的提醒反过来支持柜房见证流程。",
      "source_evidence": "苏叶下意识接道：“安全条款第九条，确实如此。”\n\n姜守补上一笔：“苏叶援引第九条，证明管事批准与柜房见证均属必要。”"
    },
    {
      "change": "苏叶因自己的安全提醒和条款熟悉被工单绑定为隔离协助人，不能只站在风险条款外指责。",
      "source_evidence": "赵矩看过工单，敲桌道：“你熟条款，就留一班。既看红绳，也看住他的手。”\n\n苏叶沉默片刻，在协助人一栏签名，字锋几乎划破纸面。"
    }
  ],
  "new_constraints": [
    {
      "change": "姜守必须在明日申时前交初步事故说明，并在演武前交复核说明，说明需包含签、时辰、伤情和现场记录。",
      "source_evidence": "赵矩合上半本事故簿：“外门演武前乙字场必须恢复。明日申时前交初步事故说明，演武前交复核说明。要有签、时辰、伤情和现场记录，别只说不是你。”"
    },
    {
      "change": "调取维护签拓印只能调拓印，且必须有柜房见证，姜守不得碰运行阵眼。",
      "source_evidence": "片刻后，他在“调取维护签拓印”后重重签下一个“准”。\n\n“只准调拓印，柜房见证。不得碰运行阵眼。”"
    },
    {
      "change": "苏叶已签隔离协助，但明确不认可姜守无辜。",
      "source_evidence": "“我只签隔离，不签你无辜。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守拿着赵矩批准的批签前往阵务柜调取前日维护签拓印及原签存档时辰，且调取需柜房见证。",
    "姜守仍是赵矩列明的首要说明人，明日申时前要交初步事故说明，演武前要交复核说明。",
    "姜守的 left-palm-burn 仍在，live-array-contact-ban 继续有效，不能直接接触运行阵眼。",
    "乙字训练剑阵已临时停用并拉设隔离红绳，事故原因未明。",
    "苏叶仍相信姜守主动改写口令签，但已签为隔离协助人，需看守测试区并阻止姜守违规接触运行阵眼。",
    "姜守已有候选人右肩木剑击伤记录、事故口令记录、调取维护签拓印工单和隔离测试区工单。"
  ],
  "deviations": []
}
```

## 第 2 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0002",
  "chapter": 2,
  "source_draft": "chapters/0002/draft.final.md",
  "source_sha256": "05a3e83aa4d8dd569a23c08a7e1fde7a3e353ca00653178b252102cda41750c5",
  "entity_changes": [
    {
      "change": "乙字训练剑阵在现场复核中错误多放第二轮木剑，仍未修复并继续停用。",
      "source_evidence": "备用剑架随之弹响。第二轮木剑竟被错位口令牵动，接连射出。第一柄钉入木靶，第二柄擦断红绳，第三柄正中偏斜的校准镜。"
    },
    {
      "change": "calibration-mirror 裂损，登记为不可现场修复且必须计赔。",
      "source_evidence": "裂镜被封条固定，登记牌上添了“不可现场修复、必须计赔”八字。"
    },
    {
      "change": "事故表已正式记录维护签拓印的证明范围、现场复核失败、姜守带伤违规接触运行阵眼、乙字训练剑阵多放一轮木剑、校准镜裂损与资格冻结。",
      "source_evidence": "赵矩回到案前，逐栏落笔：“现场复核失败。姜守，炼气二层，阵火灼伤未解除，违反禁令，带伤接触运行阵眼。后果：乙字训练剑阵多放一轮木剑，校准镜裂损。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "苏叶成为姜守违规接触运行阵眼、伤势加重、多放木剑和镜损的正式目击见证人。",
      "source_evidence": "苏叶的隔离木牌还在轻晃。她抿紧唇，写下：“已口头阻止。姜守仍接触阵眼。伤势加重、多放木剑、镜损，均亲眼所见。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 加重，症状升级为左掌由红转紫、指尖不受控颤动、灵气在伤处乱窜，基础吐纳只能勉强压住。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守踉跄退开，左掌已由红转紫，指尖不受控地颤动。灵气在伤处乱窜，连他强行运转的基础吐纳也只能勉强压住。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效，姜守伤势解除前不得直接接触运行阵眼。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "随后，他重重合上表夹：“剑阵继续停用。隔离绳外移一丈。姜守伤势解除前，不得直接接触运行阵眼。苏叶继续看守，证词候补。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "jiang-shou",
      "resource_id": "contribution-point",
      "operation": "consume",
      "amount": 2,
      "unit": "点",
      "resulting_balance": 6,
      "source_or_destination": "事故处罚扣除",
      "change": "姜守被扣除 contribution-point 2点，余额由8点变为6点。",
      "source_evidence": "赵矩取出姜守的贡献牌，连续扣下两道印记：“扣贡献二点。原有八点，现余六点。阵堂小考资格即刻冻结，待事故复核、赔偿排期与伤势验明后再议。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "jiang-shou",
      "fact_id": "maintenance-rubbing-limited-proof",
      "state": "knows",
      "belief": "维护签拓印只能证明维护项归姜守、签押是姜守、原签入柜时辰，不能证明口令错位由姜守改写。",
      "supersedes_fact_ids": [],
      "change": "姜守确认维护签拓印的证明范围和局限。",
      "source_evidence": "姜守将拓印举到光下：“能证明三件事。维护项归我，签押是我，原签何时入柜。不能证明口令错位由我改写。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "believes_false",
      "belief": "姜守为了催缴维修贡献，主动改写口令签，想让候选人吃苦头。",
      "supersedes_fact_ids": [],
      "change": "苏叶继续维持对姜守改写口令签的误信。",
      "source_evidence": "她仍按下见证印：“先说清楚，我还是认为口令签是你动的。你想催缴维修贡献，才故意让剑阵追人。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "jiang-shou-violation-witnessed",
      "state": "knows",
      "belief": "苏叶亲眼见到姜守在她口头阻止后仍接触运行阵眼，并造成伤势加重、多放木剑和镜损。",
      "supersedes_fact_ids": [],
      "change": "苏叶取得姜守新增违规及其后果的目击知识。",
      "source_evidence": "苏叶的隔离木牌还在轻晃。她抿紧唇，写下：“已口头阻止。姜守仍接触阵眼。伤势加重、多放木剑、镜损，均亲眼所见。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "maintenance-rubbing-limited-proof",
      "state": "knows",
      "belief": "维护签拓印仅证明签押、维护项及存档时辰，不能单独定责口令改写。",
      "supersedes_fact_ids": [],
      "change": "赵矩在已核事实栏正式承认维护签拓印不能单独定责口令改写。",
      "source_evidence": "赵矩看了他片刻，翻回前页，在已核事实栏补写：“维护签拓印仅证明签押、维护项及存档时辰，不能单独定责口令改写。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "jiang-shou-liability",
      "state": "knows",
      "belief": "姜守炼气二层，阵火灼伤未解除却违反禁令带伤接触运行阵眼，导致乙字训练剑阵多放一轮木剑和校准镜裂损。",
      "supersedes_fact_ids": [
        "jiang-shou-liability"
      ],
      "change": "赵矩对姜守责任的状态由维护签责任怀疑推进为对新增违规事实的正式记录。",
      "source_evidence": "赵矩回到案前，逐栏落笔：“现场复核失败。姜守，炼气二层，阵火灼伤未解除，违反禁令，带伤接触运行阵眼。后果：乙字训练剑阵多放一轮木剑，校准镜裂损。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "remaining-evidence-chain",
      "state": "investigating",
      "belief": "灵纹磨损、灵钉方向、回声阵牌与领用时辰仍未核验，口令错位责任尚无完整证据链。",
      "supersedes_fact_ids": [],
      "change": "姜守后续调查目标明确为维护签之外的证据链。",
      "source_evidence": "姜守收起拓印。左掌每颤一下，纸角便跟着轻响。资格已经冻结，镜债已经落账，剑阵仍伏在红绳内没有修好；而灵纹磨损、灵钉方向、回声阵牌与领用时辰，尚无一项填进表里。"
    }
  ],
  "thread_changes": [
    {
      "change": "姜守取得维护签拓印、原签入柜时辰与柜房见证印，但该线索只能证明签押和维护项，不能单独洗清或定责口令改写。",
      "source_evidence": "柜后执事将薄纸覆上旧签，以淡墨拓出字迹。拓印上，姜守的签押清清楚楚，维护项写的是：外沿灵纹补描，口令签复位查验。其下还有原签入柜时辰与执事见证印。"
    },
    {
      "change": "姜守阵堂小考资格被冻结，恢复资格需等待事故复核、赔偿排期与伤势验明后再议。",
      "source_evidence": "赵矩取出姜守的贡献牌，连续扣下两道印记：“扣贡献二点。原有八点，现余六点。阵堂小考资格即刻冻结，待事故复核、赔偿排期与伤势验明后再议。”"
    },
    {
      "change": "裂损校准镜的赔偿责任已经落到姜守账上。",
      "source_evidence": "赵矩走到镜前，用登记尺量过裂口，没有尝试扶正镜面：“校准镜裂损，不可现场修复，列入计赔。”\n\n“记我账上。”姜守道。\n\n“已经在你账上。”"
    },
    {
      "change": "乙字训练剑阵继续停用，隔离绳外移一丈，苏叶继续看守并作为证词候补。",
      "source_evidence": "随后，他重重合上表夹：“剑阵继续停用。隔离绳外移一丈。姜守伤势解除前，不得直接接触运行阵眼。苏叶继续看守，证词候补。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "赵矩用现场复核栏逼姜守补表，事故扩大后同一张表反而写入维护签不能单独定责的已核事实。",
      "source_evidence": "姜守没有争辩，只用发抖的右手指向事故表上方：“还缺备注。”\n\n苏叶望着他：“你还惦记那句？”\n\n“扣点归扣点，事实归事实。新增违规是带伤接触阵眼。原维护签不能单独证明我改写口令。”"
    },
    {
      "change": "苏叶被赵矩以看守栏条款反制，必须承担阻止姜守违规接触的见证职责。",
      "source_evidence": "赵矩看见她腰间木牌，将事故表推过去：“隔离协助人，签随行时辰。他若接触运行阵眼，你负责阻止并作证。”\n\n“我只是看守——”\n\n“看守栏包含违规阻止。”"
    }
  ],
  "new_constraints": [
    {
      "change": "姜守阵堂小考资格冻结，待事故复核、赔偿排期与伤势验明后再议。",
      "source_evidence": "赵矩取出姜守的贡献牌，连续扣下两道印记：“扣贡献二点。原有八点，现余六点。阵堂小考资格即刻冻结，待事故复核、赔偿排期与伤势验明后再议。”"
    },
    {
      "change": "calibration-mirror 不可现场修复且必须计赔，赔偿问题压在姜守账上。",
      "source_evidence": "裂镜被封条固定，登记牌上添了“不可现场修复、必须计赔”八字。"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 加重，左掌由红转紫、指尖颤动、导灵抖动和灵纹失稳更明显，基础吐纳只能勉强压住。",
    "live-array-contact-ban 继续有效，姜守伤势解除前不得直接接触运行阵眼。",
    "姜守 contribution-point 从8点被扣至6点，扣除的2点未退还。",
    "姜守阵堂小考资格已冻结，待事故复核、赔偿排期与伤势验明后再议。",
    "calibration-mirror 已裂损，登记为不可现场修复、必须计赔，且已经落到姜守账上。",
    "乙字训练剑阵仍未修复，继续停用，隔离绳外移一丈。",
    "赵矩事故表已写入：维护签拓印仅证明签押、维护项及存档时辰，不能单独定责口令改写；新增违规是姜守带伤接触运行阵眼并导致多放一轮木剑和镜损。",
    "苏叶仍误信姜守改写口令签，但已亲眼见到并记录姜守违规接触阵眼、伤势加重、多放木剑和镜损。",
    "灵纹磨损、灵钉方向、回声阵牌与领用时辰尚未填进表里，仍需核验。"
  ],
  "deviations": []
}
```

## 第 3 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0003",
  "chapter": 3,
  "source_draft": "chapters/0003/draft.final.md",
  "source_sha256": "11a057c392ddfd84aae49da5a4dc9f0aeb00ed01ec14ec1bbfca57b0d7bf1f92",
  "entity_changes": [
    {
      "change": "新增“共同事故隔离证词单”，由姜守记录并由苏叶签写复测前口令、复测时木剑多追一段、校准镜被击裂及其保留判断。",
      "source_evidence": "苏叶终于拿笔，重重写下：“复测前口令为‘后退三步，停剑’。复测时木剑多追一段，校准镜被击裂。本人仍保留姜守改写口令签之判断。”"
    },
    {
      "change": "事故表新增回声阵牌证据边界：只能证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。",
      "source_evidence": "赵矩这才在未核验栏后补写：“回声阵牌仅证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "苏叶因共同事故隔离证词单承担随行核对阵务柜记录的义务，但明确不替姜守免责。",
      "source_evidence": "苏叶沉默片刻，在单末补写：“随行核对，不作免责。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "recovery",
      "change": "姜守使用灼伤膏后，left-palm-burn 从加重状态部分缓解：灼痛减轻，但掌中仍刺痛，导灵时五指抖动、灵流散乱。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守用右手挑起药膏，薄薄涂过左掌。凉意刚渗进去，紫红的掌纹便猛地一抽。他闭目吐纳，把乱窜的灵气压回经脉。十息后，灼痛不再直钻臂弯，却仍像细针埋在掌中；他试着引过一缕灵气，五指立刻抖了一下，灵流也随之散乱。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 仍未解除，当前状态为伤势部分缓解但仍有刺痛及导灵抖动。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "值守弟子盖上药柜小章：“灼伤膏消耗一份。伤势部分缓解，仍有刺痛及导灵抖动。禁止接触运行阵眼继续有效。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效，姜守伤势未解除前不得接近运行阵眼三尺，不得接触运行阵眼。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "苏叶按住他的腕口：“安全条款第九：伤势未解除前，不得接近运行阵眼三尺。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "jiang-shou",
      "resource_id": "burn-salve",
      "operation": "consume",
      "amount": 1,
      "unit": "份",
      "resulting_balance": 0,
      "source_or_destination": "左掌阵火灼伤外敷治疗",
      "change": "姜守消耗1份灼伤膏，burn-salve 余额由1份变为0份。",
      "source_evidence": "值守弟子盖上药柜小章：“灼伤膏消耗一份。伤势部分缓解，仍有刺痛及导灵抖动。禁止接触运行阵眼继续有效。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "believes_false",
      "belief": "苏叶仍认为姜守为了催缴维修贡献改了口令，保留姜守改写口令签的判断，但其笃定已因回声阵牌只能复述而松动。",
      "supersedes_fact_ids": [],
      "change": "苏叶的误信未被淘汰，但开始动摇，并在证词中区分亲眼所见事实与自己的判断。",
      "source_evidence": "苏叶终于拿笔，重重写下：“复测前口令为‘后退三步，停剑’。复测时木剑多追一段，校准镜被击裂。本人仍保留姜守改写口令签之判断。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "echo-command-plate-limits",
      "state": "knows",
      "belief": "回声阵牌只留完整口令，不载说话者、不载时辰，不能单独定责，不能直接翻案。",
      "supersedes_fact_ids": [],
      "change": "姜守确认回声阵牌的证据边界，知道其不能单独定责或直接翻案。",
      "source_evidence": "“它只留完整口令。”姜守看向赵矩，“请记：不载说话者，不载时辰，不能单独定责。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "echo-command-plate-limits",
      "state": "knows",
      "belief": "回声阵牌只会复述完整口令，不能回答是谁喊的、何时收到或是否与姜守改签有关。",
      "supersedes_fact_ids": [],
      "change": "苏叶亲自追问后得知回声阵牌只能复述口令，不能提供说话者、时辰或定责信息。",
      "source_evidence": "苏叶俯身追问：“是谁喊的？”\n\n“后退三步，停剑。”\n\n“何时收到？”\n\n“后退三步，停剑。”\n\n“是不是姜守改签以后收到的？”\n\n“后退三步，停剑。”\n\n苏叶直起身，眼中的笃定松动了一线：“它只会复述。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "echo-command-plate-limits",
      "state": "knows",
      "belief": "回声阵牌仅证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。",
      "supersedes_fact_ids": [],
      "change": "赵矩将回声阵牌的证据边界写入事故表未核验栏。",
      "source_evidence": "赵矩这才在未核验栏后补写：“回声阵牌仅证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "remaining-evidence-chain",
      "state": "investigating",
      "belief": "下一步需要调维护签拓印原件，核灵纹磨损方向，查定向灵钉领用时辰与实物缺口，并结合证词核复测前后动作。",
      "supersedes_fact_ids": [
        "command-slip-verification-lead"
      ],
      "change": "姜守将后续调查目标细化为维护签拓印、灵纹磨损方向、定向灵钉领用时辰与实物缺口及证词核对。",
      "source_evidence": "姜守等他落笔：“下一步，调维护签拓印原件，核灵纹磨损方向，再查定向灵钉领用时辰与实物缺口。”\n\n“你想用这些翻案？”赵矩问。\n\n“阵牌不能翻案。”姜守逐项道，“维护签核签押内容，磨损核导灵偏向，灵钉记录核领用与缺口，证词核复测前后动作。合起来才够。”"
    }
  ],
  "thread_changes": [
    {
      "change": "调查从单纯争论姜守是否改写口令签，推进为需要核对维护签拓印、灵纹磨损方向、定向灵钉领用时辰与实物缺口的证据链。",
      "source_evidence": "姜守等他落笔：“下一步，调维护签拓印原件，核灵纹磨损方向，再查定向灵钉领用时辰与实物缺口。”"
    },
    {
      "change": "下一步行动时间与地点确定为明日辰初到阵务柜，姜守资格冻结仍照旧。",
      "source_evidence": "赵矩合上事故表：“明日辰初，阵务柜。冻结照旧。”"
    },
    {
      "change": "姜守保留事故表副页与苏叶证词单作为下一步查钉的凭据。",
      "source_evidence": "姜守收起事故表副页与证词单，退离隔离绳。\n\n“下一项，”他说，“查钉。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "姜守把苏叶的安全条款转写成她的监督、看守和记录义务，形成安全条款反差喜剧。",
      "source_evidence": "苏叶按住他的腕口：“安全条款第九：伤势未解除前，不得接近运行阵眼三尺。”\n\n姜守在单上续写：“隔离动作一，苏叶看守隔离绳。姜守靠近运行阵眼三尺，立即拦截。”"
    },
    {
      "change": "苏叶以条款阻止姜守单独复述事故经过，反被姜守推导成她必须签证词。",
      "source_evidence": "苏叶没有接：“事故相关人不得单独复述经过，须有旁证。这也是条款。”\n\n“所以你签。”姜守道，“不签，我只能单独复述，违反条款。签了，你执行条款。”"
    },
    {
      "change": "苏叶把三尺安全距离临时加到四尺，姜守想记录时被她阻止，延续条款被反用的笑点。",
      "source_evidence": "苏叶已经站到他左侧：“去训练场，只能到隔离绳外。离绳四尺。”\n\n“条款要求三尺。”\n\n“多一尺防你临时犯规。”\n\n姜守提笔欲记，苏叶一把按住纸：“这一尺不用写！”"
    }
  ],
  "new_constraints": [
    {
      "change": "姜守阵堂小考资格继续被冻结，待事故复核、赔偿排期与伤势验明后再议。",
      "source_evidence": "赵矩摊开事故表，先不写新栏，逐项宣读旧项：“姜守带伤接触运行阵眼，违反禁令，致左掌灼伤加重；错误复测使乙字训练剑阵多放一轮木剑，击裂校准镜。校准镜不可现场修复，计赔。扣贡献二点，余额六点。阵堂小考资格冻结，待事故复核、赔偿排期与伤势验明后再议。”"
    },
    {
      "change": "乙字训练场仍停用隔离，校准镜仍裂损且不可现场修复、计赔待排。",
      "source_evidence": "乙字训练场仍在停用。隔离绳外移一丈，裂开的校准镜放在木架上，白痕斜贯镜面，旁边悬着“不可现场修复，计赔待排”的木牌。"
    },
    {
      "change": "苏叶随行阵务柜，避免事故相关人单独调取记录，但不作免责。",
      "source_evidence": "姜守把证词单递给她：“保留。另加隔离义务：随行阵务柜，避免事故相关人单独调取记录。”\n\n“阵务柜没有运行阵眼。”\n\n“有领用册。”\n\n苏叶沉默片刻，在单末补写：“随行核对，不作免责。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 使用1份 burn-salve 后部分缓解，但仍有刺痛及导灵抖动，伤势未解除。",
    "live-array-contact-ban 继续有效，姜守伤势未解除前不得接近或接触运行阵眼。",
    "姜守 burn-salve 由1份消耗至0份。",
    "姜守 contribution-point 仍为6点，已扣2点未退还；阵堂小考资格仍冻结，待事故复核、赔偿排期与伤势验明后再议。",
    "乙字训练场仍停用隔离；calibration-mirror 仍裂损，不可现场修复，计赔待排。",
    "苏叶签下共同事故隔离证词单，记录复测前口令为“后退三步，停剑”、复测时木剑多追一段、校准镜被击裂；她仍保留姜守改写口令签的误信，但笃定已松动。",
    "回声阵牌已复述完整口令“后退三步，停剑”，但其证据边界已写入事故表：只证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。",
    "姜守下一步要在明日辰初去阵务柜调维护签拓印原件，核灵纹磨损方向，查定向灵钉领用时辰与实物缺口。",
    "苏叶已补写“随行核对，不作免责”，下一章需要随行阵务柜或承担证词补签压力。",
    "赵矩事故表已固定姜守带伤接触运行阵眼、左掌灼伤加重、乙字训练剑阵多放一轮木剑、击裂校准镜、扣贡献二点、余额六点、阵堂小考资格冻结等后果，并补写回声阵牌不能单独定责。"
  ],
  "deviations": []
}
```

## 第 4 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0004",
  "chapter": 4,
  "source_draft": "chapters/0004/draft.final.md",
  "source_sha256": "822ea5c761663958cd604df8ad26d0aaba296634e12bbc8bcfae62a593c27f30",
  "entity_changes": [
    {
      "change": "事故表新增已核记录：维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。",
      "source_evidence": "他终究写下：“维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。”"
    },
    {
      "change": "事故表新增三枚定向灵钉账面与现场登记不合、无对应领用登记且需核验的记录。",
      "source_evidence": "赵矩夺笔落字：“三枚定向灵钉账面与现场登记不合，无对应领用登记，需核验。”"
    },
    {
      "change": "袁客留下口头记录：临时拿过几枚定向灵钉周转，但未填明数量、时辰、归还去向。",
      "source_evidence": "请管事写：三枚定向灵钉缺口需继续核验；袁客口称临时拿过几枚周转，未填数量、时辰、归还去向。”"
    },
    {
      "change": "苏叶的证词单新增见证内容：三枚缺口客观存在，袁客口称临时拿过几枚但未明数量及时辰。",
      "source_evidence": "苏叶看着单子，又看自己的证词单，咬唇添字：“本人见证阵务柜领用簿与乙字现场登记相差三枚，未见对应领用登记。袁客口称临时拿过几枚定向灵钉周转，未明数量及时辰。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "苏叶继续作为共同事故隔离证词单的随行见证人，见证姜守未触碰阵材和阵眼。",
      "source_evidence": "“同意。”姜守点头，“我不碰阵材。查簿。样钉由值守弟子夹出，放停阵材料台。苏叶见证我未伸手。”"
    },
    {
      "change": "赵矩因事故表补事实的压力，被迫把维护签不能单独定责和三枚灵钉缺口写入记录。",
      "source_evidence": "赵矩看着自己亲手用来扣贡献、冻结资格的事故表，脸色发沉。若这表不能补事实，前面的裁定也不牢。"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 仍未解除，灼伤膏凉意已散，左掌仍刺痛。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守只用右手翻页，左掌在袖中一阵刺痛。灼伤膏的凉意已散，导灵虽未动，掌心仍像被细针沿纹路敲。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效，姜守伤势未解除，禁近运行阵眼三尺，且不能触碰阵材以免混淆责任。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "苏叶翻条款：“伤势未解除，禁近运行阵眼三尺。阵务柜不是阵眼，但阵材触碰会混责任。姜守只能翻簿，不能碰钉。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "jiang-shou",
      "fact_id": "direction-spirit-nail-gap",
      "state": "knows",
      "belief": "阵堂定向灵钉账面十二枚，乙字训练剑阵现场登记九枚，上次归还签押未见三枚入库，对应领用时辰为空。",
      "supersedes_fact_ids": [],
      "change": "姜守查明三枚定向灵钉未登记缺口。",
      "source_evidence": "“阵堂公物账面，十二枚。”姜守念，“乙字训练剑阵现场登记，九枚在位。上次归还签押，未见三枚入库。对应领用时辰，空。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "maintenance-sign-not-sole-liability",
      "state": "knows",
      "belief": "维护签存在，但不足以单独定责，需合并灵纹、灵钉、现场记录核验。",
      "supersedes_fact_ids": [],
      "change": "姜守推动赵矩在事故表上确认维护签不能单独定责。",
      "source_evidence": "他终究写下：“维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "yuan-ke-spirit-nail-statement",
      "state": "knows",
      "belief": "袁客口称自己临时拿过几枚定向灵钉周转，但没有填明数量、时辰、归还处；三枚缺口仍待其补正。",
      "supersedes_fact_ids": [],
      "change": "姜守记录袁客关于定向灵钉周转的含糊口头说法。",
      "source_evidence": "袁客立刻拱手：“赵管事，我只是说外门常有周转。我确实临时拿过几枚定向灵钉，想着补齐就好，没想到查得这么急。”\n\n姜守在口头记录栏写下原话：“临时拿过几枚定向灵钉周转。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "remaining-evidence-chain",
      "state": "investigating",
      "belief": "下一步还要查维护签拓印、灵纹磨损方向、灵钉方向；本章只先固定三枚定向灵钉缺口。",
      "supersedes_fact_ids": [
        "remaining-evidence-chain"
      ],
      "change": "姜守把后续调查目标推进到维护签拓印、灵纹磨损方向和灵钉方向。",
      "source_evidence": "“在。”姜守收好待补领用单，“所以还要查维护签拓印、灵纹磨损方向、灵钉方向。今天只处理三枚不能写成若干。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "direction-spirit-nail-gap",
      "state": "knows",
      "belief": "苏叶亲眼见证阵务柜领用簿与乙字现场登记相差三枚，未见对应领用登记。",
      "supersedes_fact_ids": [],
      "change": "苏叶知道三枚灵钉缺口客观存在。",
      "source_evidence": "苏叶看着单子，又看自己的证词单，咬唇添字：“本人见证阵务柜领用簿与乙字现场登记相差三枚，未见对应领用登记。袁客口称临时拿过几枚定向灵钉周转，未明数量及时辰。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "believes_false",
      "belief": "苏叶仍未确认姜守没有改签；她认为三枚灵钉缺口不能证明姜守没改签，但也把自己的判断暂不并入事实。",
      "supersedes_fact_ids": [],
      "change": "苏叶的 command-slip-tamperer 误信继续动摇但未被淘汰。",
      "source_evidence": "写完，她声音低了些：“这不能证明姜守没改签。”\n\n姜守道：“同意。不能单独证明。也不能证明我改签。”\n\n苏叶没反驳，只在旁补：“本人判断另列，暂不并入事实。”"
    },
    {
      "character_id": "yuan-ke",
      "fact_id": "spirit-nail-borrowing",
      "state": "conceals",
      "belief": "袁客承认临时拿过几枚定向灵钉周转，但回避具体数量、时辰、归还去向，并试图不把话写死。",
      "supersedes_fact_ids": [
        "spirit-nail-borrowing"
      ],
      "change": "袁客的隐瞒状态更新为已留下含糊口头记录但仍不补登记。",
      "source_evidence": "姜守抬笔避开：“没写死。因为你不填数量和时辰，所以写‘几枚’。但事故表数字栏已核三枚缺口，待你补正。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "direction-spirit-nail-gap",
      "state": "knows",
      "belief": "赵矩已在事故表上记录三枚定向灵钉账面与现场登记不合，无对应领用登记，需核验。",
      "supersedes_fact_ids": [],
      "change": "赵矩正式知道并记录三枚定向灵钉缺口。",
      "source_evidence": "赵矩夺笔落字：“三枚定向灵钉账面与现场登记不合，无对应领用登记，需核验。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "maintenance-sign-not-sole-liability",
      "state": "knows",
      "belief": "赵矩已记录维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。",
      "supersedes_fact_ids": [],
      "change": "赵矩正式记录维护签不能单独定责。",
      "source_evidence": "他终究写下：“维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。”"
    }
  ],
  "thread_changes": [
    {
      "change": "定向灵钉缺口线索成立：账面十二枚、现场九枚、三枚无对应领用登记。",
      "source_evidence": "“阵堂公物账面，十二枚。”姜守念，“乙字训练剑阵现场登记，九枚在位。上次归还签押，未见三枚入库。对应领用时辰，空。”"
    },
    {
      "change": "下一步调查入口转向停阵状态下的灵钉方向和灵纹磨损方向比对。",
      "source_evidence": "姜守望向白布上的样钉箭头，又看向隔离绳内静止的阵纹：“下一项，不碰阵眼，先看钉尾朝向，再看磨痕往哪边拖。”"
    },
    {
      "change": "袁客没有完全认罪，只留下临时拿过几枚定向灵钉周转的含糊记录，并称回去查。",
      "source_evidence": "袁客沉默片刻，没接笔：“我回去查查。”\n\n姜守在单末写：“当场未填，称回去查。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "维修工单的数字栏逼迫赵矩不能把三枚写成若干。",
      "source_evidence": "赵矩伸手拿笔：“记，定向灵钉若干缺口待查。”\n\n姜守把事故表推前一寸：“事故表有数字栏。”\n\n赵矩笔尖停住。\n\n“若干不能进数字栏。三枚能。”"
    },
    {
      "change": "姜守把袁客的模糊词逐项改造成待补领用单栏位。",
      "source_evidence": "姜守又写一行：“领用人：大家。需改为姓名。”"
    },
    {
      "change": "姜守坚持只让三枚说明三枚，不扩大成未证实罪名。",
      "source_evidence": "廊柱阴影里，袁客没再说“若干”，只拢袖道：“几枚小钉，未必能说明剑阵为何追人。”\n\n姜守把待补领用单收进夹板：“所以三枚先说明三枚。”"
    }
  ],
  "new_constraints": [
    {
      "change": "姜守阵堂小考资格仍冻结，扣除的二点贡献不退，校准镜裂损仍需赔偿，禁令照旧。",
      "source_evidence": "赵矩补完事故表，扔回给他：“资格仍冻结。扣的二点贡献不退。裂镜照赔。禁令照旧。”"
    },
    {
      "change": "乙字剑阵仍处停阵隔离状态，姜守不得越过隔离绳接触阵眼。",
      "source_evidence": "停阵材料台就在训练场外。隔离绳后，乙字剑阵安静伏着，阵眼封条未动。姜守没有越线，只把样钉方向图、领用簿摘录和待补领用单并排压在白布上。"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 未解除，灼伤膏凉意已散，左掌仍刺痛；未导灵时也会刺痛。",
    "live-array-contact-ban 继续有效，姜守伤势未解除，禁近运行阵眼三尺，不得触碰运行阵眼；本章他未越线。",
    "乙字训练剑阵仍停阵隔离，阵眼封条未动，尚未修复。",
    "calibration-mirror 仍裂损照赔；姜守 contribution-point 仍为6点，已扣2点不退；阵堂小考资格仍冻结。",
    "阵堂 direction-spirit-nail 账面十二枚，乙字训练剑阵现场登记九枚，三枚无对应领用登记；该缺口已写入事故表，需继续核验。",
    "赵矩已在事故表记录：维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。",
    "袁客口称临时拿过几枚定向灵钉周转，但未填数量、时辰、归还去向，当场称回去查；不得视为完全认罪。",
    "苏叶见证三枚灵钉缺口和袁客含糊口头说法；她的 command-slip-tamperer 误信已动摇但未淘汰，仍认为三枚缺口不能证明姜守没改签。",
    "姜守下一步要在不碰阵眼的前提下，先看钉尾朝向，再看灵纹磨痕往哪边拖，并继续查维护签拓印、灵纹磨损方向、灵钉方向。"
  ],
  "deviations": []
}
```

## 第 5 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0005",
  "chapter": 5,
  "source_draft": "chapters/0005/draft.final.md",
  "source_sha256": "52d11c2f9b956e3f354a18c5f4421eceb18d04f8595949c3efe3a619b860f53c",
  "entity_changes": [
    {
      "change": "乙字训练剑阵停阵材料台现场登记的九枚定向灵钉完成外观比对，其中左三、左四、左五三处相邻钉位的现钉尾朝向与旧压痕不一致。",
      "source_evidence": "“左三、左四、左五。”姜守短声道，“三处相邻。现钉尾与旧压痕不合。”"
    },
    {
      "change": "乙字训练剑阵三处异常钉位的灵纹磨痕被记录为拖向“追后三步”执行侧。",
      "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
    },
    {
      "change": "共同事故隔离证词新增苏叶全程代放纸框、读尺距、签注见证的现场记录，并确认姜守未越线、未触碰阵眼及阵材。",
      "source_evidence": "苏叶接过笔，认真签下姓名，又在旁边补了一句：全程停阵，姜守未越线、未触碰阵眼及阵材。"
    }
  ],
  "relationship_changes": [
    {
      "change": "苏叶因共同事故隔离证词，从单纯阻止姜守靠近，变成代放观察标记并签押的见证执行人。",
      "source_evidence": "姜守取出共同事故隔离证词单，用右手提笔：“阻止方式：由苏叶代放观察标记，避免姜守接触现场。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 仍未解除；灼伤膏凉意已散，左掌持续刺痛，影响书写稳定。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守站在线外，左手垂在袖中。灼伤膏的凉意早已散尽，掌心一阵阵刺痛，像有细针顺着旧伤往指缝里钻。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 在观察时再次刺痛，导致右手记录字迹发抖。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他运起灵纹辨识，并未导灵入阵，只凭纹路的深浅、焦边和磨亮处辨认。左掌虽未使力，掌心仍猛地抽痛了一下。他右手握笔，笔锋在纸上抖出一小截墨尾。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效；观察期间姜守不得越过三尺禁线，不得触碰阵眼及阵材。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "赵矩沿线走了一圈，又俯身查过阵眼封条，才把事故表夹在木板上：“封条无损。停阵未解。观察期间，姜守不得越线，不得触碰阵眼及阵材。谁动过什么，写清楚。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "ability",
      "change": "pattern-reading 本章用于辨认灵纹磨损和导灵方向，且明确不能判断移动灵钉的人。",
      "state_id": "pattern-reading",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“谁拖的？”\n\n“不知道。”姜守答得干脆，“灵纹辨识只认磨损和方向，不认手。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "jiang-shou",
      "fact_id": "array-command-error-cause",
      "state": "investigating",
      "belief": "追后三步的错误证据链新增三处钉尾与旧压痕不合、灵纹磨痕拖向执行侧；但仍不能单独定责，需要继续合并维护签拓印和灵钉领用时辰。",
      "supersedes_fact_ids": [],
      "change": "姜守将调查从灵钉数量缺口推进到方向异常与磨痕异常，并保留责任边界。",
      "source_evidence": "“所以要合并时辰。”姜守道。"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "remaining-evidence-chain",
      "state": "investigating",
      "belief": "下一步要追查三枚定向灵钉的数量、领用时辰、归还去向和经手人，袁客是重点对象。",
      "supersedes_fact_ids": [],
      "change": "姜守在抄录纸末尾列出下一步追问项，并写上袁客名字。",
      "source_evidence": "他在末尾补了四项：三枚数量，领用时辰，归还去向，经手人。\n\n最上方写着袁客的名字。"
    },
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "believes_false",
      "belief": "苏叶对姜守改签的判断继续后移、动摇，但仍不撤回；她认为三枚缺口和三处错向都不能直接证明姜守没改，需等维护签拓印入柜时辰与灵钉领用、归还时辰对上。",
      "supersedes_fact_ids": [],
      "change": "苏叶承认方向异常使她先前判断后移，但明确不撤回 command-slip-tamperer 误信。",
      "source_evidence": "“这些方向，确实不像只凭一张维护签就能解释。”她说，“我先前对你改签的判断，要再往后放。”\n\n姜守问：“撤回？”\n\n“不撤。”苏叶收起竹尺，“三枚缺口、三处错向，都不能直接证明你没改。等维护签拓印的入柜时辰，与灵钉领用、归还时辰对上，我再改证词。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "accident-record-boundary",
      "state": "knows",
      "belief": "事故表已经写明三处相邻钉位的钉尾朝向与旧压痕不一致，灵纹磨痕拖向“追后三步”执行侧；该方向异常不得单独定责，必须与维护签拓印和定向灵钉领用时辰合并核验。",
      "supersedes_fact_ids": [],
      "change": "赵矩受同一事故表约束，将钉尾朝向、旧压痕和灵纹磨痕方向异常写入新增栏，并注明合并核验边界。",
      "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
    }
  ],
  "thread_changes": [
    {
      "change": "事故复核从账面缺三枚定向灵钉推进到实物方向异常：现场登记九枚中三处相邻钉位异常。",
      "source_evidence": "赵矩又添上：“现场登记九枚中，三处相邻钉位异常。”"
    },
    {
      "change": "责任归属仍未裁定，方向异常必须与维护签拓印、定向灵钉领用时辰合并核验。",
      "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
    },
    {
      "change": "下一步事故流程转向追查灵钉领用时辰。",
      "source_evidence": "赵矩合上事故表：“资格冻结不变，扣去的两点贡献不退，裂镜照赔。明日先追灵钉领用时辰。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "苏叶原本只负责阻止姜守违规，却被姜守和事故表流程反推成代放标记、读尺距、补签注的执行人。",
      "source_evidence": "“只写‘你不能碰’，证词不完整。要写谁来碰标记，标记碰哪里。”"
    },
    {
      "change": "安全条款的执行让苏叶多出三只纸框、九次尺距和两处签押的劳动。",
      "source_evidence": "姜守道：“你守住了。只是这条线附带三只纸框、九次尺距和两处签押。”"
    },
    {
      "change": "赵矩以事故表格式否定苏叶想写“被迫”的抱怨。",
      "source_evidence": "“哪两个？”\n\n“被迫。”\n\n赵矩淡淡道：“事故表没有‘被迫’栏。”"
    }
  ],
  "new_constraints": [
    {
      "change": "乙字训练剑阵继续停阵隔离，封条无损，停阵未解。",
      "source_evidence": "赵矩沿线走了一圈，又俯身查过阵眼封条，才把事故表夹在木板上：“封条无损。停阵未解。观察期间，姜守不得越线，不得触碰阵眼及阵材。谁动过什么，写清楚。”"
    },
    {
      "change": "姜守阵堂小考资格冻结不变，已扣两点贡献不退，校准镜裂损仍需照赔。",
      "source_evidence": "赵矩合上事故表：“资格冻结不变，扣去的两点贡献不退，裂镜照赔。明日先追灵钉领用时辰。”"
    },
    {
      "change": "本章新增实物异常不能单独定责，只能作为与维护签拓印、定向灵钉领用时辰合并核验的证据。",
      "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 未解除；灼伤膏凉意已散，左掌持续刺痛，书写会因疼痛发抖。",
    "live-array-contact-ban 继续有效；本章姜守全程未越过三尺禁线，未触碰阵眼及阵材。",
    "乙字训练剑阵仍停阵隔离，封条无损，未修复，未启动整阵测试。",
    "calibration-mirror 仍裂损照赔；姜守 contribution-point 余额仍为6点，已扣2点不退；阵堂小考资格仍冻结。",
    "阵堂 direction-spirit-nail 账面仍为十二枚；乙字训练剑阵现场登记九枚，其中左三、左四、左五三处相邻钉位现钉尾朝向与旧压痕不合。",
    "灵纹磨痕已记录为拖向“追后三步”执行侧；该方向异常只能说明实物方向异常，不能单独判断责任人。",
    "赵矩事故表新增记录：现场登记九枚中三处相邻钉位异常，灵纹磨痕拖向“追后三步”执行侧，须与维护签拓印、定向灵钉领用时辰合并核验。",
    "苏叶作为代放人及见证人已签押，并确认全程停阵、姜守未越线、未触碰阵眼及阵材；她的 command-slip-tamperer 误信继续动摇但未淘汰。",
    "苏叶仍要求等维护签拓印入柜时辰与灵钉领用、归还时辰对上后，才改证词。",
    "姜守下一步已列出追查项：三枚数量、领用时辰、归还去向、经手人；袁客仍是需要追问的对象。"
  ],
  "deviations": []
}
```

## 第 6 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0006",
  "chapter": 6,
  "source_draft": "chapters/0006/draft.final.md",
  "source_sha256": "36b9988ca75468680c554614f8445a34cbdded0190b196de5903d10c1a32f2d7",
  "entity_changes": [
    {
      "change": "事故表新增并列核验页：维护签拓印、原签入柜时辰、柜房见证印、三处钉尾异常、灵纹磨痕方向被放入同一核验链，且维护签不能单独定责。",
      "source_evidence": "赵矩这才落笔：维护签拓印与原签入柜时辰、柜房见证印核验无误；入柜时辰早于部分定向灵钉方向异常记录；维护签不得单独作为口令错位定责依据，须与灵纹磨痕、灵钉领用及现场时辰合并核验。"
    },
    {
      "change": "袁客未登记借走三枚 direction-spirit-nail 的责任边界成立；具体归还去向未明，且不扩展推定其他阵材短缺责任。",
      "source_evidence": "赵矩随即加盖核验印，在事故表新增页写明：三枚定向灵钉由袁客经手未登记借走成立，具体归还去向未明；本项仅核至三枚缺口，不据此推定其他阵材短缺责任。"
    },
    {
      "change": "事故表最终合并记录：袁客三枚定向灵钉未登记借走成立；维护签不能单独定责；姜守原有带伤违规、裂镜赔偿、扣点和资格冻结仍执行。",
      "source_evidence": "赵矩将两页合并誊写：“三枚定向灵钉未登记借走成立。维护签不能单独定责。姜守带伤校阵违规、裂镜赔偿、扣除二点贡献及资格冻结，仍照原栏执行。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "闻岚允许姜守准备停阵监督下的局部低强度校阵方案，但前提是先验左掌伤势，且不免除姜守带伤违规。",
      "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
    },
    {
      "change": "苏叶确认自己下一步会到场见证闻岚安排的伤势验看与方案审查，伤势不合则方案停止。",
      "source_evidence": "苏叶收起短令：“我到场见证。伤势不合，方案当场止。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 仍未解除；未导灵时仍刺痛。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他说一句，放一样。左掌藏在袖中，未曾导灵，灼伤处仍一阵阵刺痛。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 影响签字动作，疼痛导致右手轻颤并拖出墨尾；未解除。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守签字时，左掌疼得右手也轻颤，末笔拖出一道墨尾。苏叶立即抽走印泥：“只许签，不许导灵压印。我代放，赵管事见证。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效；复核期间姜守不得触碰阵材，不得因证据进展靠近乙字阵眼三尺。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "苏叶先看他的手：“复核期间不得触碰阵材，不得以证据有利为由靠近乙字阵眼三尺。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 在闻岚短令中再次确认：阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "jiang-shou",
      "fact_id": "array-command-error-cause",
      "state": "investigating",
      "belief": "姜守掌握的证据链已推进为：维护签拓印入柜时辰、钉位记录、磨痕方向、三枚未登记单和伤势验看单需带去下一步复验；仍未最终定责。",
      "supersedes_fact_ids": [],
      "change": "姜守把下一步复验所需证据明确整理为五项。",
      "source_evidence": "姜守夹紧事故表：“明日带五项。拓印。钉位记录。磨痕方向。三枚未登记单。伤势验看单。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "remaining-evidence-chain",
      "state": "investigating",
      "belief": "袁客三枚定向灵钉由本人经手、未登记借走已成立，但归还去向仍待核。",
      "supersedes_fact_ids": [],
      "change": "姜守将追问结果更新为三枚、袁客经手、未登记借走、去向待核。",
      "source_evidence": "姜守没有往别处追，只写下：“三枚。袁客经手。未登记借走。去向待核。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "believes_false",
      "belief": "苏叶已认为“姜守主动改签”不能再作单一解释，并将该判断降为待淘汰，等待闻岚停阵复验；但她尚未正式撤回。",
      "supersedes_fact_ids": [],
      "change": "苏叶的 command-slip-tamperer 误信被降为待淘汰，但未正式 supersedes。",
      "source_evidence": "“‘姜守主动改签’不能再作单一解释。”苏叶提笔，在自己原证词旁添了一行，“判断降为待淘汰，等闻师姐停阵复验。现在不正式撤回。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "array-command-error-cause",
      "state": "investigating",
      "belief": "苏叶知道维护签入柜时辰、部分钉尾异常记录、磨痕方向和袁客三枚未登记借走互相牵制，使姜守主动改签的单一解释接不上。",
      "supersedes_fact_ids": [],
      "change": "苏叶将四项证据并列后，明确发现姜守主动改写口令签的单一路径在时辰和实物记录上接不上。",
      "source_evidence": "她逐项看完，才道：“若说你主动改写口令签，再靠灵钉造成错向，时辰接不上。若说你先动灵钉再改签，磨痕、例检记录和袁客这三枚也不能全接上。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "accident-table-boundary",
      "state": "knows",
      "belief": "赵矩已在事故表中确认维护签不能单独定责，三枚定向灵钉未登记借走成立；同时姜守带伤违规、裂镜赔偿、扣二点贡献及资格冻结仍执行。",
      "supersedes_fact_ids": [],
      "change": "赵矩正式把灵钉缺口、维护签责任边界和姜守原有处分分栏并存。",
      "source_evidence": "赵矩将两页合并誊写：“三枚定向灵钉未登记借走成立。维护签不能单独定责。姜守带伤校阵违规、裂镜赔偿、扣除二点贡献及资格冻结，仍照原栏执行。”"
    },
    {
      "character_id": "yuan-ke",
      "fact_id": "spirit-nail-borrowing",
      "state": "knows",
      "belief": "袁客知道自己经手三枚定向灵钉且未登记，并已被迫写下姓名；但仍称具体归还去向不能确定。",
      "supersedes_fact_ids": [],
      "change": "袁客从含糊承认周转更新为已承认三枚由自己经手且未登记。",
      "source_evidence": "袁客捏起笔，在数量栏写下一个“三”。\n\n“三枚。我经手。未登记。”"
    },
    {
      "character_id": "yuan-ke",
      "fact_id": "spirit-nail-borrowing-destination",
      "state": "conceals",
      "belief": "袁客不交代三枚定向灵钉后来去了何处，也不扩展说明别处短缺和其他经手人。",
      "supersedes_fact_ids": [],
      "change": "袁客仍回避归还去向及长期短缺关系。",
      "source_evidence": "“没有归还记录。”袁客放下笔，“三枚后来去了何处，我不能确定。别处还缺多少、谁拿过什么，不在我这张单里。”"
    },
    {
      "character_id": "wen-lan",
      "fact_id": "qualification-result",
      "state": "investigating",
      "belief": "闻岚已阅新增页，认为灵纹、领用、时辰可合并复验，但后果另记，姜守带伤违规不免；下一步须先验左掌伤势，再审停阵监督下局部低强度校阵方案。",
      "supersedes_fact_ids": [],
      "change": "闻岚把证据进展转化为复验流程入口，而非直接免除处分或解冻资格。",
      "source_evidence": "“新增页已阅。灵纹、领用、时辰可合并复验，后果另记。姜守带伤违规不免。”"
    }
  ],
  "thread_changes": [
    {
      "change": "乙字训练剑阵仍未修复，下一步不是启动整阵，而是明日辰初先验伤，再审停阵监督下局部低强度校阵方案。",
      "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
    },
    {
      "change": "证据链核心拼合完成：维护签入柜时辰、部分钉尾异常记录、磨痕方向、袁客三枚灵钉未登记借走被并列审视。",
      "source_evidence": "苏叶没有立刻签。她把新增页拖到前页旁，将四项记录排成一列：维护签酉初二刻入柜；部分钉尾异常记录在后；磨痕拖向“追后三步”执行侧；三枚灵钉由袁客在签入柜后、例检前未登记借走。"
    }
  ],
  "comedy_changes": [
    {
      "change": "袁客用“周转”“大家都用”“大约还到别处”等模糊说法回避责任，姜守逐项拆成数量、时辰、归还去向、领用人姓名四个待补栏，迫使其至少承认三枚未登记。",
      "source_evidence": "袁客盯着四个整整齐齐的“待补”：“姜师弟，你把我一句话拆成了四桩事。”\n\n“本来就是四桩。”"
    },
    {
      "change": "赵矩把工单字面执行到底，明确领用栏、时辰栏、归还栏都不接受袁客的模糊词。",
      "source_evidence": "赵矩翻开事故表：“领用栏不收‘周转’，时辰栏不收‘大概’，归还栏也没有‘大家’这个去向。至少补一项可核事实，否则记四项均拒答。”"
    },
    {
      "change": "袁客试图把“借走”改回“周转”，姜守用表格逻辑要求填写转入处，最终迫使袁客接受“借走”表述。",
      "source_evidence": "袁客指着“借走”二字：“我说的是周转。”\n\n姜守把表转回去：“周转需有转入处。请填。”\n\n袁客看了半晌，又把纸推回来：“借走便借走。”"
    }
  ],
  "new_constraints": [
    {
      "change": "姜守带伤校阵违规事实不因维护签核验改变，仍在事故表第五栏单列。",
      "source_evidence": "写完，他又在第五栏补道：姜守带伤私自低强度校阵之违规事实，不因本项核验改变。"
    },
    {
      "change": "姜守原有裂镜赔偿、扣除二点贡献及资格冻结继续执行；没有退点、解冻或免赔。",
      "source_evidence": "赵矩将两页合并誊写：“三枚定向灵钉未登记借走成立。维护签不能单独定责。姜守带伤校阵违规、裂镜赔偿、扣除二点贡献及资格冻结，仍照原栏执行。”"
    },
    {
      "change": "下一步复验前置条件为明日辰初先验左掌伤势，再审停阵监督下局部低强度校阵方案；阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。",
      "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 未解除；左掌未导灵时仍刺痛，签字时疼痛会导致右手轻颤。",
    "live-array-contact-ban 继续有效；阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼或因证据有利靠近乙字阵眼三尺。",
    "乙字训练剑阵仍停阵隔离，尚未修复，尚未启动整阵测试；下一步只能准备停阵监督下局部低强度校阵方案。",
    "calibration-mirror 裂镜赔偿仍照原栏执行；姜守 contribution-point 仍为6点，已扣2点不退；阵堂小考资格仍冻结。",
    "事故表已记录：维护签拓印与原签入柜时辰、柜房见证印核验无误；维护签入柜时辰为酉初二刻，早于部分定向灵钉方向异常记录。",
    "事故表已记录：左三、左四、左五三处钉尾朝向与旧压痕不合，灵纹磨痕拖向“追后三步”执行侧。",
    "事故表已写明：维护签不得单独作为口令错位定责依据，须与灵纹磨痕、灵钉领用及现场时辰合并核验。",
    "袁客未登记借走三枚 direction-spirit-nail 已成立；具体归还去向未明；本项仅核至三枚缺口，不推定其他阵材短缺责任。",
    "苏叶的 command-slip-tamperer 误信未正式淘汰；她已将“姜守主动改签”判断降为待淘汰，等待闻岚停阵复验。",
    "闻岚已阅新增页，认可灵纹、领用、时辰可合并复验，但姜守带伤违规不免；明日辰初先验左掌伤势，再审停阵监督下局部低强度校阵方案。",
    "苏叶会到场见证下一步验伤与方案审查；伤势不合，方案当场止。",
    "姜守准备明日带五项材料：拓印、钉位记录、磨痕方向、三枚未登记单、伤势验看单。"
  ],
  "deviations": []
}
```

## 第 7 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0007",
  "chapter": 7,
  "source_draft": "chapters/0007/draft.final.md",
  "source_sha256": "a8def00da3b975b0c8086ee6ed15e24a59e368831df869688ce2a36f6da48679",
  "entity_changes": [
    {
      "change": "乙字训练剑阵仍处于停阵隔离状态，本章只完成三处外缘灵纹试调，未启动整阵、未恢复口令，左五尚需另定停阵步骤。",
      "source_evidence": "这次试调没有启动整阵，也没有恢复口令，只确认三处外缘调整路径可行，其中左五尚需另定停阵步骤。"
    },
    {
      "change": "三处异常钉位外缘试调结果确定：左三偏向可压回，左四可压回但迟滞，左五仍偏且不得继续。",
      "source_evidence": "闻岚收针。苏叶报下三处刻度，赵矩逐项记表：左三偏向可压回，左四可压回但迟滞，左五仍偏，不得继续。"
    },
    {
      "change": "后续停阵调整获得许可，但范围仍限三处分步调整，禁止启动完整乙字训练剑阵和完整口令复验。",
      "source_evidence": "闻岚在方案下添注：“外缘灵纹试调完成。准许后续按三处分步调整，不得启动完整乙字训练剑阵，不得进行完整口令复验。”"
    },
    {
      "change": "袁客本章责任边界仍止于三枚定向灵钉未登记借走，其他阵材短缺不作推定。",
      "source_evidence": "“今日责任止于已核部分。”闻岚道，“三枚，未登记借走。其他阵材短缺不作推定。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "苏叶正式撤回对姜守主动改写口令签的判断，但仍坚持姜守带伤违规、禁令和后果不撤。",
      "source_evidence": "她按下见证印：“我撤回改签判断。但带伤私自校阵是另一项事实，禁令与后果不撤。”"
    },
    {
      "change": "苏叶在后续复验中的协作角色确定为递工具、读刻度、写见证，同时限制姜守只能口述。",
      "source_evidence": "苏叶把工具递送栏移到自己面前，签下姓名：“下一次你只许口述。我递工具、读刻度、写见证。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 经闻岚验看确认未解除；短时低强度导灵观察完成后，姜守不得接触运行阵眼，今日不得再导灵。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "闻岚落笔：“left-palm-burn未解除。短时低强度导灵观察已完成，不得接触运行阵眼。今日不得再导灵。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效：三尺禁线不撤，姜守不得导灵。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "闻岚在方案角上盖印：“准予审证。三尺禁线不撤，姜守不得导灵。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "姜守新增本日不得再导灵的临时限制；伤势未解除，禁令继续。",
      "state_id": "no-more-guiding-today",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "她又看向姜守：“今日不得再导灵。伤势未解除，禁令继续。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "wen-lan",
      "fact_id": "array-command-error-cause",
      "state": "knows",
      "belief": "闻岚已合并采信维护签入柜时辰、见证印、钉尾异常、磨痕拖向、三枚灵钉未登记缺口，并据此裁定这些事实足以排除姜守主动改写口令签这一单一判断，但不能判断谁移了灵钉，也不能免除姜守带伤违规。",
      "supersedes_fact_ids": [
        "qualification-result"
      ],
      "change": "闻岚对前期复验证据作出正式采信和边界裁定。",
      "source_evidence": "闻岚将材料并拢：“维护签入柜时辰、见证印、钉尾异常、磨痕拖向、三枚灵钉未登记缺口，合并采信。”\n\n苏叶问：“能据此判断谁移了灵钉？”\n\n“不能。”\n\n“能据此免除姜守的带伤违规？”\n\n“不能。”\n\n“那能排除什么？”\n\n“足以排除‘姜守主动改写口令签’这一单一判断。”闻岚道，“维护签先入柜，实物方向后有异常，又存在脱离登记的灵钉。不能越过实物和时辰，只凭一张签定责。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "command-slip-tamperer",
      "state": "knows",
      "belief": "苏叶已正式撤回“姜守主动改写口令签”的误信，承认该判断被共同事故隔离证词单列入淘汰栏。",
      "supersedes_fact_ids": [
        "command-slip-tamperer"
      ],
      "change": "苏叶的 command-slip-tamperer 误信被共同事故隔离证词单正式淘汰。",
      "source_evidence": "苏叶沉默片刻，拿起共同事故隔离证词单，将原判断划入淘汰栏，逐字写下：\n\n“command-slip-tamperer由新事实淘汰。supersedes_fact_ids：maintenance-sign-storage-time、three-nail-unregistered-gap、nail-tail-mismatch、wear-drag-direction。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "jiang-shou-injury-violation-consequence",
      "state": "knows",
      "belief": "苏叶知道姜守未主动改写口令签不等于免除带伤私自校阵，禁令与后果仍不撤。",
      "supersedes_fact_ids": [],
      "change": "苏叶将改签判断与带伤违规后果分栏处理。",
      "source_evidence": "她按下见证印：“我撤回改签判断。但带伤私自校阵是另一项事实，禁令与后果不撤。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "accident-table-verified-boundaries",
      "state": "knows",
      "belief": "赵矩已在事故表补写核验边界：维护签不能单独定责，回声阵牌不能单独定责，三枚定向灵钉未登记缺口成立，姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。",
      "supersedes_fact_ids": [
        "accident-table-boundary"
      ],
      "change": "赵矩被迫在同一事故表内补写已核事实和仍保留的后果。",
      "source_evidence": "第一行：维护签不能单独定责。\n\n第二行：回声阵牌不能单独定责。\n\n第三行：三枚定向灵钉未登记缺口成立。\n\n第四行：姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "outer-rune-test-results",
      "state": "knows",
      "belief": "姜守知道三处外缘调整路径已被停阵试调确认：左三可压回，左四可压回但迟滞，左五仍偏且需另定停阵步骤。",
      "supersedes_fact_ids": [],
      "change": "姜守掌握的修复线索推进为可用于后续分步调整的外缘试调结果。",
      "source_evidence": "闻岚收针。苏叶报下三处刻度，赵矩逐项记表：左三偏向可压回，左四可压回但迟滞，左五仍偏，不得继续。"
    },
    {
      "character_id": "yuan-ke",
      "fact_id": "spirit-nail-borrowing-destination",
      "state": "conceals",
      "belief": "袁客仍未交代三枚定向灵钉的具体归还去向或阵材长期短缺背后的其他关系，只表示回去查。",
      "supersedes_fact_ids": [],
      "change": "袁客的隐瞒状态延续，责任边界未扩展出三枚未登记借走之外。",
      "source_evidence": "袁客脸上的笑淡了些：“我再回去查。”"
    }
  ],
  "thread_changes": [
    {
      "change": "事故调查主线从并列证据推进为闻岚正式采信的组合事实，并排除了姜守主动改写口令签的单一判断。",
      "source_evidence": "“足以排除‘姜守主动改写口令签’这一单一判断。”闻岚道，“维护签先入柜，实物方向后有异常，又存在脱离登记的灵钉。不能越过实物和时辰，只凭一张签定责。”"
    },
    {
      "change": "修复主线获得下一步停阵分步调整许可，但仍不得启动完整乙字训练剑阵或进行完整口令复验。",
      "source_evidence": "闻岚在方案下添注：“外缘灵纹试调完成。准许后续按三处分步调整，不得启动完整乙字训练剑阵，不得进行完整口令复验。”"
    },
    {
      "change": "处分主线未解除：带伤违规责任、裂镜赔偿、阵堂小考资格冻结继续有效。",
      "source_evidence": "第四行：姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。"
    },
    {
      "change": "扣点后果未解除：已扣二点贡献点不退，余额六点。",
      "source_evidence": "赵矩又补：“已扣二点，不退，余额六点。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "姜守把袁客的“大家都是这么周转”拆成不可复验的栏位，迫使闻岚按流程盖下“不具备时辰效力”。",
      "source_evidence": "袁客站在材料架旁，道：“三枚灵钉确实经我手。阵堂缺用，大家都是这么周转。”\n\n姜守以右手点向空栏：“‘大家’，无姓名；‘这么’，无方式；‘周转’，无数量、时辰、归还去向。三项均不可复验。”\n\n闻岚在那句话旁盖下一枚小印：不具备时辰效力。"
    },
    {
      "change": "赵矩试图追问局部校阵偏差责任，反被姜守用工单责任栏位推回；赵矩不愿签总责，只好转入审证。",
      "source_evidence": "赵矩敲了敲纸面：“出了偏差，算谁？”\n\n姜守抽出一张空白工单：“方案错误，填方案人；递送错误，填递送人；放行错误，填监督人。若管事认为不可分，可签总责。”\n\n赵矩把手收了回去：“先审证。”"
    },
    {
      "change": "苏叶签下递工具、读刻度、写见证后仍用木尺让姜守再退半步，延续安全条款式喜剧。",
      "source_evidence": "“工作项三项。”姜守道。\n\n“这是隔离共同事故，不是帮你。”\n\n“名称不影响工时。”\n\n苏叶签完最后一栏，又把木尺横回禁线前：“也不影响你再退半步。”"
    }
  ],
  "new_constraints": [
    {
      "change": "姜守本日不得再导灵；下一次复验只能口述，由苏叶递工具、读刻度、写见证。",
      "source_evidence": "苏叶把工具递送栏移到自己面前，签下姓名：“下一次你只许口述。我递工具、读刻度、写见证。”"
    },
    {
      "change": "后续调整只能按三处分步进行，不得启动完整乙字训练剑阵，不得进行完整口令复验。",
      "source_evidence": "闻岚在方案下添注：“外缘灵纹试调完成。准许后续按三处分步调整，不得启动完整乙字训练剑阵，不得进行完整口令复验。”"
    },
    {
      "change": "左五外缘灵纹仍偏且不得继续试压，后续需从左五开始另定停阵步骤。",
      "source_evidence": "闻岚指向左五那道未能压回的磨痕：“下一次，从它开始。”"
    },
    {
      "change": "姜守已扣二点贡献点不退，余额六点；该扣点后果继续保留。",
      "source_evidence": "赵矩又补：“已扣二点，不退，余额六点。”"
    },
    {
      "change": "姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。",
      "source_evidence": "第四行：姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 未解除；短时低强度导灵观察后今日不得再导灵。",
    "live-array-contact-ban 继续有效；三尺禁线不撤，姜守不得接触运行阵眼，阵眼封条未动。",
    "乙字训练剑阵仍停阵隔离；本章未启动整阵，未恢复口令，未完成最终修复或完整口令复验。",
    "停阵外缘灵纹试调已完成：左三偏向可压回，左四可压回但迟滞，左五仍偏且不得继续。",
    "后续获准按三处分步调整，但不得启动完整乙字训练剑阵，不得进行完整口令复验；下一次从左五开始。",
    "苏叶已正式撤回姜守主动改写口令签的判断，但继续坚持带伤私自校阵、禁令与后果不撤；下一次由她递工具、读刻度、写见证，姜守只许口述。",
    "闻岚已合并采信维护签入柜时辰、见证印、钉尾异常、磨痕拖向、三枚灵钉未登记缺口，足以排除姜守主动改写口令签的单一判断，但不能判断谁移了灵钉，也不能免除带伤违规。",
    "赵矩事故表已补写：维护签不能单独定责，回声阵牌不能单独定责，三枚定向灵钉未登记缺口成立，姜守仍承担带伤违规责任、裂镜赔偿保留、阵堂小考资格继续冻结。",
    "姜守 contribution-point 余额仍为6点，已扣2点不退；calibration-mirror 裂镜赔偿仍保留。",
    "袁客责任边界仍止于三枚 direction-spirit-nail 未登记借走；其他阵材短缺不作推定，归还去向仍未明。"
  ],
  "deviations": []
}
```

## 第 8 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0008",
  "chapter": 8,
  "source_draft": "chapters/0008/draft.final.md",
  "source_sha256": "2f5ee1c2eaa5462bf7610403e75138def9475c289f49dc4381abcc7e85c3e135",
  "entity_changes": [
    {
      "change": "乙字训练剑阵仍处于停阵隔离状态，阵眼封条未动。",
      "source_evidence": "阵眼封条安静贴着，乙字训练剑阵仍在停阵隔离中。"
    },
    {
      "change": "左五外缘灵纹停阵局部试调有效，偏向被压回可接受刻度。",
      "source_evidence": "压扣回退，校针重新落稳。苏叶等了五息，又以铜尺复核两次：“左五偏向压回可接受刻度。两次读数相同。”\n\n她写完时辰、工具、读数和每次停手，又按了见证印。原本所谓隔离共同事故，如今从递钳子到数三息，全落成了她的工时。\n\n闻岚接过见证单，看完才道：“左五，停阵局部试调有效。”"
    },
    {
      "change": "左四外缘灵纹仍有迟滞，起动晚两息，回位晚一息。",
      "source_evidence": "起初针尾不动，过了两息，才慢慢向停剑侧爬了半格。\n\n苏叶立即道：“迟滞仍在。起动晚两息，回位晚一息。”"
    },
    {
      "change": "校准镜仍裂损且无法恢复。",
      "source_evidence": "案桌一角，那面裂开的校准镜仍装在木匣里。裂纹横贯镜面，没有任何恢复的可能。"
    }
  ],
  "relationship_changes": [
    {
      "change": "本章左五调整形成姜守口述、苏叶代操作并见证、闻岚监督采信的协作关系。",
      "source_evidence": "苏叶搬来工具匣，放在禁线外侧：“按共同事故隔离条款，我递工具、读刻度、代移停阵外缘校针、写见证。你只许说。若说话带出动作倾向，我有权让你后退。”"
    },
    {
      "change": "赵矩被闻岚要求在事故表中补写已核事实，不能只以未修复压掉左五局部有效记录。",
      "source_evidence": "闻岚将见证单压在事故表上：“事故表记录事故，也记录复核。补写。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "injury",
      "change": "left-palm-burn 仍未解除，左掌仍有刺痛。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守把缠着药布的左掌背到身后。掌心阵火灼痕仍一阵阵发刺，手指稍一蜷便牵着痛，并无解除的迹象。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效：姜守不得导灵、不得越线、不得触碰运行阵眼。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守刚抬眼，闻岚又道：“你不得导灵，不得越线，不得触碰运行阵眼。今日不得再导灵，仍然有效。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "no-more-guiding-today 继续有效，姜守今日不得再导灵。",
      "state_id": "no-more-guiding-today",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "姜守刚抬眼，闻岚又道：“你不得导灵，不得越线，不得触碰运行阵眼。今日不得再导灵，仍然有效。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "wen-lan",
      "fact_id": "left-five-local-adjustment-effective",
      "state": "knows",
      "belief": "闻岚确认左五停阵局部试调有效。",
      "supersedes_fact_ids": [],
      "change": "闻岚采信苏叶见证单后，确认左五停阵局部试调有效。",
      "source_evidence": "闻岚接过见证单，看完才道：“左五，停阵局部试调有效。”"
    },
    {
      "character_id": "su-ye",
      "fact_id": "left-five-local-adjustment-effective",
      "state": "knows",
      "belief": "苏叶知道左五偏向已压回可接受刻度，且由她代操作、姜守仅口述。",
      "supersedes_fact_ids": [],
      "change": "苏叶通过亲自读数和代操作，知道左五偏向压回可接受刻度。",
      "source_evidence": "压扣回退，校针重新落稳。苏叶等了五息，又以铜尺复核两次：“左五偏向压回可接受刻度。两次读数相同。”"
    },
    {
      "character_id": "jiang-shou",
      "fact_id": "left-four-lag-persists",
      "state": "knows",
      "belief": "姜守知道左四能压回但响应拖后，直接完整口令复验仍可能导致停剑侧慢。",
      "supersedes_fact_ids": [],
      "change": "姜守确认左四迟滞仍会影响完整口令复验。",
      "source_evidence": "姜守盯着针尾：“左四能压回，但响应拖后。若直接做完整口令复验，停剑侧仍可能慢。”"
    },
    {
      "character_id": "wen-lan",
      "fact_id": "left-four-lag-persists",
      "state": "knows",
      "belief": "闻岚知道左四迟滞未清，因此不得启动整阵或完整口令复验，只能先拟停阵口令模拟方案并先处理左四。",
      "supersedes_fact_ids": [],
      "change": "闻岚据左四迟滞作出下一步流程裁定。",
      "source_evidence": "闻岚抬手截断争执：“左四迟滞未清，不得启动整阵，不得进行完整口令复验。准许拟停阵口令模拟方案，但方案必须先处理左四。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "accident-form-chapter-0008-updates",
      "state": "knows",
      "belief": "赵矩事故表已补入左五局部试调有效、左四仍迟滞、姜守本次未越三尺禁线、未导灵、未触碰运行阵眼。",
      "supersedes_fact_ids": [],
      "change": "赵矩被要求并实际补写本章三类已核事实。",
      "source_evidence": "赵矩沉默片刻，提笔逐项补入。苏叶核对后，在见证处签下名字，又将今日操作工时一并写明。"
    }
  ],
  "thread_changes": [
    {
      "change": "主线从左五异常钉位推进到左五停阵局部试调有效，但尚未完成修复。",
      "source_evidence": "赵矩皱眉：“什么三栏？”\n\n“未完成修复，是结果栏。左五局部试调有效，是已核栏。左四仍迟滞，是未决栏。混写会把有效步骤一并抹掉，下次还得重做。”"
    },
    {
      "change": "完整口令复验被闻岚禁止，下一步只能拟停阵口令模拟方案，且必须先处理左四迟滞。",
      "source_evidence": "闻岚抬手截断争执：“左四迟滞未清，不得启动整阵，不得进行完整口令复验。准许拟停阵口令模拟方案，但方案必须先处理左四。”"
    },
    {
      "change": "阵堂小考资格继续冻结，裂镜赔偿和已扣贡献点后果保留。",
      "source_evidence": "闻岚收起事故表：“资格继续冻结。裂镜赔偿保留，扣除的两点贡献不退。左掌伤势未解除，禁线不撤，今日不得再导灵。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "姜守习惯性把操作说成自己动手，被苏叶按安全条款要求后退并改口，形成口述维修笑点。",
      "source_evidence": "“校针向左压回半分，我——”\n\n“停。”苏叶立刻直起身，“伤员出现代操作措辞。按条款，后退一步，改口。”"
    },
    {
      "change": "苏叶把协作隔离条款细化成递工具、读刻度、代操作、写见证的实际工时，安全限制反而成为有效流程。",
      "source_evidence": "她写完时辰、工具、读数和每次停手，又按了见证印。原本所谓隔离共同事故，如今从递钳子到数三息，全落成了她的工时。"
    },
    {
      "change": "姜守将一句未完成拆成结果栏、已核栏、未决栏，用事故表格式反制赵矩压缩流程。",
      "source_evidence": "赵矩皱眉：“什么三栏？”\n\n“未完成修复，是结果栏。左五局部试调有效，是已核栏。左四仍迟滞，是未决栏。混写会把有效步骤一并抹掉，下次还得重做。”"
    }
  ],
  "new_constraints": [
    {
      "change": "左四迟滞未清前，不得启动整阵，不得完整口令复验；停阵口令模拟方案必须先处理左四。",
      "source_evidence": "闻岚抬手截断争执：“左四迟滞未清，不得启动整阵，不得进行完整口令复验。准许拟停阵口令模拟方案，但方案必须先处理左四。”"
    },
    {
      "change": "姜守在左五调整中只能口述，若话语带出动作倾向，苏叶可要求他后退。",
      "source_evidence": "苏叶搬来工具匣，放在禁线外侧：“按共同事故隔离条款，我递工具、读刻度、代移停阵外缘校针、写见证。你只许说。若说话带出动作倾向，我有权让你后退。”"
    },
    {
      "change": "事故表新增并固定记录姜守本次未越三尺禁线、未导灵、未触碰运行阵眼。",
      "source_evidence": "“左四仍迟滞。姜守本次未越三尺禁线，未导灵，未触碰运行阵眼。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 未解除。",
    "live-array-contact-ban 继续有效：三尺禁线不撤，姜守不得导灵、不得越线、不得触碰运行阵眼。",
    "no-more-guiding-today 继续有效，姜守今日不得再导灵。",
    "乙字训练剑阵仍停阵隔离，阵眼封条未动，未启动整阵，未完成最终修复，未进行完整口令复验。",
    "左五外缘灵纹已在停阵监督、苏叶代操作、姜守口述核对下压回可接受刻度，记为停阵局部试调有效。",
    "左四迟滞仍存在，表现为起动晚两息、回位晚一息；下一步必须先处理左四迟滞。",
    "闻岚裁定下一步只能先写左四迟滞处理，再写停阵口令模拟方案，不得直接启动整阵或完整复验。",
    "苏叶继续具备共同事故隔离见证身份，实际承担递工具、读刻度、代操作、写见证和核对工时。",
    "赵矩事故表已补入左五局部试调有效、左四仍迟滞、姜守未越线未导灵未触碰运行阵眼；阵堂小考资格仍冻结。",
    "calibration-mirror 仍裂损且无恢复可能，裂镜赔偿保留。",
    "姜守 contribution-point 余额仍为6点，已扣2点不退。",
    "袁客责任边界本章未扩展；三枚 direction-spirit-nail 未登记借走之外无新增实锤。"
  ],
  "deviations": []
}
```

## 第 9 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0009",
  "chapter": 9,
  "source_draft": "chapters/0009/draft.final.md",
  "source_sha256": "5a63d46d54e11cdcd033a9f014d9d8fcdae83c179269063e51bbabe3ddd17305",
  "entity_changes": [
    {
      "change": "乙字训练剑阵左四迟滞已压入停阵模拟范围，但仅代表可模拟，仍待正式停阵复验确认。",
      "source_evidence": "闻岚俯身看过钉尾与刻线：“迟滞压入模拟范围。只代表可模拟。”\n\n姜守在方案上补写：“左四，待正式停阵复验确认。”"
    },
    {
      "change": "停阵口令模拟方案获闻岚批准，范围限定为外缘灵纹空载、左四单点复位、回声阵牌复述、不接内环，且不是完整复验。",
      "source_evidence": "姜守站在三尺禁线外，右手提笔：“剩余步骤：外缘灵纹空载响应，左四单点复位，回声阵牌复述，不接内环。”\n\n苏叶补了一句：“模拟不许追人。”\n\n姜守把这句写进首栏。\n\n闻岚看了她一眼：“不是口号。写成条件。”\n\n苏叶接过笔，在下方添道：“木剑匣封条不动；内环断灵；外缘刻线只走空载；任何一处越过停手刻度，立即复位。”\n\n“准。”闻岚在方案末尾落印，“只准这些。不是完整复验。”"
    },
    {
      "change": "回声阵牌在本次停阵模拟中只复述完整口令“后退三步，停剑”，未提供责任人、时辰或下令人信息。",
      "source_evidence": "苏叶确认所有人都退在红绳外，才轻触回声阵牌边缘的复述纹。阵牌泛起一层灰白微光，平直地响道：\n\n“后退三步，停剑。”\n\n没有人名，没有时辰，也没有下令人。"
    },
    {
      "change": "停阵空载响应成立，原先“追后三步”错误偏向未出现，但不能替代正式停阵复验。",
      "source_evidence": "赵矩还要改字，闻岚已用指节点了点刻线：“空载响应成立，错误偏向未出现。写有效。另注：不能替代正式停阵复验。”"
    },
    {
      "change": "事故表已叠入停阵模拟附页、苏叶见证单和左三左四左五试调记录，作为明日正式停阵复验材料。",
      "source_evidence": "她将停阵模拟附页、苏叶见证单和左三左四左五试调记录叠在一起，压到事故表下。\n\n“明日正式停阵复验。同时复查伤势。复验前，禁线不撤，阵眼不得接触，整阵不得启动。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "苏叶继续作为共同事故隔离见证人实际约束姜守口述流程，并把停手、读数、复位写成有效见证。",
      "source_evidence": "她记完“停手、读数、复位”，才抬起校针：“可以继续口述。”"
    },
    {
      "change": "赵矩受闻岚裁定和事故表格式约束，被迫承认未启动整阵符合本次方案，并记录模拟有效。",
      "source_evidence": "赵矩提笔，在第一栏写下“未启动完整剑阵，符合本次方案”。"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "recovery",
      "change": "left-palm-burn 部分恢复：刺痛减轻，但导灵抖动风险仍在，伤势未解除。",
      "state_id": "left-palm-burn",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "闻岚按过伤痕边缘，姜守手指轻轻一抖。她收手道：“left-palm-burn记部分恢复。刺痛减轻，导灵抖动风险仍在。未解除。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "live-array-contact-ban 继续有效至下次巡验确认；姜守资格继续冻结。",
      "state_id": "live-array-contact-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "赵矩随即补入事故表：“live-array-contact-ban继续有效，至下次巡验确认。资格继续冻结。裂镜赔偿保留，带伤校阵处分保留，贡献点余额六点，已扣二点不退。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "jiang-shou",
      "fact_id": "spirit-nail-borrowing-destination",
      "state": "investigating",
      "belief": "袁客三枚定向灵钉未登记借走已核定，但归还去向与时辰仍为空或待查；未确认就应写未确认。",
      "supersedes_fact_ids": [
        "remaining-evidence-chain"
      ],
      "change": "姜守将袁客补充说明的追问范围压缩为三枚定向灵钉的时辰与去向，仍未获得有效答案。",
      "source_evidence": "姜守把纸转正，点了三处：“数量，三枚，已填。时辰，空。去向，空。你只补后两处。”\n\n“若是经他人转手——”\n\n“写你最后确认的时辰与去向。未确认就写未确认。”"
    },
    {
      "character_id": "yuan-ke",
      "fact_id": "spirit-nail-borrowing-destination",
      "state": "conceals",
      "belief": "袁客仍未交代三枚定向灵钉的具体归还时辰与去向，只留下待查。",
      "supersedes_fact_ids": [],
      "change": "袁客对三枚定向灵钉的归还去向与时辰继续未给出实质说明。",
      "source_evidence": "袁客握笔片刻，终究只写下“待查”，没有添出别的责任。"
    },
    {
      "character_id": "wen-lan",
      "fact_id": "spirit-nail-liability-boundary",
      "state": "knows",
      "belief": "当前只核三枚定向灵钉未登记借走，其他阵材短缺不作推定。",
      "supersedes_fact_ids": [],
      "change": "闻岚明确袁客责任边界不得扩展到其他短缺推定。",
      "source_evidence": "闻岚收走说明：“只核三枚未登记借走。其他短缺，不作推定。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "simulation-valid-but-not-qualification",
      "state": "knows",
      "belief": "停阵模拟有效且未启动完整剑阵符合方案，但阵堂小考资格仍冻结待验。",
      "supersedes_fact_ids": [],
      "change": "赵矩在事故表上承认停阵模拟的合规与有效，同时维持资格冻结。",
      "source_evidence": "赵矩只能照写，末了在资格栏仍盖上“冻结待验”。"
    }
  ],
  "thread_changes": [
    {
      "change": "正式停阵复验被推进到明日进行，并将同时复查姜守左掌伤势。",
      "source_evidence": "“明日正式停阵复验。同时复查伤势。复验前，禁线不撤，阵眼不得接触，整阵不得启动。”"
    },
    {
      "change": "阵堂小考资格线仍未放行，保持冻结待验状态。",
      "source_evidence": "赵矩只能照写，末了在资格栏仍盖上“冻结待验”。"
    },
    {
      "change": "袁客线只推进到三枚定向灵钉归还去向与时辰待查，未扩展到阵材长期短缺责任。",
      "source_evidence": "闻岚收走说明：“只核三枚未登记借走。其他短缺，不作推定。”"
    },
    {
      "change": "裂损校准镜仍在木匣中且赔偿签未撤，赔偿责任继续保留。",
      "source_evidence": "左四钉位旁摆着校针、木尺和一张新见证单。裂开的校准镜仍装在木匣里，匣角挂着赔偿签，没人动它。"
    }
  ],
  "comedy_changes": [
    {
      "change": "“模拟不许追人”从苏叶的口号被闻岚要求写成正式方案条件。",
      "source_evidence": "苏叶补了一句：“模拟不许追人。”\n\n姜守把这句写进首栏。\n\n闻岚看了她一眼：“不是口号。写成条件。”"
    },
    {
      "change": "苏叶把“停手”扩展成“停口”，使姜守连口述都被纳入见证流程。",
      "source_evidence": "她写下读数，随即道：“停手。”\n\n姜守本来已经开口：“下一步——”\n\n“停手也包括停口。”苏叶指了指见证单，“否则我无法证明读数是在你改令之前还是之后。”"
    },
    {
      "change": "赵矩想以未启动整阵否定测试价值，却被拆成合规栏和空载响应栏，反成记录依据。",
      "source_evidence": "赵矩皱眉：“既不启动整阵，如何算放行测试？”\n\n姜守把一张空白附页推过去：“分两栏。第一栏，未启动整阵是否合规。第二栏，空载响应是否可记。”\n\n“我问的是放行。”\n\n“本章没有放行栏。”"
    },
    {
      "change": "苏叶每读一项就喊一次停手，三次停手都变成有效见证。",
      "source_evidence": "她每读一项，便喊一次“停手”，记一项复位。三次停手都被写成有效见证。"
    }
  ],
  "new_constraints": [
    {
      "change": "停阵模拟方案限制为木剑匣封条不动、内环断灵、外缘刻线只走空载，任何越过停手刻度立即复位。",
      "source_evidence": "苏叶接过笔，在下方添道：“木剑匣封条不动；内环断灵；外缘刻线只走空载；任何一处越过停手刻度，立即复位。”"
    },
    {
      "change": "正式复验前禁线不撤，姜守不得接触阵眼，整阵不得启动。",
      "source_evidence": "“明日正式停阵复验。同时复查伤势。复验前，禁线不撤，阵眼不得接触，整阵不得启动。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 部分恢复但未解除：刺痛减轻，导灵抖动风险仍在。",
    "live-array-contact-ban 继续有效至下次巡验确认；复验前禁线不撤，姜守不得接触阵眼，整阵不得启动。",
    "乙字训练剑阵仍未完成正式停阵复验；本章停阵模拟有效，但不能替代正式停阵复验。",
    "左三、左五停于正线，左四迟半息但停于正线，追后侧无亮纹；左四迟滞已压入模拟范围，待正式停阵复验确认。",
    "回声阵牌本章只复述“后退三步，停剑”，没有人名、时辰或下令人。",
    "事故表下已有停阵模拟附页、苏叶见证单和左三左四左五试调记录；明日正式停阵复验并同时复查伤势。",
    "阵堂小考资格仍冻结待验，尚未改为带条件准入。",
    "calibration-mirror 仍裂损，赔偿签仍在；裂镜赔偿保留。",
    "姜守 contribution-point 余额仍为6点，已扣2点不退；带伤校阵处分保留。",
    "袁客只留下三枚定向灵钉归还去向与时辰“待查”；责任边界只核三枚未登记借走，其他短缺不作推定。"
  ],
  "deviations": []
}
```

## 第 10 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0010",
  "chapter": 10,
  "source_draft": "chapters/0010/draft.final.md",
  "source_sha256": "cbb4aa5f7fb4b6c673c95367e465a0bee9600dea6d732c01a3444cb858ec7797",
  "entity_changes": [
    {
      "change": "乙字训练剑阵停阵复验有效，口令响应恢复正常，且未启动整阵。",
      "source_evidence": "闻岚收回牵引尺：“停阵复验有效。口令响应恢复正常。未启动整阵。”"
    },
    {
      "change": "姜守的阵堂小考资格由冻结改为带条件准入。",
      "source_evidence": "最后，他把资格栏的“冻结”划去，改为“带条件准入”，盖下管事印。"
    },
    {
      "change": "校准镜仍裂损且不可恢复，编号被抄入赔偿排期。",
      "source_evidence": "赵矩将裂损的校准镜编号抄入赔偿排期，镜面裂纹仍横贯正中，没有任何恢复的余地。"
    }
  ],
  "relationship_changes": [
    {
      "change": "苏叶不再认为姜守主动改写口令签，但仍区分并保留姜守带伤校阵责任。",
      "source_evidence": "她搁笔道：“维护签拓印、磨损拖向、三枚定向灵钉缺口与回声阵牌能力边界相互核验，已排除姜守主动改写口令签的单一判断。带伤校阵是另一项，不随此判断撤销。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "jiang-shou",
      "kind": "recovery",
      "change": "姜守左掌阵火灼伤经停用运行阵眼、灼伤膏、稳定吐纳与现场巡验确认后解除。",
      "state_id": "left-palm-burn",
      "state_action": "resolve",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "她逐项核对：“连续停用运行阵眼，有记录。灼伤膏已用尽，有领用与消耗记录。稳定吐纳七次，有见证。现场巡验无刺痛、无导灵抖动、无灵纹失稳。”\n\n闻岚在验伤单上写下同一行标记：left-palm-burn，解除。"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "姜守因左掌伤势解除，live-array-contact-ban 失效。",
      "state_id": "live-array-contact-ban",
      "state_action": "resolve",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“live-array-contact-ban随伤势解除失效。”"
    },
    {
      "subject_id": "jiang-shou",
      "kind": "restriction",
      "change": "姜守新增两日内不得独立启动完整剑阵的限制；期间只能在监督下参与停阵或局部低强度校阵。",
      "state_id": "two-day-complete-array-independent-start-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "闻岚点头：“两日内不得独立启动完整剑阵。只能在监督下参与停阵，或局部低强度校阵。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "wen-lan",
      "fact_id": "echo-command-plate-limits",
      "state": "knows",
      "belief": "闻岚确认回声阵牌只能证明收到过完整口令，不能证明责任人、时辰，也不能单独定责。",
      "supersedes_fact_ids": [],
      "change": "闻岚正式限定回声阵牌证据效力。",
      "source_evidence": "“只能证明它收到过完整口令。”闻岚道，“不证人，不证时辰，不单独定责。”"
    },
    {
      "character_id": "zhao-ju",
      "fact_id": "array-command-error-cause",
      "state": "knows",
      "belief": "赵矩在事故表内承认维护签不能单独定责、三枚定向灵钉未登记缺口成立、姜守主动改写口令签的单一判断已被排除，同时姜守带伤违规责任继续保留。",
      "supersedes_fact_ids": [
        "jiang-shou-liability"
      ],
      "change": "赵矩被事故表约束，必须承认已核事实并保留姜守另一项违规责任。",
      "source_evidence": "赵矩只能在事故表内承认：维护签不能单独定责；三枚定向灵钉未登记缺口成立；姜守主动改写口令签的单一判断已被排除；姜守带伤违规责任继续保留。"
    },
    {
      "character_id": "su-ye",
      "fact_id": "array-command-error-cause",
      "state": "knows",
      "belief": "苏叶已淘汰姜守主动改写口令签的单一判断，不再相信姜守是该项口令签篡改者；她仍认为带伤校阵是另一项责任。",
      "supersedes_fact_ids": [
        "command-slip-tamperer"
      ],
      "change": "苏叶在见证单中正式将 command-slip-tamperer 原判断淘汰。",
      "source_evidence": "苏叶同时展开自己的见证单，在“原判断变更”一栏写道：“command-slip-tamperer，淘汰。”"
    },
    {
      "character_id": "wen-lan",
      "fact_id": "spirit-nail-liability-boundary",
      "state": "knows",
      "belief": "闻岚只确认袁客三枚定向灵钉未登记借走，归还去向与时辰未明，其余短缺不作推定。",
      "supersedes_fact_ids": [],
      "change": "闻岚将袁客责任边界限定在三枚未登记借走，未扩展为长期短缺定责。",
      "source_evidence": "闻岚扫过纸面：“只记三枚未登记借走。去向与时辰未明。其余不作推定。”"
    },
    {
      "character_id": "yuan-ke",
      "fact_id": "spirit-nail-borrowing-destination",
      "state": "conceals",
      "belief": "袁客承认三枚灵钉临时周转，但仍未交代清楚归还去向，并试图提及库中其余短缺。",
      "supersedes_fact_ids": [],
      "change": "袁客继续未说明三枚定向灵钉的具体归还去向。",
      "source_evidence": "门外的袁客这时递来一张说明：“三枚灵钉确是临时周转，归还去向还需再核。至于库中其余短缺——”"
    }
  ],
  "thread_changes": [
    {
      "change": "乙字训练剑阵口令错位修复线完成正式停阵复验，结果为后退三步后停剑，无追加追行。",
      "source_evidence": "三步。\n\n木剑剑尖越过第三道刻线，齐齐停住。追后侧那道曾经多亮一截的灵纹安静无光，三柄木剑也没有再向前追出半寸。"
    },
    {
      "change": "姜守资格线从冻结推进为带条件准入，同时裂镜赔偿、带伤处分和两日禁启保留为后续压力。",
      "source_evidence": "闻岚在旁签押：“乙字训练剑阵停阵复验通过。口令恢复正常。姜守准予参加阵堂小考。裂镜赔偿、带伤校阵处分保留；两日内不得独立启动完整剑阵。”"
    },
    {
      "change": "贡献点扣罚结果维持不变：已扣二点，余额六点，不退还。",
      "source_evidence": "贡献栏也照旧写着：已扣二点，余额六点，不退还。"
    },
    {
      "change": "裂镜赔偿排期的下一步签认时间落到明日辰时。",
      "source_evidence": "她吹干墨迹，把小考前置事项单推到姜守面前。最上方第一行写着：裂镜赔偿排期，明日辰时签认。"
    }
  ],
  "comedy_changes": [
    {
      "change": "赵矩想先压责任，结果被姜守把话拆成监督、记录、递送读数见证和停手口令四项工单，反把记录责任落到赵矩头上。",
      "source_evidence": "赵矩看了一眼自己方才提出的“先写责任”，那句话已被拆成四项差事，其中记录一项正落在他头上。他把事故表铺开：“先验。但冻结栏不动。”"
    },
    {
      "change": "苏叶用安全条款把姜守的后退和口述距离都写成合规见证。",
      "source_evidence": "苏叶已经把工具盘抱走：“按停阵复验安全条款，你再后退半步。口述时不得探身，不得抬手越线，不得用灵气比画。”\n\n姜守退了半步：“已后退。”\n\n“再说一句。”\n\n“为何？”\n\n“证明你退后还能口述。”\n\n“距离合格，口述正常。”\n\n苏叶在见证单上落笔：“禁线外四尺，声音可达。无需靠近。”"
    },
    {
      "change": "赵矩试图用裂镜和处分继续压资格，姜守把这些后果拆成条件准入栏，反让后果成为准入表格内容。",
      "source_evidence": "赵矩原想用两项后果压住资格，如今两项后果都被钉进了准入条件。他翻回事故表，逐栏核对，最后仍得按既定流程落笔。"
    }
  ],
  "new_constraints": [
    {
      "change": "姜守两日内不得独立启动完整剑阵，只能在监督下参与停阵或局部低强度校阵。",
      "source_evidence": "闻岚点头：“两日内不得独立启动完整剑阵。只能在监督下参与停阵，或局部低强度校阵。”"
    },
    {
      "change": "姜守带条件准入阵堂小考的条件包括校准镜赔偿排期、两日禁独立启动整阵、带伤校阵处分记录保留、只能监督下参与停阵或局部低强度校阵。",
      "source_evidence": "姜守把一张空白附页推过去：“不写直接解冻。写条件准入。第一，校准镜裂损不能恢复，列赔偿排期。第二，两日内禁独立启动整阵。第三，带伤校阵处分记录保留。第四，监督下参与停阵或局部低强度校阵。四栏齐全，再判能否小考。”"
    },
    {
      "change": "苏叶作为共同事故隔离见证人承担后续核对工时。",
      "source_evidence": "苏叶在见证单末尾补了一行：“后续核对工时，由共同事故隔离见证人承担。”"
    }
  ],
  "resolved_constraints": [
    {
      "change": "姜守的 live-array-contact-ban 随 left-palm-burn 解除而失效。",
      "source_evidence": "“live-array-contact-ban随伤势解除失效。”"
    }
  ],
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 已解除。",
    "live-array-contact-ban 已失效，但姜守新增 two-day-complete-array-independent-start-ban：两日内不得独立启动完整剑阵，只能在监督下参与停阵或局部低强度校阵。",
    "乙字训练剑阵停阵复验通过，口令恢复正常；“后退三步，停剑”已验证为后退三步后停剑，无追加追行。",
    "姜守阵堂小考资格已由冻结改为带条件准入。",
    "小考条件包括裂镜赔偿排期、两日禁独立启动整阵、带伤校阵处分记录保留、监督下参与停阵或局部低强度校阵。",
    "校准镜仍裂损且不能恢复，裂镜赔偿排期需明日辰时签认。",
    "姜守 contribution-point 余额仍为6点，已扣2点不退还。",
    "苏叶已淘汰姜守主动改写口令签的单一判断，但仍会用安全条款约束姜守操作，并承担后续核对工时。",
    "赵矩已在事故表内承认维护签不能单独定责、三枚定向灵钉未登记缺口成立、姜守主动改写口令签的单一判断已被排除，同时保留姜守带伤违规责任。",
    "袁客只被确认三枚 direction-spirit-nail 未登记借走，归还去向与时辰未明；其余阵材短缺不作推定。"
  ],
  "deviations": []
}
```

## 最终结构化快照

```json
{
  "after_chapter": 10,
  "event_ids": [
    "chapter-0001",
    "chapter-0002",
    "chapter-0003",
    "chapter-0004",
    "chapter-0005",
    "chapter-0006",
    "chapter-0007",
    "chapter-0008",
    "chapter-0009",
    "chapter-0010"
  ],
  "changes": {
    "entity_changes": [
      {
        "change": "乙字训练剑阵在演练中将“后退三步，停剑”执行为继续追击并造成候选人右肩受伤。",
        "source_evidence": "候选人进两步，侧身避过第一剑，随即依照演练册喊道：“后退三步，停剑！”\n\n木剑本该在他退满三步时垂落。\n\n第一步落下，十二柄木剑却齐齐向前。\n\n第二步，剑阵追近半尺。\n\n第三步，候选人刚要停，最前一柄木剑猛地多窜出一段，拍中他的右肩。他踉跄半步，背后两柄木剑又接连撞来，将他打出白线。"
      },
      {
        "change": "乙字训练剑阵因事故被临时停用并封场隔离。",
        "source_evidence": "“先封场。”赵矩已经起身，“候选人送药堂验伤，乙字剑阵临时停用！”"
      },
      {
        "change": "候选人的右肩木剑击伤已被姜守写入旁录，候选人停止演练并送药堂验看。",
        "source_evidence": "候选人被扶出场时回头看了一眼。姜守将“右肩木剑击伤，停止演练，送药堂验看”写进旁录，随后看着杂役在场地四角插下停用牌。"
      },
      {
        "change": "乙字训练剑阵在现场复核中错误多放第二轮木剑，仍未修复并继续停用。",
        "source_evidence": "备用剑架随之弹响。第二轮木剑竟被错位口令牵动，接连射出。第一柄钉入木靶，第二柄擦断红绳，第三柄正中偏斜的校准镜。"
      },
      {
        "change": "calibration-mirror 裂损，登记为不可现场修复且必须计赔。",
        "source_evidence": "裂镜被封条固定，登记牌上添了“不可现场修复、必须计赔”八字。"
      },
      {
        "change": "事故表已正式记录维护签拓印的证明范围、现场复核失败、姜守带伤违规接触运行阵眼、乙字训练剑阵多放一轮木剑、校准镜裂损与资格冻结。",
        "source_evidence": "赵矩回到案前，逐栏落笔：“现场复核失败。姜守，炼气二层，阵火灼伤未解除，违反禁令，带伤接触运行阵眼。后果：乙字训练剑阵多放一轮木剑，校准镜裂损。”"
      },
      {
        "change": "新增“共同事故隔离证词单”，由姜守记录并由苏叶签写复测前口令、复测时木剑多追一段、校准镜被击裂及其保留判断。",
        "source_evidence": "苏叶终于拿笔，重重写下：“复测前口令为‘后退三步，停剑’。复测时木剑多追一段，校准镜被击裂。本人仍保留姜守改写口令签之判断。”"
      },
      {
        "change": "事故表新增回声阵牌证据边界：只能证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。",
        "source_evidence": "赵矩这才在未核验栏后补写：“回声阵牌仅证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。”"
      },
      {
        "change": "事故表新增已核记录：维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。",
        "source_evidence": "他终究写下：“维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。”"
      },
      {
        "change": "事故表新增三枚定向灵钉账面与现场登记不合、无对应领用登记且需核验的记录。",
        "source_evidence": "赵矩夺笔落字：“三枚定向灵钉账面与现场登记不合，无对应领用登记，需核验。”"
      },
      {
        "change": "袁客留下口头记录：临时拿过几枚定向灵钉周转，但未填明数量、时辰、归还去向。",
        "source_evidence": "请管事写：三枚定向灵钉缺口需继续核验；袁客口称临时拿过几枚周转，未填数量、时辰、归还去向。”"
      },
      {
        "change": "苏叶的证词单新增见证内容：三枚缺口客观存在，袁客口称临时拿过几枚但未明数量及时辰。",
        "source_evidence": "苏叶看着单子，又看自己的证词单，咬唇添字：“本人见证阵务柜领用簿与乙字现场登记相差三枚，未见对应领用登记。袁客口称临时拿过几枚定向灵钉周转，未明数量及时辰。”"
      },
      {
        "change": "乙字训练剑阵停阵材料台现场登记的九枚定向灵钉完成外观比对，其中左三、左四、左五三处相邻钉位的现钉尾朝向与旧压痕不一致。",
        "source_evidence": "“左三、左四、左五。”姜守短声道，“三处相邻。现钉尾与旧压痕不合。”"
      },
      {
        "change": "乙字训练剑阵三处异常钉位的灵纹磨痕被记录为拖向“追后三步”执行侧。",
        "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
      },
      {
        "change": "共同事故隔离证词新增苏叶全程代放纸框、读尺距、签注见证的现场记录，并确认姜守未越线、未触碰阵眼及阵材。",
        "source_evidence": "苏叶接过笔，认真签下姓名，又在旁边补了一句：全程停阵，姜守未越线、未触碰阵眼及阵材。"
      },
      {
        "change": "事故表新增并列核验页：维护签拓印、原签入柜时辰、柜房见证印、三处钉尾异常、灵纹磨痕方向被放入同一核验链，且维护签不能单独定责。",
        "source_evidence": "赵矩这才落笔：维护签拓印与原签入柜时辰、柜房见证印核验无误；入柜时辰早于部分定向灵钉方向异常记录；维护签不得单独作为口令错位定责依据，须与灵纹磨痕、灵钉领用及现场时辰合并核验。"
      },
      {
        "change": "袁客未登记借走三枚 direction-spirit-nail 的责任边界成立；具体归还去向未明，且不扩展推定其他阵材短缺责任。",
        "source_evidence": "赵矩随即加盖核验印，在事故表新增页写明：三枚定向灵钉由袁客经手未登记借走成立，具体归还去向未明；本项仅核至三枚缺口，不据此推定其他阵材短缺责任。"
      },
      {
        "change": "事故表最终合并记录：袁客三枚定向灵钉未登记借走成立；维护签不能单独定责；姜守原有带伤违规、裂镜赔偿、扣点和资格冻结仍执行。",
        "source_evidence": "赵矩将两页合并誊写：“三枚定向灵钉未登记借走成立。维护签不能单独定责。姜守带伤校阵违规、裂镜赔偿、扣除二点贡献及资格冻结，仍照原栏执行。”"
      },
      {
        "change": "乙字训练剑阵仍处于停阵隔离状态，本章只完成三处外缘灵纹试调，未启动整阵、未恢复口令，左五尚需另定停阵步骤。",
        "source_evidence": "这次试调没有启动整阵，也没有恢复口令，只确认三处外缘调整路径可行，其中左五尚需另定停阵步骤。"
      },
      {
        "change": "三处异常钉位外缘试调结果确定：左三偏向可压回，左四可压回但迟滞，左五仍偏且不得继续。",
        "source_evidence": "闻岚收针。苏叶报下三处刻度，赵矩逐项记表：左三偏向可压回，左四可压回但迟滞，左五仍偏，不得继续。"
      },
      {
        "change": "后续停阵调整获得许可，但范围仍限三处分步调整，禁止启动完整乙字训练剑阵和完整口令复验。",
        "source_evidence": "闻岚在方案下添注：“外缘灵纹试调完成。准许后续按三处分步调整，不得启动完整乙字训练剑阵，不得进行完整口令复验。”"
      },
      {
        "change": "袁客本章责任边界仍止于三枚定向灵钉未登记借走，其他阵材短缺不作推定。",
        "source_evidence": "“今日责任止于已核部分。”闻岚道，“三枚，未登记借走。其他阵材短缺不作推定。”"
      },
      {
        "change": "乙字训练剑阵仍处于停阵隔离状态，阵眼封条未动。",
        "source_evidence": "阵眼封条安静贴着，乙字训练剑阵仍在停阵隔离中。"
      },
      {
        "change": "左五外缘灵纹停阵局部试调有效，偏向被压回可接受刻度。",
        "source_evidence": "压扣回退，校针重新落稳。苏叶等了五息，又以铜尺复核两次：“左五偏向压回可接受刻度。两次读数相同。”\n\n她写完时辰、工具、读数和每次停手，又按了见证印。原本所谓隔离共同事故，如今从递钳子到数三息，全落成了她的工时。\n\n闻岚接过见证单，看完才道：“左五，停阵局部试调有效。”"
      },
      {
        "change": "左四外缘灵纹仍有迟滞，起动晚两息，回位晚一息。",
        "source_evidence": "起初针尾不动，过了两息，才慢慢向停剑侧爬了半格。\n\n苏叶立即道：“迟滞仍在。起动晚两息，回位晚一息。”"
      },
      {
        "change": "校准镜仍裂损且无法恢复。",
        "source_evidence": "案桌一角，那面裂开的校准镜仍装在木匣里。裂纹横贯镜面，没有任何恢复的可能。"
      },
      {
        "change": "乙字训练剑阵左四迟滞已压入停阵模拟范围，但仅代表可模拟，仍待正式停阵复验确认。",
        "source_evidence": "闻岚俯身看过钉尾与刻线：“迟滞压入模拟范围。只代表可模拟。”\n\n姜守在方案上补写：“左四，待正式停阵复验确认。”"
      },
      {
        "change": "停阵口令模拟方案获闻岚批准，范围限定为外缘灵纹空载、左四单点复位、回声阵牌复述、不接内环，且不是完整复验。",
        "source_evidence": "姜守站在三尺禁线外，右手提笔：“剩余步骤：外缘灵纹空载响应，左四单点复位，回声阵牌复述，不接内环。”\n\n苏叶补了一句：“模拟不许追人。”\n\n姜守把这句写进首栏。\n\n闻岚看了她一眼：“不是口号。写成条件。”\n\n苏叶接过笔，在下方添道：“木剑匣封条不动；内环断灵；外缘刻线只走空载；任何一处越过停手刻度，立即复位。”\n\n“准。”闻岚在方案末尾落印，“只准这些。不是完整复验。”"
      },
      {
        "change": "回声阵牌在本次停阵模拟中只复述完整口令“后退三步，停剑”，未提供责任人、时辰或下令人信息。",
        "source_evidence": "苏叶确认所有人都退在红绳外，才轻触回声阵牌边缘的复述纹。阵牌泛起一层灰白微光，平直地响道：\n\n“后退三步，停剑。”\n\n没有人名，没有时辰，也没有下令人。"
      },
      {
        "change": "停阵空载响应成立，原先“追后三步”错误偏向未出现，但不能替代正式停阵复验。",
        "source_evidence": "赵矩还要改字，闻岚已用指节点了点刻线：“空载响应成立，错误偏向未出现。写有效。另注：不能替代正式停阵复验。”"
      },
      {
        "change": "事故表已叠入停阵模拟附页、苏叶见证单和左三左四左五试调记录，作为明日正式停阵复验材料。",
        "source_evidence": "她将停阵模拟附页、苏叶见证单和左三左四左五试调记录叠在一起，压到事故表下。\n\n“明日正式停阵复验。同时复查伤势。复验前，禁线不撤，阵眼不得接触，整阵不得启动。”"
      },
      {
        "change": "乙字训练剑阵停阵复验有效，口令响应恢复正常，且未启动整阵。",
        "source_evidence": "闻岚收回牵引尺：“停阵复验有效。口令响应恢复正常。未启动整阵。”"
      },
      {
        "change": "姜守的阵堂小考资格由冻结改为带条件准入。",
        "source_evidence": "最后，他把资格栏的“冻结”划去，改为“带条件准入”，盖下管事印。"
      },
      {
        "change": "校准镜仍裂损且不可恢复，编号被抄入赔偿排期。",
        "source_evidence": "赵矩将裂损的校准镜编号抄入赔偿排期，镜面裂纹仍横贯正中，没有任何恢复的余地。"
      }
    ],
    "relationship_changes": [
      {
        "change": "赵矩依据维护签上的姜守签押，将姜守临时列为事故首要说明人。",
        "source_evidence": "赵矩从夹板中抽出维护签。纸签末尾确有“姜守”二字，旁边还压着阵务小印。\n\n他用笔尖点住签押：“事故先认记录。姜守，暂列首要说明人。”"
      },
      {
        "change": "苏叶因隔离工单成为乙字剑阵测试区隔离协助人，负责看守红绳并阻止姜守违规接触运行阵眼。",
        "source_evidence": "姜守换了一栏：“后续任务二：隔离乙字剑阵测试区。协助人，苏叶。职责：拉设隔离绳，阻止无关人员入内，阻止姜守违规接触运行阵眼。”"
      },
      {
        "change": "苏叶成为姜守违规接触运行阵眼、伤势加重、多放木剑和镜损的正式目击见证人。",
        "source_evidence": "苏叶的隔离木牌还在轻晃。她抿紧唇，写下：“已口头阻止。姜守仍接触阵眼。伤势加重、多放木剑、镜损，均亲眼所见。”"
      },
      {
        "change": "苏叶因共同事故隔离证词单承担随行核对阵务柜记录的义务，但明确不替姜守免责。",
        "source_evidence": "苏叶沉默片刻，在单末补写：“随行核对，不作免责。”"
      },
      {
        "change": "苏叶继续作为共同事故隔离证词单的随行见证人，见证姜守未触碰阵材和阵眼。",
        "source_evidence": "“同意。”姜守点头，“我不碰阵材。查簿。样钉由值守弟子夹出，放停阵材料台。苏叶见证我未伸手。”"
      },
      {
        "change": "赵矩因事故表补事实的压力，被迫把维护签不能单独定责和三枚灵钉缺口写入记录。",
        "source_evidence": "赵矩看着自己亲手用来扣贡献、冻结资格的事故表，脸色发沉。若这表不能补事实，前面的裁定也不牢。"
      },
      {
        "change": "苏叶因共同事故隔离证词，从单纯阻止姜守靠近，变成代放观察标记并签押的见证执行人。",
        "source_evidence": "姜守取出共同事故隔离证词单，用右手提笔：“阻止方式：由苏叶代放观察标记，避免姜守接触现场。”"
      },
      {
        "change": "闻岚允许姜守准备停阵监督下的局部低强度校阵方案，但前提是先验左掌伤势，且不免除姜守带伤违规。",
        "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
      },
      {
        "change": "苏叶确认自己下一步会到场见证闻岚安排的伤势验看与方案审查，伤势不合则方案停止。",
        "source_evidence": "苏叶收起短令：“我到场见证。伤势不合，方案当场止。”"
      },
      {
        "change": "苏叶正式撤回对姜守主动改写口令签的判断，但仍坚持姜守带伤违规、禁令和后果不撤。",
        "source_evidence": "她按下见证印：“我撤回改签判断。但带伤私自校阵是另一项事实，禁令与后果不撤。”"
      },
      {
        "change": "苏叶在后续复验中的协作角色确定为递工具、读刻度、写见证，同时限制姜守只能口述。",
        "source_evidence": "苏叶把工具递送栏移到自己面前，签下姓名：“下一次你只许口述。我递工具、读刻度、写见证。”"
      },
      {
        "change": "本章左五调整形成姜守口述、苏叶代操作并见证、闻岚监督采信的协作关系。",
        "source_evidence": "苏叶搬来工具匣，放在禁线外侧：“按共同事故隔离条款，我递工具、读刻度、代移停阵外缘校针、写见证。你只许说。若说话带出动作倾向，我有权让你后退。”"
      },
      {
        "change": "赵矩被闻岚要求在事故表中补写已核事实，不能只以未修复压掉左五局部有效记录。",
        "source_evidence": "闻岚将见证单压在事故表上：“事故表记录事故，也记录复核。补写。”"
      },
      {
        "change": "苏叶继续作为共同事故隔离见证人实际约束姜守口述流程，并把停手、读数、复位写成有效见证。",
        "source_evidence": "她记完“停手、读数、复位”，才抬起校针：“可以继续口述。”"
      },
      {
        "change": "赵矩受闻岚裁定和事故表格式约束，被迫承认未启动整阵符合本次方案，并记录模拟有效。",
        "source_evidence": "赵矩提笔，在第一栏写下“未启动完整剑阵，符合本次方案”。"
      },
      {
        "change": "苏叶不再认为姜守主动改写口令签，但仍区分并保留姜守带伤校阵责任。",
        "source_evidence": "她搁笔道：“维护签拓印、磨损拖向、三枚定向灵钉缺口与回声阵牌能力边界相互核验，已排除姜守主动改写口令签的单一判断。带伤校阵是另一项，不随此判断撤销。”"
      }
    ],
    "cultivation_changes": [
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "左掌阵火灼伤被写入事故记录，症状明确为导灵时刺痛、抖动，可能导致灵纹失稳。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他另起一行写道：“姜守，左掌阵火灼伤，导灵时刺痛、抖动，可能致灵纹失稳。伤势解除前，不得直接接触运行阵眼。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "伤势解除前不得直接接触运行阵眼的禁令被赵矩确认即刻适用。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他另起一行写道：“姜守，左掌阵火灼伤，导灵时刺痛、抖动，可能致灵纹失稳。伤势解除前，不得直接接触运行阵眼。”\n\n赵矩抬头确认：“禁令即刻适用。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 加重，症状升级为左掌由红转紫、指尖不受控颤动、灵气在伤处乱窜，基础吐纳只能勉强压住。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守踉跄退开，左掌已由红转紫，指尖不受控地颤动。灵气在伤处乱窜，连他强行运转的基础吐纳也只能勉强压住。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效，姜守伤势解除前不得直接接触运行阵眼。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "随后，他重重合上表夹：“剑阵继续停用。隔离绳外移一丈。姜守伤势解除前，不得直接接触运行阵眼。苏叶继续看守，证词候补。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "recovery",
        "change": "姜守使用灼伤膏后，left-palm-burn 从加重状态部分缓解：灼痛减轻，但掌中仍刺痛，导灵时五指抖动、灵流散乱。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守用右手挑起药膏，薄薄涂过左掌。凉意刚渗进去，紫红的掌纹便猛地一抽。他闭目吐纳，把乱窜的灵气压回经脉。十息后，灼痛不再直钻臂弯，却仍像细针埋在掌中；他试着引过一缕灵气，五指立刻抖了一下，灵流也随之散乱。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 仍未解除，当前状态为伤势部分缓解但仍有刺痛及导灵抖动。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "值守弟子盖上药柜小章：“灼伤膏消耗一份。伤势部分缓解，仍有刺痛及导灵抖动。禁止接触运行阵眼继续有效。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效，姜守伤势未解除前不得接近运行阵眼三尺，不得接触运行阵眼。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "苏叶按住他的腕口：“安全条款第九：伤势未解除前，不得接近运行阵眼三尺。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 仍未解除，灼伤膏凉意已散，左掌仍刺痛。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守只用右手翻页，左掌在袖中一阵刺痛。灼伤膏的凉意已散，导灵虽未动，掌心仍像被细针沿纹路敲。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效，姜守伤势未解除，禁近运行阵眼三尺，且不能触碰阵材以免混淆责任。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "苏叶翻条款：“伤势未解除，禁近运行阵眼三尺。阵务柜不是阵眼，但阵材触碰会混责任。姜守只能翻簿，不能碰钉。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 仍未解除；灼伤膏凉意已散，左掌持续刺痛，影响书写稳定。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守站在线外，左手垂在袖中。灼伤膏的凉意早已散尽，掌心一阵阵刺痛，像有细针顺着旧伤往指缝里钻。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 在观察时再次刺痛，导致右手记录字迹发抖。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他运起灵纹辨识，并未导灵入阵，只凭纹路的深浅、焦边和磨亮处辨认。左掌虽未使力，掌心仍猛地抽痛了一下。他右手握笔，笔锋在纸上抖出一小截墨尾。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效；观察期间姜守不得越过三尺禁线，不得触碰阵眼及阵材。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "赵矩沿线走了一圈，又俯身查过阵眼封条，才把事故表夹在木板上：“封条无损。停阵未解。观察期间，姜守不得越线，不得触碰阵眼及阵材。谁动过什么，写清楚。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "ability",
        "change": "pattern-reading 本章用于辨认灵纹磨损和导灵方向，且明确不能判断移动灵钉的人。",
        "state_id": "pattern-reading",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“谁拖的？”\n\n“不知道。”姜守答得干脆，“灵纹辨识只认磨损和方向，不认手。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 仍未解除；未导灵时仍刺痛。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他说一句，放一样。左掌藏在袖中，未曾导灵，灼伤处仍一阵阵刺痛。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 影响签字动作，疼痛导致右手轻颤并拖出墨尾；未解除。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守签字时，左掌疼得右手也轻颤，末笔拖出一道墨尾。苏叶立即抽走印泥：“只许签，不许导灵压印。我代放，赵管事见证。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效；复核期间姜守不得触碰阵材，不得因证据进展靠近乙字阵眼三尺。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "苏叶先看他的手：“复核期间不得触碰阵材，不得以证据有利为由靠近乙字阵眼三尺。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 在闻岚短令中再次确认：阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 经闻岚验看确认未解除；短时低强度导灵观察完成后，姜守不得接触运行阵眼，今日不得再导灵。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "闻岚落笔：“left-palm-burn未解除。短时低强度导灵观察已完成，不得接触运行阵眼。今日不得再导灵。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效：三尺禁线不撤，姜守不得导灵。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "闻岚在方案角上盖印：“准予审证。三尺禁线不撤，姜守不得导灵。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "姜守新增本日不得再导灵的临时限制；伤势未解除，禁令继续。",
        "state_id": "no-more-guiding-today",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "她又看向姜守：“今日不得再导灵。伤势未解除，禁令继续。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "injury",
        "change": "left-palm-burn 仍未解除，左掌仍有刺痛。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守把缠着药布的左掌背到身后。掌心阵火灼痕仍一阵阵发刺，手指稍一蜷便牵着痛，并无解除的迹象。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效：姜守不得导灵、不得越线、不得触碰运行阵眼。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守刚抬眼，闻岚又道：“你不得导灵，不得越线，不得触碰运行阵眼。今日不得再导灵，仍然有效。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "no-more-guiding-today 继续有效，姜守今日不得再导灵。",
        "state_id": "no-more-guiding-today",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "姜守刚抬眼，闻岚又道：“你不得导灵，不得越线，不得触碰运行阵眼。今日不得再导灵，仍然有效。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "recovery",
        "change": "left-palm-burn 部分恢复：刺痛减轻，但导灵抖动风险仍在，伤势未解除。",
        "state_id": "left-palm-burn",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "闻岚按过伤痕边缘，姜守手指轻轻一抖。她收手道：“left-palm-burn记部分恢复。刺痛减轻，导灵抖动风险仍在。未解除。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "live-array-contact-ban 继续有效至下次巡验确认；姜守资格继续冻结。",
        "state_id": "live-array-contact-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "赵矩随即补入事故表：“live-array-contact-ban继续有效，至下次巡验确认。资格继续冻结。裂镜赔偿保留，带伤校阵处分保留，贡献点余额六点，已扣二点不退。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "recovery",
        "change": "姜守左掌阵火灼伤经停用运行阵眼、灼伤膏、稳定吐纳与现场巡验确认后解除。",
        "state_id": "left-palm-burn",
        "state_action": "resolve",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "她逐项核对：“连续停用运行阵眼，有记录。灼伤膏已用尽，有领用与消耗记录。稳定吐纳七次，有见证。现场巡验无刺痛、无导灵抖动、无灵纹失稳。”\n\n闻岚在验伤单上写下同一行标记：left-palm-burn，解除。"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "姜守因左掌伤势解除，live-array-contact-ban 失效。",
        "state_id": "live-array-contact-ban",
        "state_action": "resolve",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“live-array-contact-ban随伤势解除失效。”"
      },
      {
        "subject_id": "jiang-shou",
        "kind": "restriction",
        "change": "姜守新增两日内不得独立启动完整剑阵的限制；期间只能在监督下参与停阵或局部低强度校阵。",
        "state_id": "two-day-complete-array-independent-start-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "闻岚点头：“两日内不得独立启动完整剑阵。只能在监督下参与停阵，或局部低强度校阵。”"
      }
    ],
    "resource_changes": [
      {
        "owner_id": "jiang-shou",
        "resource_id": "contribution-point",
        "operation": "consume",
        "amount": 2,
        "unit": "点",
        "resulting_balance": 6,
        "source_or_destination": "事故处罚扣除",
        "change": "姜守被扣除 contribution-point 2点，余额由8点变为6点。",
        "source_evidence": "赵矩取出姜守的贡献牌，连续扣下两道印记：“扣贡献二点。原有八点，现余六点。阵堂小考资格即刻冻结，待事故复核、赔偿排期与伤势验明后再议。”"
      },
      {
        "owner_id": "jiang-shou",
        "resource_id": "burn-salve",
        "operation": "consume",
        "amount": 1,
        "unit": "份",
        "resulting_balance": 0,
        "source_or_destination": "左掌阵火灼伤外敷治疗",
        "change": "姜守消耗1份灼伤膏，burn-salve 余额由1份变为0份。",
        "source_evidence": "值守弟子盖上药柜小章：“灼伤膏消耗一份。伤势部分缓解，仍有刺痛及导灵抖动。禁止接触运行阵眼继续有效。”"
      }
    ],
    "knowledge_changes": [
      {
        "character_id": "su-ye",
        "fact_id": "command-slip-tamperer",
        "state": "believes_false",
        "belief": "姜守为了催缴维修贡献，主动改写口令签，想让候选人吃苦头。",
        "supersedes_fact_ids": [],
        "change": "苏叶当面说出并维持对姜守改写口令签的误信。",
        "source_evidence": "苏叶正在整理安全册，闻言冷声道：“你最会拿流程把自己摘干净。前日你催候选人补维修贡献，今日口令就从停剑变成追后三步。姜守，是不是你为了催缴，主动改写了口令签，想让他们吃些苦头？”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "command-slip-verification-lead",
        "state": "investigating",
        "belief": "需要通过维护签拓印、原签时辰及现场记录核验苏叶关于他改写口令签的判断。",
        "supersedes_fact_ids": [],
        "change": "姜守将苏叶的指控转化为待核验事项。",
        "source_evidence": "姜守低头续写：“苏叶提出风险判断，待以维护签拓印、原签时辰及现场记录核验。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "jiang-shou-liability",
        "state": "suspects",
        "belief": "维护签上有姜守签押，因此姜守须作为首要说明人在演武前提交可核验说明，否则按签押上报。",
        "supersedes_fact_ids": [],
        "change": "赵矩将对姜守的责任怀疑落实为首要说明人身份和提交说明的期限要求。",
        "source_evidence": "赵矩将维护签锁进木匣，贴上封条：“拿批签去阵务柜调拓印。明日申时前，给我一份阵堂能核的说明。若只有‘不是我’，我便照签押上报。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "maintenance-rubbing-limited-proof",
        "state": "knows",
        "belief": "维护签拓印只能证明维护项归姜守、签押是姜守、原签入柜时辰，不能证明口令错位由姜守改写。",
        "supersedes_fact_ids": [],
        "change": "姜守确认维护签拓印的证明范围和局限。",
        "source_evidence": "姜守将拓印举到光下：“能证明三件事。维护项归我，签押是我，原签何时入柜。不能证明口令错位由我改写。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "command-slip-tamperer",
        "state": "believes_false",
        "belief": "姜守为了催缴维修贡献，主动改写口令签，想让候选人吃苦头。",
        "supersedes_fact_ids": [],
        "change": "苏叶继续维持对姜守改写口令签的误信。",
        "source_evidence": "她仍按下见证印：“先说清楚，我还是认为口令签是你动的。你想催缴维修贡献，才故意让剑阵追人。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "jiang-shou-violation-witnessed",
        "state": "knows",
        "belief": "苏叶亲眼见到姜守在她口头阻止后仍接触运行阵眼，并造成伤势加重、多放木剑和镜损。",
        "supersedes_fact_ids": [],
        "change": "苏叶取得姜守新增违规及其后果的目击知识。",
        "source_evidence": "苏叶的隔离木牌还在轻晃。她抿紧唇，写下：“已口头阻止。姜守仍接触阵眼。伤势加重、多放木剑、镜损，均亲眼所见。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "maintenance-rubbing-limited-proof",
        "state": "knows",
        "belief": "维护签拓印仅证明签押、维护项及存档时辰，不能单独定责口令改写。",
        "supersedes_fact_ids": [],
        "change": "赵矩在已核事实栏正式承认维护签拓印不能单独定责口令改写。",
        "source_evidence": "赵矩看了他片刻，翻回前页，在已核事实栏补写：“维护签拓印仅证明签押、维护项及存档时辰，不能单独定责口令改写。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "jiang-shou-liability",
        "state": "knows",
        "belief": "姜守炼气二层，阵火灼伤未解除却违反禁令带伤接触运行阵眼，导致乙字训练剑阵多放一轮木剑和校准镜裂损。",
        "supersedes_fact_ids": [
          "jiang-shou-liability"
        ],
        "change": "赵矩对姜守责任的状态由维护签责任怀疑推进为对新增违规事实的正式记录。",
        "source_evidence": "赵矩回到案前，逐栏落笔：“现场复核失败。姜守，炼气二层，阵火灼伤未解除，违反禁令，带伤接触运行阵眼。后果：乙字训练剑阵多放一轮木剑，校准镜裂损。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "remaining-evidence-chain",
        "state": "investigating",
        "belief": "灵纹磨损、灵钉方向、回声阵牌与领用时辰仍未核验，口令错位责任尚无完整证据链。",
        "supersedes_fact_ids": [],
        "change": "姜守后续调查目标明确为维护签之外的证据链。",
        "source_evidence": "姜守收起拓印。左掌每颤一下，纸角便跟着轻响。资格已经冻结，镜债已经落账，剑阵仍伏在红绳内没有修好；而灵纹磨损、灵钉方向、回声阵牌与领用时辰，尚无一项填进表里。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "command-slip-tamperer",
        "state": "believes_false",
        "belief": "苏叶仍认为姜守为了催缴维修贡献改了口令，保留姜守改写口令签的判断，但其笃定已因回声阵牌只能复述而松动。",
        "supersedes_fact_ids": [],
        "change": "苏叶的误信未被淘汰，但开始动摇，并在证词中区分亲眼所见事实与自己的判断。",
        "source_evidence": "苏叶终于拿笔，重重写下：“复测前口令为‘后退三步，停剑’。复测时木剑多追一段，校准镜被击裂。本人仍保留姜守改写口令签之判断。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "回声阵牌只留完整口令，不载说话者、不载时辰，不能单独定责，不能直接翻案。",
        "supersedes_fact_ids": [],
        "change": "姜守确认回声阵牌的证据边界，知道其不能单独定责或直接翻案。",
        "source_evidence": "“它只留完整口令。”姜守看向赵矩，“请记：不载说话者，不载时辰，不能单独定责。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "回声阵牌只会复述完整口令，不能回答是谁喊的、何时收到或是否与姜守改签有关。",
        "supersedes_fact_ids": [],
        "change": "苏叶亲自追问后得知回声阵牌只能复述口令，不能提供说话者、时辰或定责信息。",
        "source_evidence": "苏叶俯身追问：“是谁喊的？”\n\n“后退三步，停剑。”\n\n“何时收到？”\n\n“后退三步，停剑。”\n\n“是不是姜守改签以后收到的？”\n\n“后退三步，停剑。”\n\n苏叶直起身，眼中的笃定松动了一线：“它只会复述。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "回声阵牌仅证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。",
        "supersedes_fact_ids": [],
        "change": "赵矩将回声阵牌的证据边界写入事故表未核验栏。",
        "source_evidence": "赵矩这才在未核验栏后补写：“回声阵牌仅证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "remaining-evidence-chain",
        "state": "investigating",
        "belief": "下一步需要调维护签拓印原件，核灵纹磨损方向，查定向灵钉领用时辰与实物缺口，并结合证词核复测前后动作。",
        "supersedes_fact_ids": [
          "command-slip-verification-lead"
        ],
        "change": "姜守将后续调查目标细化为维护签拓印、灵纹磨损方向、定向灵钉领用时辰与实物缺口及证词核对。",
        "source_evidence": "姜守等他落笔：“下一步，调维护签拓印原件，核灵纹磨损方向，再查定向灵钉领用时辰与实物缺口。”\n\n“你想用这些翻案？”赵矩问。\n\n“阵牌不能翻案。”姜守逐项道，“维护签核签押内容，磨损核导灵偏向，灵钉记录核领用与缺口，证词核复测前后动作。合起来才够。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "direction-spirit-nail-gap",
        "state": "knows",
        "belief": "阵堂定向灵钉账面十二枚，乙字训练剑阵现场登记九枚，上次归还签押未见三枚入库，对应领用时辰为空。",
        "supersedes_fact_ids": [],
        "change": "姜守查明三枚定向灵钉未登记缺口。",
        "source_evidence": "“阵堂公物账面，十二枚。”姜守念，“乙字训练剑阵现场登记，九枚在位。上次归还签押，未见三枚入库。对应领用时辰，空。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "maintenance-sign-not-sole-liability",
        "state": "knows",
        "belief": "维护签存在，但不足以单独定责，需合并灵纹、灵钉、现场记录核验。",
        "supersedes_fact_ids": [],
        "change": "姜守推动赵矩在事故表上确认维护签不能单独定责。",
        "source_evidence": "他终究写下：“维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "yuan-ke-spirit-nail-statement",
        "state": "knows",
        "belief": "袁客口称自己临时拿过几枚定向灵钉周转，但没有填明数量、时辰、归还处；三枚缺口仍待其补正。",
        "supersedes_fact_ids": [],
        "change": "姜守记录袁客关于定向灵钉周转的含糊口头说法。",
        "source_evidence": "袁客立刻拱手：“赵管事，我只是说外门常有周转。我确实临时拿过几枚定向灵钉，想着补齐就好，没想到查得这么急。”\n\n姜守在口头记录栏写下原话：“临时拿过几枚定向灵钉周转。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "remaining-evidence-chain",
        "state": "investigating",
        "belief": "下一步还要查维护签拓印、灵纹磨损方向、灵钉方向；本章只先固定三枚定向灵钉缺口。",
        "supersedes_fact_ids": [
          "remaining-evidence-chain"
        ],
        "change": "姜守把后续调查目标推进到维护签拓印、灵纹磨损方向和灵钉方向。",
        "source_evidence": "“在。”姜守收好待补领用单，“所以还要查维护签拓印、灵纹磨损方向、灵钉方向。今天只处理三枚不能写成若干。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "direction-spirit-nail-gap",
        "state": "knows",
        "belief": "苏叶亲眼见证阵务柜领用簿与乙字现场登记相差三枚，未见对应领用登记。",
        "supersedes_fact_ids": [],
        "change": "苏叶知道三枚灵钉缺口客观存在。",
        "source_evidence": "苏叶看着单子，又看自己的证词单，咬唇添字：“本人见证阵务柜领用簿与乙字现场登记相差三枚，未见对应领用登记。袁客口称临时拿过几枚定向灵钉周转，未明数量及时辰。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "command-slip-tamperer",
        "state": "believes_false",
        "belief": "苏叶仍未确认姜守没有改签；她认为三枚灵钉缺口不能证明姜守没改签，但也把自己的判断暂不并入事实。",
        "supersedes_fact_ids": [],
        "change": "苏叶的 command-slip-tamperer 误信继续动摇但未被淘汰。",
        "source_evidence": "写完，她声音低了些：“这不能证明姜守没改签。”\n\n姜守道：“同意。不能单独证明。也不能证明我改签。”\n\n苏叶没反驳，只在旁补：“本人判断另列，暂不并入事实。”"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing",
        "state": "conceals",
        "belief": "袁客承认临时拿过几枚定向灵钉周转，但回避具体数量、时辰、归还去向，并试图不把话写死。",
        "supersedes_fact_ids": [
          "spirit-nail-borrowing"
        ],
        "change": "袁客的隐瞒状态更新为已留下含糊口头记录但仍不补登记。",
        "source_evidence": "姜守抬笔避开：“没写死。因为你不填数量和时辰，所以写‘几枚’。但事故表数字栏已核三枚缺口，待你补正。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "direction-spirit-nail-gap",
        "state": "knows",
        "belief": "赵矩已在事故表上记录三枚定向灵钉账面与现场登记不合，无对应领用登记，需核验。",
        "supersedes_fact_ids": [],
        "change": "赵矩正式知道并记录三枚定向灵钉缺口。",
        "source_evidence": "赵矩夺笔落字：“三枚定向灵钉账面与现场登记不合，无对应领用登记，需核验。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "maintenance-sign-not-sole-liability",
        "state": "knows",
        "belief": "赵矩已记录维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。",
        "supersedes_fact_ids": [],
        "change": "赵矩正式记录维护签不能单独定责。",
        "source_evidence": "他终究写下：“维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "array-command-error-cause",
        "state": "investigating",
        "belief": "追后三步的错误证据链新增三处钉尾与旧压痕不合、灵纹磨痕拖向执行侧；但仍不能单独定责，需要继续合并维护签拓印和灵钉领用时辰。",
        "supersedes_fact_ids": [],
        "change": "姜守将调查从灵钉数量缺口推进到方向异常与磨痕异常，并保留责任边界。",
        "source_evidence": "“所以要合并时辰。”姜守道。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "remaining-evidence-chain",
        "state": "investigating",
        "belief": "下一步要追查三枚定向灵钉的数量、领用时辰、归还去向和经手人，袁客是重点对象。",
        "supersedes_fact_ids": [],
        "change": "姜守在抄录纸末尾列出下一步追问项，并写上袁客名字。",
        "source_evidence": "他在末尾补了四项：三枚数量，领用时辰，归还去向，经手人。\n\n最上方写着袁客的名字。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "command-slip-tamperer",
        "state": "believes_false",
        "belief": "苏叶对姜守改签的判断继续后移、动摇，但仍不撤回；她认为三枚缺口和三处错向都不能直接证明姜守没改，需等维护签拓印入柜时辰与灵钉领用、归还时辰对上。",
        "supersedes_fact_ids": [],
        "change": "苏叶承认方向异常使她先前判断后移，但明确不撤回 command-slip-tamperer 误信。",
        "source_evidence": "“这些方向，确实不像只凭一张维护签就能解释。”她说，“我先前对你改签的判断，要再往后放。”\n\n姜守问：“撤回？”\n\n“不撤。”苏叶收起竹尺，“三枚缺口、三处错向，都不能直接证明你没改。等维护签拓印的入柜时辰，与灵钉领用、归还时辰对上，我再改证词。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "accident-record-boundary",
        "state": "knows",
        "belief": "事故表已经写明三处相邻钉位的钉尾朝向与旧压痕不一致，灵纹磨痕拖向“追后三步”执行侧；该方向异常不得单独定责，必须与维护签拓印和定向灵钉领用时辰合并核验。",
        "supersedes_fact_ids": [],
        "change": "赵矩受同一事故表约束，将钉尾朝向、旧压痕和灵纹磨痕方向异常写入新增栏，并注明合并核验边界。",
        "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "array-command-error-cause",
        "state": "investigating",
        "belief": "姜守掌握的证据链已推进为：维护签拓印入柜时辰、钉位记录、磨痕方向、三枚未登记单和伤势验看单需带去下一步复验；仍未最终定责。",
        "supersedes_fact_ids": [],
        "change": "姜守把下一步复验所需证据明确整理为五项。",
        "source_evidence": "姜守夹紧事故表：“明日带五项。拓印。钉位记录。磨痕方向。三枚未登记单。伤势验看单。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "remaining-evidence-chain",
        "state": "investigating",
        "belief": "袁客三枚定向灵钉由本人经手、未登记借走已成立，但归还去向仍待核。",
        "supersedes_fact_ids": [],
        "change": "姜守将追问结果更新为三枚、袁客经手、未登记借走、去向待核。",
        "source_evidence": "姜守没有往别处追，只写下：“三枚。袁客经手。未登记借走。去向待核。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "command-slip-tamperer",
        "state": "believes_false",
        "belief": "苏叶已认为“姜守主动改签”不能再作单一解释，并将该判断降为待淘汰，等待闻岚停阵复验；但她尚未正式撤回。",
        "supersedes_fact_ids": [],
        "change": "苏叶的 command-slip-tamperer 误信被降为待淘汰，但未正式 supersedes。",
        "source_evidence": "“‘姜守主动改签’不能再作单一解释。”苏叶提笔，在自己原证词旁添了一行，“判断降为待淘汰，等闻师姐停阵复验。现在不正式撤回。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "array-command-error-cause",
        "state": "investigating",
        "belief": "苏叶知道维护签入柜时辰、部分钉尾异常记录、磨痕方向和袁客三枚未登记借走互相牵制，使姜守主动改签的单一解释接不上。",
        "supersedes_fact_ids": [],
        "change": "苏叶将四项证据并列后，明确发现姜守主动改写口令签的单一路径在时辰和实物记录上接不上。",
        "source_evidence": "她逐项看完，才道：“若说你主动改写口令签，再靠灵钉造成错向，时辰接不上。若说你先动灵钉再改签，磨痕、例检记录和袁客这三枚也不能全接上。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "accident-table-boundary",
        "state": "knows",
        "belief": "赵矩已在事故表中确认维护签不能单独定责，三枚定向灵钉未登记借走成立；同时姜守带伤违规、裂镜赔偿、扣二点贡献及资格冻结仍执行。",
        "supersedes_fact_ids": [],
        "change": "赵矩正式把灵钉缺口、维护签责任边界和姜守原有处分分栏并存。",
        "source_evidence": "赵矩将两页合并誊写：“三枚定向灵钉未登记借走成立。维护签不能单独定责。姜守带伤校阵违规、裂镜赔偿、扣除二点贡献及资格冻结，仍照原栏执行。”"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing",
        "state": "knows",
        "belief": "袁客知道自己经手三枚定向灵钉且未登记，并已被迫写下姓名；但仍称具体归还去向不能确定。",
        "supersedes_fact_ids": [],
        "change": "袁客从含糊承认周转更新为已承认三枚由自己经手且未登记。",
        "source_evidence": "袁客捏起笔，在数量栏写下一个“三”。\n\n“三枚。我经手。未登记。”"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing-destination",
        "state": "conceals",
        "belief": "袁客不交代三枚定向灵钉后来去了何处，也不扩展说明别处短缺和其他经手人。",
        "supersedes_fact_ids": [],
        "change": "袁客仍回避归还去向及长期短缺关系。",
        "source_evidence": "“没有归还记录。”袁客放下笔，“三枚后来去了何处，我不能确定。别处还缺多少、谁拿过什么，不在我这张单里。”"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "qualification-result",
        "state": "investigating",
        "belief": "闻岚已阅新增页，认为灵纹、领用、时辰可合并复验，但后果另记，姜守带伤违规不免；下一步须先验左掌伤势，再审停阵监督下局部低强度校阵方案。",
        "supersedes_fact_ids": [],
        "change": "闻岚把证据进展转化为复验流程入口，而非直接免除处分或解冻资格。",
        "source_evidence": "“新增页已阅。灵纹、领用、时辰可合并复验，后果另记。姜守带伤违规不免。”"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "array-command-error-cause",
        "state": "knows",
        "belief": "闻岚已合并采信维护签入柜时辰、见证印、钉尾异常、磨痕拖向、三枚灵钉未登记缺口，并据此裁定这些事实足以排除姜守主动改写口令签这一单一判断，但不能判断谁移了灵钉，也不能免除姜守带伤违规。",
        "supersedes_fact_ids": [
          "qualification-result"
        ],
        "change": "闻岚对前期复验证据作出正式采信和边界裁定。",
        "source_evidence": "闻岚将材料并拢：“维护签入柜时辰、见证印、钉尾异常、磨痕拖向、三枚灵钉未登记缺口，合并采信。”\n\n苏叶问：“能据此判断谁移了灵钉？”\n\n“不能。”\n\n“能据此免除姜守的带伤违规？”\n\n“不能。”\n\n“那能排除什么？”\n\n“足以排除‘姜守主动改写口令签’这一单一判断。”闻岚道，“维护签先入柜，实物方向后有异常，又存在脱离登记的灵钉。不能越过实物和时辰，只凭一张签定责。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "command-slip-tamperer",
        "state": "knows",
        "belief": "苏叶已正式撤回“姜守主动改写口令签”的误信，承认该判断被共同事故隔离证词单列入淘汰栏。",
        "supersedes_fact_ids": [
          "command-slip-tamperer"
        ],
        "change": "苏叶的 command-slip-tamperer 误信被共同事故隔离证词单正式淘汰。",
        "source_evidence": "苏叶沉默片刻，拿起共同事故隔离证词单，将原判断划入淘汰栏，逐字写下：\n\n“command-slip-tamperer由新事实淘汰。supersedes_fact_ids：maintenance-sign-storage-time、three-nail-unregistered-gap、nail-tail-mismatch、wear-drag-direction。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "jiang-shou-injury-violation-consequence",
        "state": "knows",
        "belief": "苏叶知道姜守未主动改写口令签不等于免除带伤私自校阵，禁令与后果仍不撤。",
        "supersedes_fact_ids": [],
        "change": "苏叶将改签判断与带伤违规后果分栏处理。",
        "source_evidence": "她按下见证印：“我撤回改签判断。但带伤私自校阵是另一项事实，禁令与后果不撤。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "accident-table-verified-boundaries",
        "state": "knows",
        "belief": "赵矩已在事故表补写核验边界：维护签不能单独定责，回声阵牌不能单独定责，三枚定向灵钉未登记缺口成立，姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。",
        "supersedes_fact_ids": [
          "accident-table-boundary"
        ],
        "change": "赵矩被迫在同一事故表内补写已核事实和仍保留的后果。",
        "source_evidence": "第一行：维护签不能单独定责。\n\n第二行：回声阵牌不能单独定责。\n\n第三行：三枚定向灵钉未登记缺口成立。\n\n第四行：姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "outer-rune-test-results",
        "state": "knows",
        "belief": "姜守知道三处外缘调整路径已被停阵试调确认：左三可压回，左四可压回但迟滞，左五仍偏且需另定停阵步骤。",
        "supersedes_fact_ids": [],
        "change": "姜守掌握的修复线索推进为可用于后续分步调整的外缘试调结果。",
        "source_evidence": "闻岚收针。苏叶报下三处刻度，赵矩逐项记表：左三偏向可压回，左四可压回但迟滞，左五仍偏，不得继续。"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing-destination",
        "state": "conceals",
        "belief": "袁客仍未交代三枚定向灵钉的具体归还去向或阵材长期短缺背后的其他关系，只表示回去查。",
        "supersedes_fact_ids": [],
        "change": "袁客的隐瞒状态延续，责任边界未扩展出三枚未登记借走之外。",
        "source_evidence": "袁客脸上的笑淡了些：“我再回去查。”"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "left-five-local-adjustment-effective",
        "state": "knows",
        "belief": "闻岚确认左五停阵局部试调有效。",
        "supersedes_fact_ids": [],
        "change": "闻岚采信苏叶见证单后，确认左五停阵局部试调有效。",
        "source_evidence": "闻岚接过见证单，看完才道：“左五，停阵局部试调有效。”"
      },
      {
        "character_id": "su-ye",
        "fact_id": "left-five-local-adjustment-effective",
        "state": "knows",
        "belief": "苏叶知道左五偏向已压回可接受刻度，且由她代操作、姜守仅口述。",
        "supersedes_fact_ids": [],
        "change": "苏叶通过亲自读数和代操作，知道左五偏向压回可接受刻度。",
        "source_evidence": "压扣回退，校针重新落稳。苏叶等了五息，又以铜尺复核两次：“左五偏向压回可接受刻度。两次读数相同。”"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "left-four-lag-persists",
        "state": "knows",
        "belief": "姜守知道左四能压回但响应拖后，直接完整口令复验仍可能导致停剑侧慢。",
        "supersedes_fact_ids": [],
        "change": "姜守确认左四迟滞仍会影响完整口令复验。",
        "source_evidence": "姜守盯着针尾：“左四能压回，但响应拖后。若直接做完整口令复验，停剑侧仍可能慢。”"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "left-four-lag-persists",
        "state": "knows",
        "belief": "闻岚知道左四迟滞未清，因此不得启动整阵或完整口令复验，只能先拟停阵口令模拟方案并先处理左四。",
        "supersedes_fact_ids": [],
        "change": "闻岚据左四迟滞作出下一步流程裁定。",
        "source_evidence": "闻岚抬手截断争执：“左四迟滞未清，不得启动整阵，不得进行完整口令复验。准许拟停阵口令模拟方案，但方案必须先处理左四。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "accident-form-chapter-0008-updates",
        "state": "knows",
        "belief": "赵矩事故表已补入左五局部试调有效、左四仍迟滞、姜守本次未越三尺禁线、未导灵、未触碰运行阵眼。",
        "supersedes_fact_ids": [],
        "change": "赵矩被要求并实际补写本章三类已核事实。",
        "source_evidence": "赵矩沉默片刻，提笔逐项补入。苏叶核对后，在见证处签下名字，又将今日操作工时一并写明。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "spirit-nail-borrowing-destination",
        "state": "investigating",
        "belief": "袁客三枚定向灵钉未登记借走已核定，但归还去向与时辰仍为空或待查；未确认就应写未确认。",
        "supersedes_fact_ids": [
          "remaining-evidence-chain"
        ],
        "change": "姜守将袁客补充说明的追问范围压缩为三枚定向灵钉的时辰与去向，仍未获得有效答案。",
        "source_evidence": "姜守把纸转正，点了三处：“数量，三枚，已填。时辰，空。去向，空。你只补后两处。”\n\n“若是经他人转手——”\n\n“写你最后确认的时辰与去向。未确认就写未确认。”"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing-destination",
        "state": "conceals",
        "belief": "袁客仍未交代三枚定向灵钉的具体归还时辰与去向，只留下待查。",
        "supersedes_fact_ids": [],
        "change": "袁客对三枚定向灵钉的归还去向与时辰继续未给出实质说明。",
        "source_evidence": "袁客握笔片刻，终究只写下“待查”，没有添出别的责任。"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "spirit-nail-liability-boundary",
        "state": "knows",
        "belief": "当前只核三枚定向灵钉未登记借走，其他阵材短缺不作推定。",
        "supersedes_fact_ids": [],
        "change": "闻岚明确袁客责任边界不得扩展到其他短缺推定。",
        "source_evidence": "闻岚收走说明：“只核三枚未登记借走。其他短缺，不作推定。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "simulation-valid-but-not-qualification",
        "state": "knows",
        "belief": "停阵模拟有效且未启动完整剑阵符合方案，但阵堂小考资格仍冻结待验。",
        "supersedes_fact_ids": [],
        "change": "赵矩在事故表上承认停阵模拟的合规与有效，同时维持资格冻结。",
        "source_evidence": "赵矩只能照写，末了在资格栏仍盖上“冻结待验”。"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "闻岚确认回声阵牌只能证明收到过完整口令，不能证明责任人、时辰，也不能单独定责。",
        "supersedes_fact_ids": [],
        "change": "闻岚正式限定回声阵牌证据效力。",
        "source_evidence": "“只能证明它收到过完整口令。”闻岚道，“不证人，不证时辰，不单独定责。”"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "array-command-error-cause",
        "state": "knows",
        "belief": "赵矩在事故表内承认维护签不能单独定责、三枚定向灵钉未登记缺口成立、姜守主动改写口令签的单一判断已被排除，同时姜守带伤违规责任继续保留。",
        "supersedes_fact_ids": [
          "jiang-shou-liability"
        ],
        "change": "赵矩被事故表约束，必须承认已核事实并保留姜守另一项违规责任。",
        "source_evidence": "赵矩只能在事故表内承认：维护签不能单独定责；三枚定向灵钉未登记缺口成立；姜守主动改写口令签的单一判断已被排除；姜守带伤违规责任继续保留。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "array-command-error-cause",
        "state": "knows",
        "belief": "苏叶已淘汰姜守主动改写口令签的单一判断，不再相信姜守是该项口令签篡改者；她仍认为带伤校阵是另一项责任。",
        "supersedes_fact_ids": [
          "command-slip-tamperer"
        ],
        "change": "苏叶在见证单中正式将 command-slip-tamperer 原判断淘汰。",
        "source_evidence": "苏叶同时展开自己的见证单，在“原判断变更”一栏写道：“command-slip-tamperer，淘汰。”"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "spirit-nail-liability-boundary",
        "state": "knows",
        "belief": "闻岚只确认袁客三枚定向灵钉未登记借走，归还去向与时辰未明，其余短缺不作推定。",
        "supersedes_fact_ids": [],
        "change": "闻岚将袁客责任边界限定在三枚未登记借走，未扩展为长期短缺定责。",
        "source_evidence": "闻岚扫过纸面：“只记三枚未登记借走。去向与时辰未明。其余不作推定。”"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing-destination",
        "state": "conceals",
        "belief": "袁客承认三枚灵钉临时周转，但仍未交代清楚归还去向，并试图提及库中其余短缺。",
        "supersedes_fact_ids": [],
        "change": "袁客继续未说明三枚定向灵钉的具体归还去向。",
        "source_evidence": "门外的袁客这时递来一张说明：“三枚灵钉确是临时周转，归还去向还需再核。至于库中其余短缺——”"
      }
    ],
    "thread_changes": [
      {
        "change": "姜守获得调取前日维护签拓印及原签存档时辰的正式工单入口。",
        "source_evidence": "“已构成任务依据。”姜守将工单推到他面前，“后续任务一：调取前日维护签拓印及原签存档时辰，请管事批准。”"
      },
      {
        "change": "赵矩批准调取维护签拓印，但限定必须柜房见证且不得碰运行阵眼。",
        "source_evidence": "片刻后，他在“调取维护签拓印”后重重签下一个“准”。\n\n“只准调拓印，柜房见证。不得碰运行阵眼。”"
      },
      {
        "change": "姜守下一步将前往阵务柜调取维护签拓印。",
        "source_evidence": "姜守拿着批签转身走向阵务柜。维护签拓印，是他在不能碰阵眼的情况下，唯一能先查的东西。"
      },
      {
        "change": "姜守手中已有候选人受伤记录、事故口令和两项工单。",
        "source_evidence": "姜守把候选人受伤记录、事故口令和两项工单夹进旁录簿。左掌仍在灰布下刺痛，最直接的试阵办法已经被禁令封死。"
      },
      {
        "change": "姜守取得维护签拓印、原签入柜时辰与柜房见证印，但该线索只能证明签押和维护项，不能单独洗清或定责口令改写。",
        "source_evidence": "柜后执事将薄纸覆上旧签，以淡墨拓出字迹。拓印上，姜守的签押清清楚楚，维护项写的是：外沿灵纹补描，口令签复位查验。其下还有原签入柜时辰与执事见证印。"
      },
      {
        "change": "姜守阵堂小考资格被冻结，恢复资格需等待事故复核、赔偿排期与伤势验明后再议。",
        "source_evidence": "赵矩取出姜守的贡献牌，连续扣下两道印记：“扣贡献二点。原有八点，现余六点。阵堂小考资格即刻冻结，待事故复核、赔偿排期与伤势验明后再议。”"
      },
      {
        "change": "裂损校准镜的赔偿责任已经落到姜守账上。",
        "source_evidence": "赵矩走到镜前，用登记尺量过裂口，没有尝试扶正镜面：“校准镜裂损，不可现场修复，列入计赔。”\n\n“记我账上。”姜守道。\n\n“已经在你账上。”"
      },
      {
        "change": "乙字训练剑阵继续停用，隔离绳外移一丈，苏叶继续看守并作为证词候补。",
        "source_evidence": "随后，他重重合上表夹：“剑阵继续停用。隔离绳外移一丈。姜守伤势解除前，不得直接接触运行阵眼。苏叶继续看守，证词候补。”"
      },
      {
        "change": "调查从单纯争论姜守是否改写口令签，推进为需要核对维护签拓印、灵纹磨损方向、定向灵钉领用时辰与实物缺口的证据链。",
        "source_evidence": "姜守等他落笔：“下一步，调维护签拓印原件，核灵纹磨损方向，再查定向灵钉领用时辰与实物缺口。”"
      },
      {
        "change": "下一步行动时间与地点确定为明日辰初到阵务柜，姜守资格冻结仍照旧。",
        "source_evidence": "赵矩合上事故表：“明日辰初，阵务柜。冻结照旧。”"
      },
      {
        "change": "姜守保留事故表副页与苏叶证词单作为下一步查钉的凭据。",
        "source_evidence": "姜守收起事故表副页与证词单，退离隔离绳。\n\n“下一项，”他说，“查钉。”"
      },
      {
        "change": "定向灵钉缺口线索成立：账面十二枚、现场九枚、三枚无对应领用登记。",
        "source_evidence": "“阵堂公物账面，十二枚。”姜守念，“乙字训练剑阵现场登记，九枚在位。上次归还签押，未见三枚入库。对应领用时辰，空。”"
      },
      {
        "change": "下一步调查入口转向停阵状态下的灵钉方向和灵纹磨损方向比对。",
        "source_evidence": "姜守望向白布上的样钉箭头，又看向隔离绳内静止的阵纹：“下一项，不碰阵眼，先看钉尾朝向，再看磨痕往哪边拖。”"
      },
      {
        "change": "袁客没有完全认罪，只留下临时拿过几枚定向灵钉周转的含糊记录，并称回去查。",
        "source_evidence": "袁客沉默片刻，没接笔：“我回去查查。”\n\n姜守在单末写：“当场未填，称回去查。”"
      },
      {
        "change": "事故复核从账面缺三枚定向灵钉推进到实物方向异常：现场登记九枚中三处相邻钉位异常。",
        "source_evidence": "赵矩又添上：“现场登记九枚中，三处相邻钉位异常。”"
      },
      {
        "change": "责任归属仍未裁定，方向异常必须与维护签拓印、定向灵钉领用时辰合并核验。",
        "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
      },
      {
        "change": "下一步事故流程转向追查灵钉领用时辰。",
        "source_evidence": "赵矩合上事故表：“资格冻结不变，扣去的两点贡献不退，裂镜照赔。明日先追灵钉领用时辰。”"
      },
      {
        "change": "乙字训练剑阵仍未修复，下一步不是启动整阵，而是明日辰初先验伤，再审停阵监督下局部低强度校阵方案。",
        "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
      },
      {
        "change": "证据链核心拼合完成：维护签入柜时辰、部分钉尾异常记录、磨痕方向、袁客三枚灵钉未登记借走被并列审视。",
        "source_evidence": "苏叶没有立刻签。她把新增页拖到前页旁，将四项记录排成一列：维护签酉初二刻入柜；部分钉尾异常记录在后；磨痕拖向“追后三步”执行侧；三枚灵钉由袁客在签入柜后、例检前未登记借走。"
      },
      {
        "change": "事故调查主线从并列证据推进为闻岚正式采信的组合事实，并排除了姜守主动改写口令签的单一判断。",
        "source_evidence": "“足以排除‘姜守主动改写口令签’这一单一判断。”闻岚道，“维护签先入柜，实物方向后有异常，又存在脱离登记的灵钉。不能越过实物和时辰，只凭一张签定责。”"
      },
      {
        "change": "修复主线获得下一步停阵分步调整许可，但仍不得启动完整乙字训练剑阵或进行完整口令复验。",
        "source_evidence": "闻岚在方案下添注：“外缘灵纹试调完成。准许后续按三处分步调整，不得启动完整乙字训练剑阵，不得进行完整口令复验。”"
      },
      {
        "change": "处分主线未解除：带伤违规责任、裂镜赔偿、阵堂小考资格冻结继续有效。",
        "source_evidence": "第四行：姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。"
      },
      {
        "change": "扣点后果未解除：已扣二点贡献点不退，余额六点。",
        "source_evidence": "赵矩又补：“已扣二点，不退，余额六点。”"
      },
      {
        "change": "主线从左五异常钉位推进到左五停阵局部试调有效，但尚未完成修复。",
        "source_evidence": "赵矩皱眉：“什么三栏？”\n\n“未完成修复，是结果栏。左五局部试调有效，是已核栏。左四仍迟滞，是未决栏。混写会把有效步骤一并抹掉，下次还得重做。”"
      },
      {
        "change": "完整口令复验被闻岚禁止，下一步只能拟停阵口令模拟方案，且必须先处理左四迟滞。",
        "source_evidence": "闻岚抬手截断争执：“左四迟滞未清，不得启动整阵，不得进行完整口令复验。准许拟停阵口令模拟方案，但方案必须先处理左四。”"
      },
      {
        "change": "阵堂小考资格继续冻结，裂镜赔偿和已扣贡献点后果保留。",
        "source_evidence": "闻岚收起事故表：“资格继续冻结。裂镜赔偿保留，扣除的两点贡献不退。左掌伤势未解除，禁线不撤，今日不得再导灵。”"
      },
      {
        "change": "正式停阵复验被推进到明日进行，并将同时复查姜守左掌伤势。",
        "source_evidence": "“明日正式停阵复验。同时复查伤势。复验前，禁线不撤，阵眼不得接触，整阵不得启动。”"
      },
      {
        "change": "阵堂小考资格线仍未放行，保持冻结待验状态。",
        "source_evidence": "赵矩只能照写，末了在资格栏仍盖上“冻结待验”。"
      },
      {
        "change": "袁客线只推进到三枚定向灵钉归还去向与时辰待查，未扩展到阵材长期短缺责任。",
        "source_evidence": "闻岚收走说明：“只核三枚未登记借走。其他短缺，不作推定。”"
      },
      {
        "change": "裂损校准镜仍在木匣中且赔偿签未撤，赔偿责任继续保留。",
        "source_evidence": "左四钉位旁摆着校针、木尺和一张新见证单。裂开的校准镜仍装在木匣里，匣角挂着赔偿签，没人动它。"
      },
      {
        "change": "乙字训练剑阵口令错位修复线完成正式停阵复验，结果为后退三步后停剑，无追加追行。",
        "source_evidence": "三步。\n\n木剑剑尖越过第三道刻线，齐齐停住。追后侧那道曾经多亮一截的灵纹安静无光，三柄木剑也没有再向前追出半寸。"
      },
      {
        "change": "姜守资格线从冻结推进为带条件准入，同时裂镜赔偿、带伤处分和两日禁启保留为后续压力。",
        "source_evidence": "闻岚在旁签押：“乙字训练剑阵停阵复验通过。口令恢复正常。姜守准予参加阵堂小考。裂镜赔偿、带伤校阵处分保留；两日内不得独立启动完整剑阵。”"
      },
      {
        "change": "贡献点扣罚结果维持不变：已扣二点，余额六点，不退还。",
        "source_evidence": "贡献栏也照旧写着：已扣二点，余额六点，不退还。"
      },
      {
        "change": "裂镜赔偿排期的下一步签认时间落到明日辰时。",
        "source_evidence": "她吹干墨迹，把小考前置事项单推到姜守面前。最上方第一行写着：裂镜赔偿排期，明日辰时签认。"
      }
    ],
    "comedy_changes": [
      {
        "change": "姜守将赵矩“先把能证明的都写清”的推诿话写成任务依据，迫使赵矩面对流程。",
        "source_evidence": "姜守当即在下一栏写道：“赵矩管事指示：先把能证明的都写清。”\n\n赵矩眼角一跳：“这句不必记。”\n\n“已构成任务依据。”姜守将工单推到他面前，“后续任务一：调取前日维护签拓印及原签存档时辰，请管事批准。”"
      },
      {
        "change": "姜守把苏叶的安全条款提醒写入工单依据，使她的提醒反过来支持柜房见证流程。",
        "source_evidence": "苏叶下意识接道：“安全条款第九条，确实如此。”\n\n姜守补上一笔：“苏叶援引第九条，证明管事批准与柜房见证均属必要。”"
      },
      {
        "change": "苏叶因自己的安全提醒和条款熟悉被工单绑定为隔离协助人，不能只站在风险条款外指责。",
        "source_evidence": "赵矩看过工单，敲桌道：“你熟条款，就留一班。既看红绳，也看住他的手。”\n\n苏叶沉默片刻，在协助人一栏签名，字锋几乎划破纸面。"
      },
      {
        "change": "赵矩用现场复核栏逼姜守补表，事故扩大后同一张表反而写入维护签不能单独定责的已核事实。",
        "source_evidence": "姜守没有争辩，只用发抖的右手指向事故表上方：“还缺备注。”\n\n苏叶望着他：“你还惦记那句？”\n\n“扣点归扣点，事实归事实。新增违规是带伤接触阵眼。原维护签不能单独证明我改写口令。”"
      },
      {
        "change": "苏叶被赵矩以看守栏条款反制，必须承担阻止姜守违规接触的见证职责。",
        "source_evidence": "赵矩看见她腰间木牌，将事故表推过去：“隔离协助人，签随行时辰。他若接触运行阵眼，你负责阻止并作证。”\n\n“我只是看守——”\n\n“看守栏包含违规阻止。”"
      },
      {
        "change": "姜守把苏叶的安全条款转写成她的监督、看守和记录义务，形成安全条款反差喜剧。",
        "source_evidence": "苏叶按住他的腕口：“安全条款第九：伤势未解除前，不得接近运行阵眼三尺。”\n\n姜守在单上续写：“隔离动作一，苏叶看守隔离绳。姜守靠近运行阵眼三尺，立即拦截。”"
      },
      {
        "change": "苏叶以条款阻止姜守单独复述事故经过，反被姜守推导成她必须签证词。",
        "source_evidence": "苏叶没有接：“事故相关人不得单独复述经过，须有旁证。这也是条款。”\n\n“所以你签。”姜守道，“不签，我只能单独复述，违反条款。签了，你执行条款。”"
      },
      {
        "change": "苏叶把三尺安全距离临时加到四尺，姜守想记录时被她阻止，延续条款被反用的笑点。",
        "source_evidence": "苏叶已经站到他左侧：“去训练场，只能到隔离绳外。离绳四尺。”\n\n“条款要求三尺。”\n\n“多一尺防你临时犯规。”\n\n姜守提笔欲记，苏叶一把按住纸：“这一尺不用写！”"
      },
      {
        "change": "维修工单的数字栏逼迫赵矩不能把三枚写成若干。",
        "source_evidence": "赵矩伸手拿笔：“记，定向灵钉若干缺口待查。”\n\n姜守把事故表推前一寸：“事故表有数字栏。”\n\n赵矩笔尖停住。\n\n“若干不能进数字栏。三枚能。”"
      },
      {
        "change": "姜守把袁客的模糊词逐项改造成待补领用单栏位。",
        "source_evidence": "姜守又写一行：“领用人：大家。需改为姓名。”"
      },
      {
        "change": "姜守坚持只让三枚说明三枚，不扩大成未证实罪名。",
        "source_evidence": "廊柱阴影里，袁客没再说“若干”，只拢袖道：“几枚小钉，未必能说明剑阵为何追人。”\n\n姜守把待补领用单收进夹板：“所以三枚先说明三枚。”"
      },
      {
        "change": "苏叶原本只负责阻止姜守违规，却被姜守和事故表流程反推成代放标记、读尺距、补签注的执行人。",
        "source_evidence": "“只写‘你不能碰’，证词不完整。要写谁来碰标记，标记碰哪里。”"
      },
      {
        "change": "安全条款的执行让苏叶多出三只纸框、九次尺距和两处签押的劳动。",
        "source_evidence": "姜守道：“你守住了。只是这条线附带三只纸框、九次尺距和两处签押。”"
      },
      {
        "change": "赵矩以事故表格式否定苏叶想写“被迫”的抱怨。",
        "source_evidence": "“哪两个？”\n\n“被迫。”\n\n赵矩淡淡道：“事故表没有‘被迫’栏。”"
      },
      {
        "change": "袁客用“周转”“大家都用”“大约还到别处”等模糊说法回避责任，姜守逐项拆成数量、时辰、归还去向、领用人姓名四个待补栏，迫使其至少承认三枚未登记。",
        "source_evidence": "袁客盯着四个整整齐齐的“待补”：“姜师弟，你把我一句话拆成了四桩事。”\n\n“本来就是四桩。”"
      },
      {
        "change": "赵矩把工单字面执行到底，明确领用栏、时辰栏、归还栏都不接受袁客的模糊词。",
        "source_evidence": "赵矩翻开事故表：“领用栏不收‘周转’，时辰栏不收‘大概’，归还栏也没有‘大家’这个去向。至少补一项可核事实，否则记四项均拒答。”"
      },
      {
        "change": "袁客试图把“借走”改回“周转”，姜守用表格逻辑要求填写转入处，最终迫使袁客接受“借走”表述。",
        "source_evidence": "袁客指着“借走”二字：“我说的是周转。”\n\n姜守把表转回去：“周转需有转入处。请填。”\n\n袁客看了半晌，又把纸推回来：“借走便借走。”"
      },
      {
        "change": "姜守把袁客的“大家都是这么周转”拆成不可复验的栏位，迫使闻岚按流程盖下“不具备时辰效力”。",
        "source_evidence": "袁客站在材料架旁，道：“三枚灵钉确实经我手。阵堂缺用，大家都是这么周转。”\n\n姜守以右手点向空栏：“‘大家’，无姓名；‘这么’，无方式；‘周转’，无数量、时辰、归还去向。三项均不可复验。”\n\n闻岚在那句话旁盖下一枚小印：不具备时辰效力。"
      },
      {
        "change": "赵矩试图追问局部校阵偏差责任，反被姜守用工单责任栏位推回；赵矩不愿签总责，只好转入审证。",
        "source_evidence": "赵矩敲了敲纸面：“出了偏差，算谁？”\n\n姜守抽出一张空白工单：“方案错误，填方案人；递送错误，填递送人；放行错误，填监督人。若管事认为不可分，可签总责。”\n\n赵矩把手收了回去：“先审证。”"
      },
      {
        "change": "苏叶签下递工具、读刻度、写见证后仍用木尺让姜守再退半步，延续安全条款式喜剧。",
        "source_evidence": "“工作项三项。”姜守道。\n\n“这是隔离共同事故，不是帮你。”\n\n“名称不影响工时。”\n\n苏叶签完最后一栏，又把木尺横回禁线前：“也不影响你再退半步。”"
      },
      {
        "change": "姜守习惯性把操作说成自己动手，被苏叶按安全条款要求后退并改口，形成口述维修笑点。",
        "source_evidence": "“校针向左压回半分，我——”\n\n“停。”苏叶立刻直起身，“伤员出现代操作措辞。按条款，后退一步，改口。”"
      },
      {
        "change": "苏叶把协作隔离条款细化成递工具、读刻度、代操作、写见证的实际工时，安全限制反而成为有效流程。",
        "source_evidence": "她写完时辰、工具、读数和每次停手，又按了见证印。原本所谓隔离共同事故，如今从递钳子到数三息，全落成了她的工时。"
      },
      {
        "change": "姜守将一句未完成拆成结果栏、已核栏、未决栏，用事故表格式反制赵矩压缩流程。",
        "source_evidence": "赵矩皱眉：“什么三栏？”\n\n“未完成修复，是结果栏。左五局部试调有效，是已核栏。左四仍迟滞，是未决栏。混写会把有效步骤一并抹掉，下次还得重做。”"
      },
      {
        "change": "“模拟不许追人”从苏叶的口号被闻岚要求写成正式方案条件。",
        "source_evidence": "苏叶补了一句：“模拟不许追人。”\n\n姜守把这句写进首栏。\n\n闻岚看了她一眼：“不是口号。写成条件。”"
      },
      {
        "change": "苏叶把“停手”扩展成“停口”，使姜守连口述都被纳入见证流程。",
        "source_evidence": "她写下读数，随即道：“停手。”\n\n姜守本来已经开口：“下一步——”\n\n“停手也包括停口。”苏叶指了指见证单，“否则我无法证明读数是在你改令之前还是之后。”"
      },
      {
        "change": "赵矩想以未启动整阵否定测试价值，却被拆成合规栏和空载响应栏，反成记录依据。",
        "source_evidence": "赵矩皱眉：“既不启动整阵，如何算放行测试？”\n\n姜守把一张空白附页推过去：“分两栏。第一栏，未启动整阵是否合规。第二栏，空载响应是否可记。”\n\n“我问的是放行。”\n\n“本章没有放行栏。”"
      },
      {
        "change": "苏叶每读一项就喊一次停手，三次停手都变成有效见证。",
        "source_evidence": "她每读一项，便喊一次“停手”，记一项复位。三次停手都被写成有效见证。"
      },
      {
        "change": "赵矩想先压责任，结果被姜守把话拆成监督、记录、递送读数见证和停手口令四项工单，反把记录责任落到赵矩头上。",
        "source_evidence": "赵矩看了一眼自己方才提出的“先写责任”，那句话已被拆成四项差事，其中记录一项正落在他头上。他把事故表铺开：“先验。但冻结栏不动。”"
      },
      {
        "change": "苏叶用安全条款把姜守的后退和口述距离都写成合规见证。",
        "source_evidence": "苏叶已经把工具盘抱走：“按停阵复验安全条款，你再后退半步。口述时不得探身，不得抬手越线，不得用灵气比画。”\n\n姜守退了半步：“已后退。”\n\n“再说一句。”\n\n“为何？”\n\n“证明你退后还能口述。”\n\n“距离合格，口述正常。”\n\n苏叶在见证单上落笔：“禁线外四尺，声音可达。无需靠近。”"
      },
      {
        "change": "赵矩试图用裂镜和处分继续压资格，姜守把这些后果拆成条件准入栏，反让后果成为准入表格内容。",
        "source_evidence": "赵矩原想用两项后果压住资格，如今两项后果都被钉进了准入条件。他翻回事故表，逐栏核对，最后仍得按既定流程落笔。"
      }
    ],
    "new_constraints": [
      {
        "change": "姜守必须在明日申时前交初步事故说明，并在演武前交复核说明，说明需包含签、时辰、伤情和现场记录。",
        "source_evidence": "赵矩合上半本事故簿：“外门演武前乙字场必须恢复。明日申时前交初步事故说明，演武前交复核说明。要有签、时辰、伤情和现场记录，别只说不是你。”"
      },
      {
        "change": "调取维护签拓印只能调拓印，且必须有柜房见证，姜守不得碰运行阵眼。",
        "source_evidence": "片刻后，他在“调取维护签拓印”后重重签下一个“准”。\n\n“只准调拓印，柜房见证。不得碰运行阵眼。”"
      },
      {
        "change": "苏叶已签隔离协助，但明确不认可姜守无辜。",
        "source_evidence": "“我只签隔离，不签你无辜。”"
      },
      {
        "change": "姜守阵堂小考资格冻结，待事故复核、赔偿排期与伤势验明后再议。",
        "source_evidence": "赵矩取出姜守的贡献牌，连续扣下两道印记：“扣贡献二点。原有八点，现余六点。阵堂小考资格即刻冻结，待事故复核、赔偿排期与伤势验明后再议。”"
      },
      {
        "change": "calibration-mirror 不可现场修复且必须计赔，赔偿问题压在姜守账上。",
        "source_evidence": "裂镜被封条固定，登记牌上添了“不可现场修复、必须计赔”八字。"
      },
      {
        "change": "姜守阵堂小考资格继续被冻结，待事故复核、赔偿排期与伤势验明后再议。",
        "source_evidence": "赵矩摊开事故表，先不写新栏，逐项宣读旧项：“姜守带伤接触运行阵眼，违反禁令，致左掌灼伤加重；错误复测使乙字训练剑阵多放一轮木剑，击裂校准镜。校准镜不可现场修复，计赔。扣贡献二点，余额六点。阵堂小考资格冻结，待事故复核、赔偿排期与伤势验明后再议。”"
      },
      {
        "change": "乙字训练场仍停用隔离，校准镜仍裂损且不可现场修复、计赔待排。",
        "source_evidence": "乙字训练场仍在停用。隔离绳外移一丈，裂开的校准镜放在木架上，白痕斜贯镜面，旁边悬着“不可现场修复，计赔待排”的木牌。"
      },
      {
        "change": "苏叶随行阵务柜，避免事故相关人单独调取记录，但不作免责。",
        "source_evidence": "姜守把证词单递给她：“保留。另加隔离义务：随行阵务柜，避免事故相关人单独调取记录。”\n\n“阵务柜没有运行阵眼。”\n\n“有领用册。”\n\n苏叶沉默片刻，在单末补写：“随行核对，不作免责。”"
      },
      {
        "change": "姜守阵堂小考资格仍冻结，扣除的二点贡献不退，校准镜裂损仍需赔偿，禁令照旧。",
        "source_evidence": "赵矩补完事故表，扔回给他：“资格仍冻结。扣的二点贡献不退。裂镜照赔。禁令照旧。”"
      },
      {
        "change": "乙字剑阵仍处停阵隔离状态，姜守不得越过隔离绳接触阵眼。",
        "source_evidence": "停阵材料台就在训练场外。隔离绳后，乙字剑阵安静伏着，阵眼封条未动。姜守没有越线，只把样钉方向图、领用簿摘录和待补领用单并排压在白布上。"
      },
      {
        "change": "乙字训练剑阵继续停阵隔离，封条无损，停阵未解。",
        "source_evidence": "赵矩沿线走了一圈，又俯身查过阵眼封条，才把事故表夹在木板上：“封条无损。停阵未解。观察期间，姜守不得越线，不得触碰阵眼及阵材。谁动过什么，写清楚。”"
      },
      {
        "change": "姜守阵堂小考资格冻结不变，已扣两点贡献不退，校准镜裂损仍需照赔。",
        "source_evidence": "赵矩合上事故表：“资格冻结不变，扣去的两点贡献不退，裂镜照赔。明日先追灵钉领用时辰。”"
      },
      {
        "change": "本章新增实物异常不能单独定责，只能作为与维护签拓印、定向灵钉领用时辰合并核验的证据。",
        "source_evidence": "赵矩顿了顿，最终写全：“灵纹磨痕拖向‘追后三步’执行侧。该方向异常不得单独定责，须与维护签拓印、定向灵钉领用时辰合并核验。”"
      },
      {
        "change": "姜守带伤校阵违规事实不因维护签核验改变，仍在事故表第五栏单列。",
        "source_evidence": "写完，他又在第五栏补道：姜守带伤私自低强度校阵之违规事实，不因本项核验改变。"
      },
      {
        "change": "姜守原有裂镜赔偿、扣除二点贡献及资格冻结继续执行；没有退点、解冻或免赔。",
        "source_evidence": "赵矩将两页合并誊写：“三枚定向灵钉未登记借走成立。维护签不能单独定责。姜守带伤校阵违规、裂镜赔偿、扣除二点贡献及资格冻结，仍照原栏执行。”"
      },
      {
        "change": "下一步复验前置条件为明日辰初先验左掌伤势，再审停阵监督下局部低强度校阵方案；阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。",
        "source_evidence": "“冻结资格，不等于禁止准备复验。明日辰初，先验左掌伤势，再审停阵监督下局部低强度校阵方案。阵眼封条不动，三尺禁线不撤，姜守不得触碰运行阵眼。”"
      },
      {
        "change": "姜守本日不得再导灵；下一次复验只能口述，由苏叶递工具、读刻度、写见证。",
        "source_evidence": "苏叶把工具递送栏移到自己面前，签下姓名：“下一次你只许口述。我递工具、读刻度、写见证。”"
      },
      {
        "change": "后续调整只能按三处分步进行，不得启动完整乙字训练剑阵，不得进行完整口令复验。",
        "source_evidence": "闻岚在方案下添注：“外缘灵纹试调完成。准许后续按三处分步调整，不得启动完整乙字训练剑阵，不得进行完整口令复验。”"
      },
      {
        "change": "左五外缘灵纹仍偏且不得继续试压，后续需从左五开始另定停阵步骤。",
        "source_evidence": "闻岚指向左五那道未能压回的磨痕：“下一次，从它开始。”"
      },
      {
        "change": "姜守已扣二点贡献点不退，余额六点；该扣点后果继续保留。",
        "source_evidence": "赵矩又补：“已扣二点，不退，余额六点。”"
      },
      {
        "change": "姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。",
        "source_evidence": "第四行：姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。"
      },
      {
        "change": "左四迟滞未清前，不得启动整阵，不得完整口令复验；停阵口令模拟方案必须先处理左四。",
        "source_evidence": "闻岚抬手截断争执：“左四迟滞未清，不得启动整阵，不得进行完整口令复验。准许拟停阵口令模拟方案，但方案必须先处理左四。”"
      },
      {
        "change": "姜守在左五调整中只能口述，若话语带出动作倾向，苏叶可要求他后退。",
        "source_evidence": "苏叶搬来工具匣，放在禁线外侧：“按共同事故隔离条款，我递工具、读刻度、代移停阵外缘校针、写见证。你只许说。若说话带出动作倾向，我有权让你后退。”"
      },
      {
        "change": "事故表新增并固定记录姜守本次未越三尺禁线、未导灵、未触碰运行阵眼。",
        "source_evidence": "“左四仍迟滞。姜守本次未越三尺禁线，未导灵，未触碰运行阵眼。”"
      },
      {
        "change": "停阵模拟方案限制为木剑匣封条不动、内环断灵、外缘刻线只走空载，任何越过停手刻度立即复位。",
        "source_evidence": "苏叶接过笔，在下方添道：“木剑匣封条不动；内环断灵；外缘刻线只走空载；任何一处越过停手刻度，立即复位。”"
      },
      {
        "change": "正式复验前禁线不撤，姜守不得接触阵眼，整阵不得启动。",
        "source_evidence": "“明日正式停阵复验。同时复查伤势。复验前，禁线不撤，阵眼不得接触，整阵不得启动。”"
      },
      {
        "change": "姜守两日内不得独立启动完整剑阵，只能在监督下参与停阵或局部低强度校阵。",
        "source_evidence": "闻岚点头：“两日内不得独立启动完整剑阵。只能在监督下参与停阵，或局部低强度校阵。”"
      },
      {
        "change": "姜守带条件准入阵堂小考的条件包括校准镜赔偿排期、两日禁独立启动整阵、带伤校阵处分记录保留、只能监督下参与停阵或局部低强度校阵。",
        "source_evidence": "姜守把一张空白附页推过去：“不写直接解冻。写条件准入。第一，校准镜裂损不能恢复，列赔偿排期。第二，两日内禁独立启动整阵。第三，带伤校阵处分记录保留。第四，监督下参与停阵或局部低强度校阵。四栏齐全，再判能否小考。”"
      },
      {
        "change": "苏叶作为共同事故隔离见证人承担后续核对工时。",
        "source_evidence": "苏叶在见证单末尾补了一行：“后续核对工时，由共同事故隔离见证人承担。”"
      }
    ],
    "resolved_constraints": [
      {
        "change": "姜守的 live-array-contact-ban 随 left-palm-burn 解除而失效。",
        "source_evidence": "“live-array-contact-ban随伤势解除失效。”"
      }
    ]
  },
  "structured_state": {
    "cultivation": [
      {
        "subject_id": "jiang-shou",
        "stage": "炼气二层",
        "abilities": [
          "基础吐纳",
          "灵纹辨识",
          "低强度校阵",
          "pattern-reading 本章用于辨认灵纹磨损和导灵方向，且明确不能判断移动灵钉的人。"
        ],
        "injuries": [],
        "limits": [
          "no-more-guiding-today 继续有效，姜守今日不得再导灵。",
          "姜守新增两日内不得独立启动完整剑阵的限制；期间只能在监督下参与停阵或局部低强度校阵。"
        ],
        "tracked_states": [
          {
            "state_id": "no-more-guiding-today",
            "kind": "restriction",
            "description": "no-more-guiding-today 继续有效，姜守今日不得再导灵。"
          },
          {
            "state_id": "pattern-reading",
            "kind": "ability",
            "description": "pattern-reading 本章用于辨认灵纹磨损和导灵方向，且明确不能判断移动灵钉的人。"
          },
          {
            "state_id": "two-day-complete-array-independent-start-ban",
            "kind": "restriction",
            "description": "姜守新增两日内不得独立启动完整剑阵的限制；期间只能在监督下参与停阵或局部低强度校阵。"
          }
        ],
        "last_kind": "restriction",
        "last_change": "姜守新增两日内不得独立启动完整剑阵的限制；期间只能在监督下参与停阵或局部低强度校阵。"
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
        ],
        "tracked_states": []
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
        ],
        "tracked_states": []
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
        ],
        "tracked_states": []
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
        ],
        "tracked_states": []
      }
    ],
    "resources": [
      {
        "owner_id": "formation-hall",
        "resource_id": "direction-spirit-nail",
        "amount": 12,
        "unit": "枚"
      },
      {
        "owner_id": "jiang-shou",
        "resource_id": "burn-salve",
        "amount": 0.0,
        "unit": "份",
        "last_operation": "consume",
        "last_source_or_destination": "左掌阵火灼伤外敷治疗"
      },
      {
        "owner_id": "jiang-shou",
        "resource_id": "contribution-point",
        "amount": 6.0,
        "unit": "点",
        "last_operation": "consume",
        "last_source_or_destination": "事故处罚扣除"
      },
      {
        "owner_id": "jiang-shou",
        "resource_id": "low-spirit-stone",
        "amount": 3,
        "unit": "枚"
      }
    ],
    "knowledge": [
      {
        "character_id": "jiang-shou",
        "fact_id": "array-command-error-cause",
        "state": "investigating",
        "belief": "姜守掌握的证据链已推进为：维护签拓印入柜时辰、钉位记录、磨痕方向、三枚未登记单和伤势验看单需带去下一步复验；仍未最终定责。",
        "last_change": "姜守把下一步复验所需证据明确整理为五项。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "direction-spirit-nail-gap",
        "state": "knows",
        "belief": "阵堂定向灵钉账面十二枚，乙字训练剑阵现场登记九枚，上次归还签押未见三枚入库，对应领用时辰为空。",
        "last_change": "姜守查明三枚定向灵钉未登记缺口。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "回声阵牌只留完整口令，不载说话者、不载时辰，不能单独定责，不能直接翻案。",
        "last_change": "姜守确认回声阵牌的证据边界，知道其不能单独定责或直接翻案。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "left-four-lag-persists",
        "state": "knows",
        "belief": "姜守知道左四能压回但响应拖后，直接完整口令复验仍可能导致停剑侧慢。",
        "last_change": "姜守确认左四迟滞仍会影响完整口令复验。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "maintenance-rubbing-limited-proof",
        "state": "knows",
        "belief": "维护签拓印只能证明维护项归姜守、签押是姜守、原签入柜时辰，不能证明口令错位由姜守改写。",
        "last_change": "姜守确认维护签拓印的证明范围和局限。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "maintenance-sign-not-sole-liability",
        "state": "knows",
        "belief": "维护签存在，但不足以单独定责，需合并灵纹、灵钉、现场记录核验。",
        "last_change": "姜守推动赵矩在事故表上确认维护签不能单独定责。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "outer-rune-test-results",
        "state": "knows",
        "belief": "姜守知道三处外缘调整路径已被停阵试调确认：左三可压回，左四可压回但迟滞，左五仍偏且需另定停阵步骤。",
        "last_change": "姜守掌握的修复线索推进为可用于后续分步调整的外缘试调结果。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "spirit-nail-borrowing-destination",
        "state": "investigating",
        "belief": "袁客三枚定向灵钉未登记借走已核定，但归还去向与时辰仍为空或待查；未确认就应写未确认。",
        "last_change": "姜守将袁客补充说明的追问范围压缩为三枚定向灵钉的时辰与去向，仍未获得有效答案。"
      },
      {
        "character_id": "jiang-shou",
        "fact_id": "yuan-ke-spirit-nail-statement",
        "state": "knows",
        "belief": "袁客口称自己临时拿过几枚定向灵钉周转，但没有填明数量、时辰、归还处；三枚缺口仍待其补正。",
        "last_change": "姜守记录袁客关于定向灵钉周转的含糊口头说法。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "array-command-error-cause",
        "state": "knows",
        "belief": "苏叶已淘汰姜守主动改写口令签的单一判断，不再相信姜守是该项口令签篡改者；她仍认为带伤校阵是另一项责任。",
        "last_change": "苏叶在见证单中正式将 command-slip-tamperer 原判断淘汰。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "direction-spirit-nail-gap",
        "state": "knows",
        "belief": "苏叶亲眼见证阵务柜领用簿与乙字现场登记相差三枚，未见对应领用登记。",
        "last_change": "苏叶知道三枚灵钉缺口客观存在。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "回声阵牌只会复述完整口令，不能回答是谁喊的、何时收到或是否与姜守改签有关。",
        "last_change": "苏叶亲自追问后得知回声阵牌只能复述口令，不能提供说话者、时辰或定责信息。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "jiang-shou-injury-violation-consequence",
        "state": "knows",
        "belief": "苏叶知道姜守未主动改写口令签不等于免除带伤私自校阵，禁令与后果仍不撤。",
        "last_change": "苏叶将改签判断与带伤违规后果分栏处理。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "jiang-shou-violation-witnessed",
        "state": "knows",
        "belief": "苏叶亲眼见到姜守在她口头阻止后仍接触运行阵眼，并造成伤势加重、多放木剑和镜损。",
        "last_change": "苏叶取得姜守新增违规及其后果的目击知识。"
      },
      {
        "character_id": "su-ye",
        "fact_id": "left-five-local-adjustment-effective",
        "state": "knows",
        "belief": "苏叶知道左五偏向已压回可接受刻度，且由她代操作、姜守仅口述。",
        "last_change": "苏叶通过亲自读数和代操作，知道左五偏向压回可接受刻度。"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "array-command-error-cause",
        "state": "knows",
        "belief": "闻岚已合并采信维护签入柜时辰、见证印、钉尾异常、磨痕拖向、三枚灵钉未登记缺口，并据此裁定这些事实足以排除姜守主动改写口令签这一单一判断，但不能判断谁移了灵钉，也不能免除姜守带伤违规。",
        "last_change": "闻岚对前期复验证据作出正式采信和边界裁定。"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "闻岚确认回声阵牌只能证明收到过完整口令，不能证明责任人、时辰，也不能单独定责。",
        "last_change": "闻岚正式限定回声阵牌证据效力。"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "left-five-local-adjustment-effective",
        "state": "knows",
        "belief": "闻岚确认左五停阵局部试调有效。",
        "last_change": "闻岚采信苏叶见证单后，确认左五停阵局部试调有效。"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "left-four-lag-persists",
        "state": "knows",
        "belief": "闻岚知道左四迟滞未清，因此不得启动整阵或完整口令复验，只能先拟停阵口令模拟方案并先处理左四。",
        "last_change": "闻岚据左四迟滞作出下一步流程裁定。"
      },
      {
        "character_id": "wen-lan",
        "fact_id": "spirit-nail-liability-boundary",
        "state": "knows",
        "belief": "闻岚只确认袁客三枚定向灵钉未登记借走，归还去向与时辰未明，其余短缺不作推定。",
        "last_change": "闻岚将袁客责任边界限定在三枚未登记借走，未扩展为长期短缺定责。"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing",
        "state": "knows",
        "belief": "袁客知道自己经手三枚定向灵钉且未登记，并已被迫写下姓名；但仍称具体归还去向不能确定。",
        "last_change": "袁客从含糊承认周转更新为已承认三枚由自己经手且未登记。"
      },
      {
        "character_id": "yuan-ke",
        "fact_id": "spirit-nail-borrowing-destination",
        "state": "conceals",
        "belief": "袁客承认三枚灵钉临时周转，但仍未交代清楚归还去向，并试图提及库中其余短缺。",
        "last_change": "袁客继续未说明三枚定向灵钉的具体归还去向。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "accident-form-chapter-0008-updates",
        "state": "knows",
        "belief": "赵矩事故表已补入左五局部试调有效、左四仍迟滞、姜守本次未越三尺禁线、未导灵、未触碰运行阵眼。",
        "last_change": "赵矩被要求并实际补写本章三类已核事实。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "accident-record-boundary",
        "state": "knows",
        "belief": "事故表已经写明三处相邻钉位的钉尾朝向与旧压痕不一致，灵纹磨痕拖向“追后三步”执行侧；该方向异常不得单独定责，必须与维护签拓印和定向灵钉领用时辰合并核验。",
        "last_change": "赵矩受同一事故表约束，将钉尾朝向、旧压痕和灵纹磨痕方向异常写入新增栏，并注明合并核验边界。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "accident-table-verified-boundaries",
        "state": "knows",
        "belief": "赵矩已在事故表补写核验边界：维护签不能单独定责，回声阵牌不能单独定责，三枚定向灵钉未登记缺口成立，姜守仍承担带伤违规责任，裂镜赔偿保留，阵堂小考资格继续冻结。",
        "last_change": "赵矩被迫在同一事故表内补写已核事实和仍保留的后果。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "array-command-error-cause",
        "state": "knows",
        "belief": "赵矩在事故表内承认维护签不能单独定责、三枚定向灵钉未登记缺口成立、姜守主动改写口令签的单一判断已被排除，同时姜守带伤违规责任继续保留。",
        "last_change": "赵矩被事故表约束，必须承认已核事实并保留姜守另一项违规责任。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "direction-spirit-nail-gap",
        "state": "knows",
        "belief": "赵矩已在事故表上记录三枚定向灵钉账面与现场登记不合，无对应领用登记，需核验。",
        "last_change": "赵矩正式知道并记录三枚定向灵钉缺口。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "echo-command-plate-limits",
        "state": "knows",
        "belief": "回声阵牌仅证明完整口令曾被收到，不记录说话者及收到时辰，不能单独定责。",
        "last_change": "赵矩将回声阵牌的证据边界写入事故表未核验栏。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "maintenance-rubbing-limited-proof",
        "state": "knows",
        "belief": "维护签拓印仅证明签押、维护项及存档时辰，不能单独定责口令改写。",
        "last_change": "赵矩在已核事实栏正式承认维护签拓印不能单独定责口令改写。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "maintenance-sign-not-sole-liability",
        "state": "knows",
        "belief": "赵矩已记录维护签不能单独定责，须合并灵纹、灵钉、现场记录核验。",
        "last_change": "赵矩正式记录维护签不能单独定责。"
      },
      {
        "character_id": "zhao-ju",
        "fact_id": "simulation-valid-but-not-qualification",
        "state": "knows",
        "belief": "停阵模拟有效且未启动完整剑阵符合方案，但阵堂小考资格仍冻结待验。",
        "last_change": "赵矩在事故表上承认停阵模拟的合规与有效，同时维持资格冻结。"
      }
    ]
  },
  "next_chapter_inputs": [
    "姜守仍为炼气二层，left-palm-burn 已解除。",
    "live-array-contact-ban 已失效，但姜守新增 two-day-complete-array-independent-start-ban：两日内不得独立启动完整剑阵，只能在监督下参与停阵或局部低强度校阵。",
    "乙字训练剑阵停阵复验通过，口令恢复正常；“后退三步，停剑”已验证为后退三步后停剑，无追加追行。",
    "姜守阵堂小考资格已由冻结改为带条件准入。",
    "小考条件包括裂镜赔偿排期、两日禁独立启动整阵、带伤校阵处分记录保留、监督下参与停阵或局部低强度校阵。",
    "校准镜仍裂损且不能恢复，裂镜赔偿排期需明日辰时签认。",
    "姜守 contribution-point 余额仍为6点，已扣2点不退还。",
    "苏叶已淘汰姜守主动改写口令签的单一判断，但仍会用安全条款约束姜守操作，并承担后续核对工时。",
    "赵矩已在事故表内承认维护签不能单独定责、三枚定向灵钉未登记缺口成立、姜守主动改写口令签的单一判断已被排除，同时保留姜守带伤违规责任。",
    "袁客只被确认三枚 direction-spirit-nail 未登记借走，归还去向与时辰未明；其余阵材短缺不作推定。"
  ],
  "deviations": [],
  "last_source_draft": "chapters/0010/draft.final.md",
  "last_source_sha256": "cbb4aa5f7fb4b6c673c95367e465a0bee9600dea6d732c01a3444cb858ec7797",
  "source": "chapters/0010/state-event.json"
}
```
