# 逐章正式状态事件

## 第 1 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0001",
  "chapter": 1,
  "source_draft": "chapters/0001/draft.final.md",
  "source_sha256": "b2e8b725e028477e9ba9aed8ded4ed3a615ccdf32e3ab2b2ea57b495000dd1ce",
  "entity_changes": [
    {
      "change": "外门候场弟子持有并传阅写有所谓安全雷时和站位的避雷黄历。",
      "source_evidence": "纸边被汗浸软，上头写着歪歪扭扭的字：辰时三刻半，东风铃二响，西南柱阴影内可避；巳初一响后退三步；值守廊不得停留三息以上，三息后雷不认人。"
    },
    {
      "change": "校雷铜铃曾被曹雨暂挂在值守廊西梁钩且第二道复位封签缺失。",
      "source_evidence": "纪凌策写下三项：铜铃曾暂挂值守廊西梁钩；第二道封签缺失；黄历节拍与低限校雷回声相似。"
    },
    {
      "change": "胡善交出《避雷黄历初校》抄本，抄本包含按回声和站位解释的避雷规则。",
      "source_evidence": "胡善忍痛似的交出最厚一本。封皮上写着《避雷黄历初校》，旁边还画了一个笑眯眯的铃。纪凌策翻开，见每条后头都配着站位：“廊口闻半响者不宜贪；西南闻二响者可小进；告示下三息为一小周天。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野被纪凌策要求暂停单独登记高风险雷时，只能在巡雷使可见范围内记录低限雷痕。",
      "state_id": "solo-high-risk-thunder-registration-suspension",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“我先按记录判断。”纪凌策看向他，“自此刻起，你暂停单独登记高风险雷时，只在我可见范围内记录低限雷痕。所有黄历抄本交出核验。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "injury",
      "change": "裴照野右手雷麻旧伤仍存在，但本章未加重也未减轻。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "裴照野看见了，没有分辩，只把雷痕先后、接地刻度、疑似回声角度逐项补入低限记录。右手旧麻仍伏在指节里，未重也未轻，他没有碰高压塔梯。"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策依据时刻簿、调度记录和裴照野当班登记位置，仍保留裴照野泄露安全雷时的嫌疑记录。",
      "supersedes_fact_ids": [],
      "change": "纪凌策没有更正对裴照野泄露安全雷时的误信，只将其作为未排除嫌疑继续记录。",
      "source_evidence": "纪凌策写下三项：铜铃曾暂挂值守廊西梁钩；第二道封签缺失；黄历节拍与低限校雷回声相似。他笔尖停了停，又另起一行：裴照野当班登记位置与黄历所列时段重合，泄露安全雷时嫌疑未排除。"
    },
    {
      "character_id": "pei-zhaoye",
      "fact_id": "shared-safe-window-origin",
      "state": "investigating",
      "belief": "裴照野认为黄历来源可能与校雷铜铃位置、雷痕先后和回声角度有关，而非同一路正式雷时泄露。",
      "supersedes_fact_ids": [],
      "change": "裴照野提出黄历抄录顺序与墙上雷痕方向相反，需核对铜铃位置和回声角度。",
      "source_evidence": "“黄历抄录顺序是西南先响、东柱后响。”他说，“墙上雷痕方向相反。东柱残纹在前，西南回纹在后。不是同一路正式雷时抄出。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "纪凌策知道校雷铜铃曾暂挂值守廊西梁钩，且第二道复位封签缺失。",
      "supersedes_fact_ids": [],
      "change": "纪凌策查问曹雨后确认暂挂说法和第二道封签缺失线索。",
      "source_evidence": "曹雨把铜铃换了个胳膊抱，像那铃忽然重了三倍：“当时赶低限校雷，想着先挂梁钩上避潮，随后便取下。第二道……许是补在工房。”"
    },
    {
      "character_id": "cao-yu",
      "fact_id": "unsealed-calibration-chime",
      "state": "knows",
      "belief": "曹雨知道自己曾把校雷铜铃暂挂值守廊，并且第二道复位封签还未补。",
      "supersedes_fact_ids": [
        "unsealed-calibration-chime"
      ],
      "change": "曹雨不再完全隐瞒未封校雷铜铃暂挂值守廊一事，在纪凌策面前承认第二道封签还未补。",
      "source_evidence": "曹雨低头翻袖袋，翻出一枚铜刷、一段旧绳、一张买灯油的欠条，唯独没有封签。他声音更低：“还未补。”"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "lucky-thunder-almanac-source",
      "state": "knows",
      "belief": "胡善知道自己抄过值守廊铜铃声并传给同组，但自称不知真实落雷时刻，只把告示和铃声误解成避雷门道。",
      "supersedes_fact_ids": [
        "lucky-thunder-almanac-source"
      ],
      "change": "胡善不再隐瞒抄录并传播铜铃声一事，但仍否认知道真实落雷时刻。",
      "source_evidence": "胡善蔫了：“承认抄过铃声，也传给同组。弟子不知真实落雷时刻，只以为塔中告示藏得深。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "hu-shan-copied-chime-echo",
      "state": "knows",
      "belief": "纪凌策知道胡善承认抄录并传播值守廊铜铃回声，但胡善不承认知道真实落雷时刻。",
      "supersedes_fact_ids": [],
      "change": "纪凌策获得胡善关于黄历传播来源的口供。",
      "source_evidence": "“从现在起，候场弟子按接地刻度排队，不按黄历。胡善，你承认抄录并传播铜铃回声？”\n\n胡善蔫了：“承认抄过铃声，也传给同组。弟子不知真实落雷时刻，只以为塔中告示藏得深。”"
    }
  ],
  "thread_changes": [
    {
      "change": "共享安全雷时外泄疑云公开化，黄历抄本被统一交出核验。",
      "source_evidence": "“我先按记录判断。”纪凌策看向他，“自此刻起，你暂停单独登记高风险雷时，只在我可见范围内记录低限雷痕。所有黄历抄本交出核验。”"
    },
    {
      "change": "听雷塔修复结论暂缓，后续需完成铜铃梁钩、回声节拍和雷痕证据链核对。",
      "source_evidence": "他看向塔身未校的四处接地脊，声音沉下去：“在证据链完成前，听雷塔不作修复结论，你也不得单独登记高风险雷时。”"
    },
    {
      "change": "胡善的抄本将被逐条比对回声节拍。",
      "source_evidence": "纪凌策收起时刻簿：“裴照野，接下来在我监督下补录值守廊雷痕。曹雨，带人确认此铃挂过的梁钩。胡善的抄本，逐条比对回声节拍。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善把安全告示曲解成押雷秘诀，形成后续可复用的误解笑点。",
      "source_evidence": "“巡雷使明鉴，”胡善拱手，“弟子只是把告示和铃声合参。告示说不得停留三息以上，可见三息以内尚有余地；三息以后雷不认人，此乃塔中慈悲，写得含蓄。”"
    },
    {
      "change": "裴照野以“耳朵无证，胆子有证”给乱写黄历者分组，形成查案中的冷面吐槽风格。",
      "source_evidence": "“为何另列？”胡善问。\n\n“耳朵无证，胆子有证。”"
    },
    {
      "change": "胡善继续把回声与黄历解释成秘格，被裴照野用站位打断。",
      "source_evidence": "胡善从后头探脑袋：“那便是黄历秘格。眼见为反，耳听为真，西南先占——”\n\n裴照野指向地面刻度：“你站在三尺外，秘格失效。”"
    }
  ],
  "new_constraints": [
    {
      "change": "候场弟子改为按接地刻度排队，不再按避雷黄历站位。",
      "source_evidence": "纪凌策把抄本合上：“从现在起，候场弟子按接地刻度排队，不按黄历。胡善，你承认抄录并传播铜铃回声？”"
    },
    {
      "change": "裴照野接下来必须在纪凌策监督下补录值守廊雷痕。",
      "source_evidence": "纪凌策收起时刻簿：“裴照野，接下来在我监督下补录值守廊雷痕。曹雨，带人确认此铃挂过的梁钩。胡善的抄本，逐条比对回声节拍。”"
    },
    {
      "change": "曹雨需要带人确认校雷铜铃挂过的梁钩。",
      "source_evidence": "纪凌策收起时刻簿：“裴照野，接下来在我监督下补录值守廊雷痕。曹雨，带人确认此铃挂过的梁钩。胡善的抄本，逐条比对回声节拍。”"
    },
    {
      "change": "证据链完成前，听雷塔不作修复结论。",
      "source_evidence": "他看向塔身未校的四处接地脊，声音沉下去：“在证据链完成前，听雷塔不作修复结论，你也不得单独登记高风险雷时。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "纪凌策仍保留 pei-leaked-strike-window 误信：裴照野当班登记位置与黄历所列时段重合，泄露安全雷时嫌疑未排除。",
    "裴照野提出黄历抄录顺序与墙上雷痕方向相反，需核对铜铃位置、梁钩位置和回声角度。",
    "曹雨承认校雷铜铃只是“暂挂”过值守廊，且第二道复位封签还未补。",
    "胡善承认抄过值守廊铜铃声并传给同组，但否认知道真实落雷时刻。",
    "裴照野被暂停单独登记高风险雷时，只能在纪凌策可见范围内记录低限雷痕。",
    "裴照野 right-hand-thunder-numbness 仍活动，未加重、未恢复、未解除。",
    "资源未动：裴照野下品灵石 5 枚、定雷符 3 张；听雷塔重置钉 2 枚、导雷铜条 6 段。",
    "听雷塔四处接地脊未校，修复结论未作出。"
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
  "source_sha256": "ffa920d4aaf83af1941b5e82e185c57713986e4c4d4f0a2edfc597fe8b86d53b",
  "entity_changes": [
    {
      "change": "校雷铜铃未封期间曾挂在值守廊偏东第三根梁下旧钩，离东墙约四尺。‘暂挂’不能替代封签。",
      "source_evidence": "片刻后，曹雨指向偏东那根梁：“第三根梁下的旧钩。离东墙约四尺。”\n\n“为何挂那里？”\n\n“铃架漆未干，检修间又在搬铜料。我想着只挂半日。”\n\n“未封器物进入值守廊，半日也有回声。”沈络道，“‘暂挂’说明时长，不改变位置，也不替代封签。”"
    },
    {
      "change": "听雷塔东、西两处接地脊回声异常成立，南、北暂不能判定完好。",
      "source_evidence": "纪凌策复看裴照野的标位，又亲自以低强度灵识扫过，不作引雷，只核对回声方向。\n\n“东、西两处异常成立。南、北暂不能判定完好。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "胡善被沈络调整为远端回声样本，不得参与站位解释。",
      "source_evidence": "沈络在风险表上添了一行：“黄历传播者改为远端回声样本。不得参与站位解释。”"
    },
    {
      "change": "下一次低限试雷由纪凌策在场复核，曹雨只控铃，裴照野负责辨序且受右手限制。",
      "source_evidence": "“谁操作？”\n\n“裴照野辨序，我控铃。”曹雨答。\n\n“谁复核？”\n\n纪凌策道：“我在场。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "injury",
      "change": "裴照野右手雷麻旧伤仍未解除，状态未加重也未恢复。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络看向裴照野的右手：“旧伤何时发作？”\n\n“接触高压雷纹时。指节麻，符笔偏。”\n\n“今日状态？”\n\n“旧伤。未加重，未恢复。”\n\n“是否取出铜刺、用定雷符、完成低负荷抄录复核？”\n\n“没有。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野仍不得独自登高压塔，且不得借查证扩大试雷强度。",
      "state_id": "solo-high-voltage-tower-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络将右手雷麻写入操作风险：“那就仍按未解除处理。不得独自登高压塔，不得借查证扩大试雷强度。你漏封铜铃与提前试雷的程序责任，也不因提出铜铃线索而撤销。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野在检修沟内只能读残痕，不得注灵试压。",
      "state_id": "solo-high-risk-thunder-registration-suspension",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "纪凌策先在沟口布下监督线：“裴照野只读残痕，不注灵试压。曹雨报链号。沈络记录接触时长。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "ability",
      "change": "裴照野在监督下使用雷痕辨序发现东、西两处接地脊回声滞后，但仅凭残痕不能定是链扣错位还是脊端错序。",
      "state_id": "thunder-mark-sequencing",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“西脊也滞后。一处半拍，一处至少一拍。仅凭残痕，不能定是链扣错位还是脊端错序。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "cao-yu",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "曹雨知道未封校雷铜铃曾暂挂在值守廊偏东第三根梁下旧钩，离东墙约四尺，且暂挂不能替代封签。",
      "supersedes_fact_ids": [
        "unsealed-calibration-chime"
      ],
      "change": "曹雨明确指出未封校雷铜铃的具体暂挂位置，并接受其封签责任。",
      "source_evidence": "片刻后，曹雨指向偏东那根梁：“第三根梁下的旧钩。离东墙约四尺。”\n\n“为何挂那里？”\n\n“铃架漆未干，检修间又在搬铜料。我想着只挂半日。”\n\n“未封器物进入值守廊，半日也有回声。”沈络道，“‘暂挂’说明时长，不改变位置，也不替代封签。”\n\n曹雨没再辩。"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "沈络确认未封校雷铜铃曾挂在值守廊偏东梁钩，且未封器物进入值守廊会造成回声风险，暂挂不替代封签。",
      "supersedes_fact_ids": [],
      "change": "沈络将未封铜铃位置和封签责任纳入复核。",
      "source_evidence": "“未封器物进入值守廊，半日也有回声。”沈络道，“‘暂挂’说明时长，不改变位置，也不替代封签。”"
    },
    {
      "character_id": "pei-zhaoye",
      "fact_id": "shared-safe-window-origin",
      "state": "knows",
      "belief": "裴照野确认避雷黄历来源是校雷铜铃回声节拍，不是后续随机天雷时刻。",
      "supersedes_fact_ids": [
        "shared-safe-window-origin"
      ],
      "change": "裴照野对黄历来源的调查从怀疑转为确认。",
      "source_evidence": "裴照野道：“抄的是铃声。不是天雷。”"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "lucky-thunder-almanac-source",
      "state": "knows",
      "belief": "胡善被现场比对证明其避雷黄历不是预知随机落雷，只是把校验节拍写成押时秘诀；两次避开落雷属于偶合。",
      "supersedes_fact_ids": [
        "lucky-thunder-almanac-source"
      ],
      "change": "胡善的避雷黄历被确认并非真正预知雷击。",
      "source_evidence": "沈络问胡善：“你知道后续落雷时刻吗？”\n\n“不知道。”\n\n“那两次避开，是偶合。你把校验节拍写成押时秘诀，诱使候场弟子按所谓吉位停留，增加聚集风险。记管理责任，人数待核。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "hu-shan-copied-chime-echo",
      "state": "knows",
      "belief": "纪凌策通过黄历、试雷记录和真实雷雨记录比对，确认黄历所抄主要对应低限试雷铜铃节拍而非随机落雷。",
      "supersedes_fact_ids": [
        "hu-shan-copied-chime-echo"
      ],
      "change": "纪凌策完成对胡善黄历来源的当场比对。",
      "source_evidence": "纪凌策逐页展开，又从时刻簿中抽出前三次低限试雷记录。他先对年月，再对铜铃维护册，最后将黄历上那些被圈作“宜出门”的时刻逐个压在试雷节拍下。"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策仍因裴照野当班、调度记录缺口和第二道封签缺失，未正式更正裴照野泄露安全雷时的判断。",
      "supersedes_fact_ids": [],
      "change": "纪凌策保留对裴照野泄露安全雷时的误信，同时把铜铃位置和回声角度列入核查。",
      "source_evidence": "纪凌策在核查单上添入“铜铃偏东梁钩”“铃口朝向”“候场区回声范围”三项，却没有划去裴照野名下的嫌疑。\n\n“时刻簿显示，黄历首批节拍出现时，裴照野正在当班。调度记录也没有第二条正式调用。曹雨所说的挂铃时刻，仍缺第二道封签佐证。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "temporary-thunder-clerk-qualification",
      "state": "investigating",
      "belief": "沈络已把裴照野右手旧伤、漏封铜铃和提前试雷程序责任纳入临时登记资格复核，且不因他提出铜铃线索而撤销责任。",
      "supersedes_fact_ids": [
        "temporary-thunder-clerk-qualification"
      ],
      "change": "沈络对裴照野资格复核新增旧伤操作风险和程序责任记录。",
      "source_evidence": "沈络将右手雷麻写入操作风险：“那就仍按未解除处理。不得独自登高压塔，不得借查证扩大试雷强度。你漏封铜铃与提前试雷的程序责任，也不因提出铜铃线索而撤销。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "grounding-ridge-echo-delay",
      "state": "knows",
      "belief": "纪凌策确认听雷塔东、西两处接地脊回声异常成立，南、北暂不能判定完好。",
      "supersedes_fact_ids": [],
      "change": "纪凌策复核裴照野标位后确认东、西两处异常。",
      "source_evidence": "纪凌策复看裴照野的标位，又亲自以低强度灵识扫过，不作引雷，只核对回声方向。\n\n“东、西两处异常成立。南、北暂不能判定完好。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "low-limit-test-thunder-procedure",
      "state": "knows",
      "belief": "沈络批准下一章仅可进行低限一刻试雷，须纪凌策在场复核，storm-reset-pin 预备待命但不得提前启用，启用后永久消耗。",
      "supersedes_fact_ids": [],
      "change": "沈络正式限定下一次试雷程序和重置钉启用条件。",
      "source_evidence": "沈络看过编号：“两枚，只能预备一枚待命。本次不得提前启用。若接地链失序，是否启用由纪凌策当场判断。重置钉入阵即永久消耗，不返还，不补记成暂借。”"
    }
  ],
  "thread_changes": [
    {
      "change": "听雷塔修复仍未完成，下一步只能通过低限试雷确认接地链错序范围。",
      "source_evidence": "“东、西两处异常成立。南、北暂不能判定完好。”\n\n曹雨问：“那便做一次低限试雷？”"
    },
    {
      "change": "裴照野泄露安全雷时的嫌疑线未正式更正，继续受封签时间缺口影响。",
      "source_evidence": "“列入核查，不等于完成证明。”纪凌策合上簿册，“在封签时间缺口补齐前，泄露安全雷时的判断不正式更正。”"
    },
    {
      "change": "胡善黄历传播责任被记录，传播人数仍待核。",
      "source_evidence": "“那两次避开，是偶合。你把校验节拍写成押时秘诀，诱使候场弟子按所谓吉位停留，增加聚集风险。记管理责任，人数待核。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善试图把复核要点包装成新的吉位黄历，被纪凌策当场制止。",
      "source_evidence": "纪凌策按住纸角：“你抄什么？”\n\n“复核要点。”\n\n“题头为何是‘新订东廊吉位’？”\n\n“便于记忆。”\n\n纪凌策收走空纸，指向院墙最远处一张矮桌：“你去远端抄录席。只记听见几响、相隔几息，不许加吉凶。”"
    },
    {
      "change": "胡善从避雷黄历传播者变成了自己黄历的反证样本。",
      "source_evidence": "胡善只得坐回矮桌，成了自己那本黄历的反证。"
    },
    {
      "change": "曹雨对“暂借”重置钉的念头被沈络规则堵死后闭嘴。",
      "source_evidence": "曹雨的目光在“暂借”二字上停了停，识趣地闭嘴。"
    }
  ],
  "new_constraints": [
    {
      "change": "下一章低限试雷仅允许低限一刻，不得上调。",
      "source_evidence": "沈络又问：“试雷强度？”\n\n“低限一刻。”纪凌策道。\n\n“不得上调。裴照野右手不得持续接触高压雷纹，符笔偏移即停。曹雨只控校雷铜铃，不得改接地链。试雷前复核封签、清空候场廊、核对远端抄录席。”"
    },
    {
      "change": "下一次低限试雷必须由纪凌策在场复核。",
      "source_evidence": "纪凌策接过试雷令，在复核人一栏签名：“明日低限试雷，我在场。”"
    },
    {
      "change": "storm-reset-pin 两枚余额不变，其中一枚移入待命槽；不得提前启用，启用将永久消耗。",
      "source_evidence": "沈络看过编号：“两枚，只能预备一枚待命。本次不得提前启用。若接地链失序，是否启用由纪凌策当场判断。重置钉入阵即永久消耗，不返还，不补记成暂借。”"
    },
    {
      "change": "下一次试雷前必须复核封签、清空候场廊、核对远端抄录席。",
      "source_evidence": "“不得上调。裴照野右手不得持续接触高压雷纹，符笔偏移即停。曹雨只控校雷铜铃，不得改接地链。试雷前复核封签、清空候场廊、核对远端抄录席。”"
    },
    {
      "change": "曹雨下一次试雷只可控制校雷铜铃，不得改接地链。",
      "source_evidence": "“不得上调。裴照野右手不得持续接触高压雷纹，符笔偏移即停。曹雨只控校雷铜铃，不得改接地链。试雷前复核封签、清空候场廊、核对远端抄录席。”"
    },
    {
      "change": "胡善作为黄历传播者被改为远端回声样本，不得参与站位解释。",
      "source_evidence": "沈络在风险表上添了一行：“黄历传播者改为远端回声样本。不得参与站位解释。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "沈络已介入安全复核，候场停留、未封铜铃、右手旧伤和低限试雷程序均进入正式记录。",
    "曹雨已明确未封校雷铜铃曾挂在值守廊偏东第三根梁下旧钩，离东墙约四尺；该位置会把低限试雷节拍折入候场区。",
    "胡善的避雷黄历已被确认抄的是铜铃回声节拍，不是后续随机落雷时刻；传播管理责任已记，人数待核。",
    "纪凌策仍未正式更正 pei-leaked-strike-window，只把铜铃偏东梁钩、铃口朝向、候场区回声范围列入核查。",
    "裴照野在监督下发现东、西两处接地脊回声滞后；南、北暂不能判定完好，需低限试雷确认错序范围。",
    "下一章试雷限定为低限一刻，纪凌策在场复核，沈络备案，试雷前复核封签、清空候场廊、核对远端抄录席。",
    "storm-reset-pin 仍为 2 枚，其中一枚移入待命槽；不得提前启用，若启用将永久消耗。",
    "裴照野 right-hand-thunder-numbness 仍未解除，未加重、未恢复；右手不得持续接触高压雷纹，符笔偏移即停。",
    "资源余额保持：裴照野下品灵石 5 枚、定雷符 3 张；听雷塔 storm-reset-pin 2 枚、conductive-copper-strip 6 段。",
    "听雷塔仍未修复，四处接地脊仍未完成校准。"
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
  "source_sha256": "ecdb5d6aa798eefce967ead4f42b0fd22b3fc2b2b02882bf9a1767e175c990d2",
  "entity_changes": [
    {
      "change": "听雷塔低限试雷出现错序反卷，主塔未修复，四处接地脊未校准。",
      "source_evidence": "纪凌策封闭试雷阵枢，又在时刻簿上补录：“本次试雷未提高强度。确认东、西两处接地脊先后倒置，并存在反卷牵连。主塔未修复，四脊未校准。”"
    },
    {
      "change": "曹雨未封校雷铜铃偏东梁钩位置与回声角度再次被验证，但封签时间仍待核。",
      "source_evidence": "铜铃先接主链节拍，回声沿铃口朝向折入值守廊，恰与胡善抄本上最早几页的间隔相合。\n\n“位置成立。”沈络道，“角度成立到值守廊。封签时间仍待核。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "ability",
      "change": "裴照野在低限试雷中用雷痕辨序确认东、西两处接地脊先后倒置，并指出链扣间牵连。",
      "state_id": "thunder-mark-sequencing",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "裴照野放低符笔：“东、西两脊次序倒置。链扣间有牵连。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "injury",
      "change": "裴照野右手雷麻旧伤加重，表现为指节颤动、符笔落点偏移。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络按住记录页，不让他继续：“右手雷麻加重。症状，指节颤动，符笔落点偏移。自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。后续先处理伤势风险。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "沈络新增限制：裴照野不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。",
      "state_id": "solo-high-voltage-thunder-pattern-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络按住记录页，不让他继续：“右手雷麻加重。症状，指节颤动，符笔落点偏移。自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。后续先处理伤势风险。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "thunder-tower",
      "resource_id": "storm-reset-pin",
      "operation": "consume",
      "amount": 1,
      "unit": "枚",
      "resulting_balance": 1,
      "source_or_destination": "阻断低限试雷错序引发的接地链反卷",
      "change": "听雷塔启用并永久消耗 1 枚 storm-reset-pin，余额从 2 枚降为 1 枚。",
      "source_evidence": "“原有两枚，永久消耗一枚，余额一枚。”沈络当场记入安全复核簿，“用途：阻断低限试雷错序引发的接地链反卷。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "grounding-ridge-echo-delay",
      "state": "knows",
      "belief": "纪凌策确认东、西两处接地脊存在先后倒置，并存在反卷牵连；主塔未修复，四脊未校准。",
      "supersedes_fact_ids": [
        "grounding-ridge-echo-delay"
      ],
      "change": "纪凌策从上一章的回声滞后待判定更新为确认东、西两处接地脊先后倒置并存在反卷牵连。",
      "source_evidence": "纪凌策封闭试雷阵枢，又在时刻簿上补录：“本次试雷未提高强度。确认东、西两处接地脊先后倒置，并存在反卷牵连。主塔未修复，四脊未校准。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策仍认为目前证据不足以更正裴照野泄露安全雷时的判断。",
      "supersedes_fact_ids": [],
      "change": "纪凌策维持对裴照野泄露安全雷时的误信，未正式更正。",
      "source_evidence": "“铜铃位置与回声角度继续核查。封签时间另查。错序雷痕另查。”他合上时刻簿，“目前证据不足以更正裴照野泄露安全雷时的判断。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "investigating",
      "belief": "纪凌策承认铜铃位置与回声角度需要继续核查，封签时间和错序雷痕也要另查。",
      "supersedes_fact_ids": [],
      "change": "纪凌策未把铜铃线索用于更正泄露判断，只将铜铃位置、回声角度、封签时间、错序雷痕继续列为核查内容。",
      "source_evidence": "“铜铃位置与回声角度继续核查。封签时间另查。错序雷痕另查。”他合上时刻簿，“目前证据不足以更正裴照野泄露安全雷时的判断。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "temporary-thunder-clerk-qualification",
      "state": "investigating",
      "belief": "沈络将重置钉消耗、旧伤加重、提前试雷程序风险和禁止裴照野独自接触高压雷纹纳入安全复核，既有程序责任不抵扣。",
      "supersedes_fact_ids": [
        "temporary-thunder-clerk-qualification"
      ],
      "change": "沈络的临时登记资格复核更新为包含本次低限试雷后果、伤势加重和新的接触限制，且不抵扣此前责任。",
      "source_evidence": "沈络把另一份记录推到他面前：“提前试雷的既有程序风险也继续保留。今日受监督试雷，不抵扣此前责任。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "沈络确认校雷铜铃的非正式悬位实际参与回声传递，第二道封签缺失。",
      "supersedes_fact_ids": [
        "unsealed-calibration-chime-at-duty-corridor"
      ],
      "change": "沈络将曹雨所称暂挂的铜铃记录为实际参与回声传递且缺失第二道封签。",
      "source_evidence": "沈络在簿上写道：“非正式悬位，实际参与回声传递。第二道封签缺失。”"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "lucky-thunder-almanac-source",
      "state": "knows",
      "belief": "胡善被当场告知他避雷黄历中准的是铜铃响过，而不是正式雷时或宜忌。",
      "supersedes_fact_ids": [
        "lucky-thunder-almanac-source"
      ],
      "change": "胡善的黄历来源被进一步压实为铜铃回声节拍，他本人被禁止添宜忌。",
      "source_evidence": "胡善隔着两道线道：“那上面有三处很准。”\n\n纪凌策道：“准的是铜铃响过。”\n\n胡善闭嘴了。"
    },
    {
      "character_id": "cao-yu",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "曹雨知道校雷铜铃当时挂在偏东第三根梁的旧钩，铃口朝西南，未补第二道封签，并且下一次核查要带封签簿与铜铃维护记录说明缺失原因。",
      "supersedes_fact_ids": [
        "unsealed-calibration-chime-at-duty-corridor"
      ],
      "change": "曹雨对未封铜铃位置与第二道封签缺失责任的知情状态更新为需提交封签簿和维护记录说明。",
      "source_evidence": "沈络抬笔，在复核簿末尾添了一行：“曹雨，下一次核查带封签簿与铜铃维护记录。说明第二道封签为何缺失。”"
    }
  ],
  "thread_changes": [
    {
      "change": "听雷塔修复线进入低压隔离、查明两脊断点、再定铜条修补方案阶段。",
      "source_evidence": "纪凌策封上停试签：“下一步先做低压隔离，查明两脊断点，再定铜条修补方案。剩余重置钉只有一枚，不得再靠试错。”"
    },
    {
      "change": "铜铃证据链尚未完整，仍需核查封签时间、错序雷痕和回声角度。",
      "source_evidence": "“铜铃位置与回声角度继续核查。封签时间另查。错序雷痕另查。”他合上时刻簿，“目前证据不足以更正裴照野泄露安全雷时的判断。”"
    },
    {
      "change": "胡善避雷黄历只允许作为节拍对照，不作为雷时记录。",
      "source_evidence": "纪凌策检查远端抄录席，又把胡善的黄历抄本翻到最早一页，搁在时刻簿旁。\n\n“此册只作节拍对照，不作雷时记录。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善继续把候场分组线误当避雷黄历用途，被裴照野纠正。",
      "source_evidence": "胡善抬头：“我知道。我的意思是，站在线后，东时避东，西时——”\n\n“分两组。不是黄历。”"
    },
    {
      "change": "胡善被要求只抄节拍不许添宜忌，黄历式记录被沈络纳入传播未核雷时风险。",
      "source_evidence": "裴照野将他的抄本抽走，压在远端抄录席上：“你去第二组，离铜铃回声最远。只抄听见的节拍，不许添宜忌。”\n\n胡善望着被没收的册子，迟疑道：“若恰好又对了一次呢？”\n\n沈络翻开安全复核簿：“就多记一次你传播未核雷时。”"
    }
  ],
  "new_constraints": [
    {
      "change": "裴照野自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。",
      "source_evidence": "沈络按住记录页，不让他继续：“右手雷麻加重。症状，指节颤动，符笔落点偏移。自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。后续先处理伤势风险。”"
    },
    {
      "change": "剩余 storm-reset-pin 只有 1 枚，不得再靠试错。",
      "source_evidence": "纪凌策封上停试签：“下一步先做低压隔离，查明两脊断点，再定铜条修补方案。剩余重置钉只有一枚，不得再靠试错。”"
    },
    {
      "change": "曹雨下一次核查必须带封签簿与铜铃维护记录说明第二道封签缺失原因。",
      "source_evidence": "沈络抬笔，在复核簿末尾添了一行：“曹雨，下一次核查带封签簿与铜铃维护记录。说明第二道封签为何缺失。”"
    },
    {
      "change": "提前试雷的既有程序风险继续保留，今日受监督试雷不抵扣此前责任。",
      "source_evidence": "沈络把另一份记录推到他面前：“提前试雷的既有程序风险也继续保留。今日受监督试雷，不抵扣此前责任。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "低限试雷已发生错序和接地链反卷；听雷塔启用并永久消耗 1 枚 storm-reset-pin，余额为 1 枚。",
    "听雷塔主塔未修复，四处接地脊未校准；已确认东、西两处接地脊先后倒置并存在反卷牵连。",
    "裴照野仍为炼气五层，未突破；right-hand-thunder-numbness 加重为指节颤动、符笔落点偏移。",
    "沈络已限制裴照野不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。",
    "纪凌策仍未正式更正 pei-leaked-strike-window，认为目前证据不足以更正裴照野泄露安全雷时的判断。",
    "铜铃偏东梁钩位置与回声角度已被试雷回声再次验证，但封签时间、错序雷痕和完整回声证据链仍需继续核查。",
    "曹雨下一次核查需带封签簿与铜铃维护记录，说明第二道封签为何缺失。",
    "胡善的避雷黄历继续只作铜铃节拍对照，不作雷时记录；传播未核雷时责任尚未处置完毕。",
    "下一步修塔需先做低压隔离，查明两脊断点，再定铜条修补方案；剩余重置钉只有一枚，不得再靠试错。",
    "资源余额：裴照野下品灵石 5 枚、定雷符 3 张；听雷塔 storm-reset-pin 1 枚、conductive-copper-strip 6 段。"
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
  "source_sha256": "85f984c41ff507b1186d88fc8ef7c7653ee78e6c94a5c2cc9b0c7437368a9f4c",
  "entity_changes": [
    {
      "change": "曹雨提交的铜铃维护记录明确未封校雷铜铃曾于申时一刻至酉时正暂挂在值守廊偏东东三梁钩，且第二道封签缺失。",
      "source_evidence": "纪凌策写下这七字，又补记：未封校雷铜铃自申时一刻至酉时正，暂挂值守廊偏东东三梁钩。"
    },
    {
      "change": "胡善提交的避雷黄历抄本来源被明确为铜铃回声，不是正式巡雷记录。",
      "source_evidence": "“黄历来源？”\n\n“铜铃回声。”\n\n“是否经正式巡雷记录核验？”\n\n“没有。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "低负荷抄录流程中，裴照野负责口述雷痕方向与刻度，纪凌策负责代笔和分栏复核。",
      "source_evidence": "沈络把符笔从他右手下抽走，放到纪凌策面前：“你代笔。他口述。原始时刻簿与现场残痕分栏，不准拿一项覆盖另一项。”"
    },
    {
      "change": "次日低压隔离检修分工确定：裴照野只口述刻度，纪凌策复核，曹雨带铜条量尺，胡善带传播名册且不带黄历。",
      "source_evidence": "沈络收起复核页：“明日先封主链，做低压隔离。裴照野只口述刻度，纪凌策复核。曹雨带铜条量尺。胡善带传播名册，不带黄历。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "沈络正式收紧裴照野接触高压雷纹的资格，要求其停止接触高压雷纹，只准低负荷抄录、口述方向与刻度，并禁止执符笔探痕和注灵复验。",
      "state_id": "solo-high-voltage-thunder-pattern-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "“停止接触高压雷纹。”沈络道，“从现在起，只准低负荷抄录、口述方向与刻度。不得执符笔探痕，不得注灵复验。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "injury",
      "change": "裴照野的右手雷麻仍处于加重状态，表现为右手指节颤动、掌侧旧伤青紫、细微雷意沿筋脉跳动。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "裴照野指节仍在颤。掌侧旧伤处泛着青紫，细微雷意沿筋脉一跳一跳，像有根看不见的铜丝埋在皮下。"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "recovery",
      "change": "裴照野右手雷麻进入恢复流程第一步：停止高压接触；但尚未部分恢复，也不得解除限制。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "沈络又在旁添了一行：“右手雷麻仍属加重状态。停止高压接触，仅为恢复流程第一步。未见部分恢复，不得解除限制。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "ability",
      "change": "裴照野在低负荷状态下继续使用雷痕辨序，能口述错序雷痕的方向、落雷次序和接地刻度，但仍不能确定动机。",
      "state_id": "thunder-mark-sequencing",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "裴照野道：“再记。东脊第四扣，接地刻度少半格。西脊第二扣，多一格。反卷从西入东。”\n\n“能确定是器物错序，不是你落笔错记？”\n\n“能确定方向。不能确定动机。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "grounding-ridge-echo-delay",
      "state": "knows",
      "belief": "纪凌策确认低限试雷中时刻簿记录的调用顺序与残痕显示的实际导行顺序不一致，时刻簿不足以单独解释错序雷痕。",
      "supersedes_fact_ids": [
        "grounding-ridge-echo-delay"
      ],
      "change": "纪凌策纠正了只依赖时刻簿判断试雷顺序的旧认知，确认必须区分调用顺序与实际导行顺序。",
      "source_evidence": "“时刻簿记录调用顺序。”纪凌策道，“残痕记录实际导行顺序。两者不一致。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "investigating",
      "belief": "纪凌策将铜铃位置、雷痕先后、封签时间和回声角度列为合并核查材料，但现阶段仍不足以更正泄露判断。",
      "supersedes_fact_ids": [],
      "change": "纪凌策的核查证据项更新为铜铃位置、雷痕先后、封签时间、回声角度四项合并核查。",
      "source_evidence": "纪凌策把四项材料列在同页：铜铃位置、雷痕先后、封签时间、回声角度。\n\n“合并核查。”他说，“现阶段仍不足以更正泄露判断。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策仍认为现有证据不足以更正裴照野泄露安全雷时的核查结论。",
      "supersedes_fact_ids": [],
      "change": "纪凌策没有正式更正裴照野泄露安全雷时的判断。",
      "source_evidence": "他随后看向裴照野：“此项只纠正试雷顺序判断，不足以更正泄露安全雷时的核查结论。”"
    },
    {
      "character_id": "cao-yu",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "曹雨知道维护册显示第二道封签缺失，且格式申诉不能改变梁钩位置或补出第二道封签。",
      "supersedes_fact_ids": [],
      "change": "曹雨已面对第二道封签缺失和偏东梁钩暂挂记录，但责任处置尚未完成。",
      "source_evidence": "沈络又道：“格式不改变梁钩位置，也不补出第二道封签。”\n\n曹雨的神色重新落了回去。"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "lucky-thunder-almanac-source",
      "state": "knows",
      "belief": "胡善承认避雷黄历来源是铜铃回声，不能预测后续随机雷，且没有经过正式巡雷记录核验。",
      "supersedes_fact_ids": [
        "lucky-thunder-almanac-source"
      ],
      "change": "胡善旧有“黄历能押后续随机雷”的认知被随机空响和复核事实纠正。",
      "source_evidence": "沈络问：“这算什么？”\n\n胡善小声道：“随机空响。”\n\n“能押后续随机雷？”\n\n“不能。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "temporary-thunder-clerk-qualification",
      "state": "investigating",
      "belief": "沈络将裴照野右手雷麻加重后的高压接触限制、低负荷抄录流程和未解除限制纳入临时登记资格复核。",
      "supersedes_fact_ids": [],
      "change": "沈络确认停止高压接触只是恢复流程第一步，裴照野的限制仍有效。",
      "source_evidence": "沈络又在旁添了一行：“右手雷麻仍属加重状态。停止高压接触，仅为恢复流程第一步。未见部分恢复，不得解除限制。”"
    }
  ],
  "thread_changes": [
    {
      "change": "听雷塔检修方向确定为先低压隔离，东脊第四扣和西脊第二扣需要导雷铜条修补，南北两脊只先做低压查验。",
      "source_evidence": "裴照野铺开四脊简图，以左手压尺，逐处口述：“东脊第四扣，西脊第二扣，先隔离。两处都需导雷铜条修补。南、北两脊只做低压查验，未查明前不定用量。”"
    },
    {
      "change": "听雷塔检修架已为东、西两脊挂上隔离牌，但铜条去向仍未填写，修补和校准尚未完成。",
      "source_evidence": "廊外云层缓缓压低。纪凌策将东、西两脊的隔离牌挂上检修架，最下方留着两处尚未填写的铜条去向。"
    },
    {
      "change": "下一步优先检查西脊第二扣，因裴照野判断反卷从那里起；西脊沟内出现细小金属绷响，提示隐患仍在。",
      "source_evidence": "裴照野看了一眼：“明日先开西脊第二扣。反卷从那里起。”\n\n检修架后，封闭的西脊沟内忽然传来一声细小的金属绷响。"
    },
    {
      "change": "曹雨的铜铃暂挂和第二道封签缺失仍造成管理责任风险，申诉格式不能消除事实后果。",
      "source_evidence": "沈络道：“位置有回声后果，时长有传播后果。自然记。”"
    },
    {
      "change": "胡善需要列出避雷黄历传播范围，传播管理责任尚未处置完成。",
      "source_evidence": "沈络指向候场登记栏：“把抄过、看过、按此换过候场位置的人名列出。不是新天机，是传播范围。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "裴照野把字写偏到责任人栏，形成本章申诉格式搞笑点。",
      "source_evidence": "纸上“东脊二刻”四字，最后一笔偏出去半寸，正好戳进“责任人”一栏。"
    },
    {
      "change": "胡善面对随机空响无法继续用黄历解释后续落雷，喜剧性地被迫承认不能预测。",
      "source_evidence": "胡善等了三息。\n\n天上很给面子地一片安静。"
    },
    {
      "change": "候场弟子按是否看过黄历、是否依黄历换位分组，胡善作为原抄人被单独归类，强化黄历传播笑点。",
      "source_evidence": "几名候场弟子原本还想问空响能否另开一页，闻言只得分成两组：看过黄历的站西栏，依黄历换过值守位置的站东栏。胡善站在两栏中间，抱着抄本，一时不知自己该归哪边。"
    }
  ],
  "new_constraints": [
    {
      "change": "裴照野不得接触高压雷纹，不得执符笔探痕，不得注灵复验，只准低负荷抄录和口述方向与刻度。",
      "source_evidence": "“停止接触高压雷纹。”沈络道，“从现在起，只准低负荷抄录、口述方向与刻度。不得执符笔探痕，不得注灵复验。”"
    },
    {
      "change": "右手雷麻尚未部分恢复或解除，停止高压接触仅是恢复流程第一步。",
      "source_evidence": "沈络又在旁添了一行：“右手雷麻仍属加重状态。停止高压接触，仅为恢复流程第一步。未见部分恢复，不得解除限制。”"
    },
    {
      "change": "听雷塔剩余一枚重置钉不得用于试错。",
      "source_evidence": "“重置钉一枚。”沈络道，“不得用于试错。”"
    },
    {
      "change": "塔库现有 conductive-copper-strip 六段，本章不领用，待断点确认后才能登记去向。",
      "source_evidence": "纪凌策在东、西两脊上各画一道红线：“塔库现有导雷铜条六段，本章不领用。待断点确认后再登记去向。”"
    },
    {
      "change": "次日修塔必须先封主链并做低压隔离。",
      "source_evidence": "沈络收起复核页：“明日先封主链，做低压隔离。裴照野只口述刻度，纪凌策复核。曹雨带铜条量尺。胡善带传播名册，不带黄历。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "裴照野仍为炼气五层，未突破；right-hand-thunder-numbness 仍属加重状态，停止高压接触只是恢复流程第一步，未见部分恢复，不得解除限制。",
    "沈络已正式限制裴照野停止接触高压雷纹，只准低负荷抄录、口述方向与刻度；不得执符笔探痕，不得注灵复验。",
    "低负荷复核中，裴照野确认错序雷痕方向与接地刻度：主塔北偏东落点三刻，西脊回卷逆行二刻半，东脊先受牵引后被西脊反卷；东脊第四扣少半格，西脊第二扣多一格，反卷从西入东。",
    "纪凌策已确认时刻簿记录调用顺序、残痕记录实际导行顺序，两者不一致；时刻簿不足以单独解释错序雷痕。",
    "纪凌策仍未正式更正 pei-leaked-strike-window，现阶段仍认为不足以更正泄露判断。",
    "曹雨的铜铃维护记录显示未封校雷铜铃自申时一刻至酉时正暂挂值守廊偏东东三梁钩，第二道封签缺失，管理责任尚未处置完成。",
    "胡善承认避雷黄历来源是铜铃回声，不能预测后续随机雷，也未经过正式巡雷记录核验；他需带传播名册，不带黄历。",
    "听雷塔东脊第四扣和西脊第二扣需要导雷铜条修补，南北两脊先做低压查验；本章未消耗 conductive-copper-strip，未完成校准。",
    "下一章修塔流程为先封主链、做低压隔离；裴照野只口述刻度，纪凌策复核，曹雨带铜条量尺，胡善带传播名册。",
    "资源余额保持不变：裴照野下品灵石 5 枚、定雷符 3 张；听雷塔 storm-reset-pin 1 枚、conductive-copper-strip 6 段。",
    "西脊第二扣将优先开启检查，因为裴照野判断反卷从那里起；封闭的西脊沟内已传出细小金属绷响。"
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
  "source_sha256": "1c3e62866c5e0238d8c8671a8e294cb32b9730fda17755a580957d38136d746a",
  "entity_changes": [
    {
      "change": "听雷塔西脊第二扣旧铜片被确认外挤一格并顶住接地扣，金属绷响来源被实物确认。",
      "source_evidence": "曹雨赶紧伏下，用量尺抵住扣缝，报数：“第二扣旧片外挤一格，顶住接地扣舌。不是新断，是被反卷挤出来的。”"
    },
    {
      "change": "西脊第二扣导雷断点已嵌入裁好的导雷铜条修补。",
      "source_evidence": "他把裁好的铜条嵌入第二扣导雷断点，用扣钉压平，再由纪凌策接上低压回路。"
    },
    {
      "change": "西脊低压回路通过复核，反卷起点被截断。",
      "source_evidence": "纪凌策报：“西脊低压回路通过。反卷起点截断。”"
    },
    {
      "change": "传播名册被用于整理候场弟子原候场线、实际站位和铜铃回声先后，确认多人站位偏东或越线。",
      "source_evidence": "纪凌策接过一看，右栏果然列着二十来个人名，每个名字后有原候场线、实际站位和听到铜铃回声的先后。有五人从中线挪到偏东，有三人越过了原定半步线，还有两人把“不得停留”告示抄成“不可久留，须快步向东”。"
    }
  ],
  "relationship_changes": [
    {
      "change": "曹雨的暂挂铜铃位置、铜铃回声和候场弟子换位之间被沈络拆分为三项责任链条，不能互相抵消。",
      "source_evidence": "沈络没看他，只在名册上画线：“暂挂造成偏东回声；回声造成换位；换位越过候场线。三件事分别记，不互相抵消。”"
    },
    {
      "change": "胡善的传播责任范围扩大到名册所列人员。",
      "source_evidence": "“你要解释的是传播范围。”沈络把名册拍到他怀里，“候场弟子重新分组，偏东越线者明日补安全听训。你的责任范围扩大到名册所列人员。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "ability",
      "change": "裴照野在不触碰雷纹、不执笔、不注灵、不越线的低负荷条件下，继续以雷痕辨序口述西脊残痕方向、逆行时长和扣位异常，并被纪凌策代录。",
      "state_id": "thunder-mark-sequencing",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "纪凌策提笔代录：“裴照野口述：西入东、逆行二刻半、第二扣多一格。未触碰雷纹。”\n\n沈络补了一句：“未执笔，未注灵，未越线。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野右手未恢复，沈络继续禁止他执符笔探痕和注灵复验。",
      "state_id": "solo-high-voltage-thunder-pattern-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“未加重不是恢复。”沈络道，“继续不得执符笔探痕，不得注灵复验。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "injury",
      "change": "裴照野右手雷麻仍未恢复，西脊修补未解除伤势状态。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络最后复核伤势限制：“西脊修补不等于右手恢复。裴照野仍只准低负荷抄录与口述，不得执符笔探痕，不得注灵复验。掌侧铜刺未查，定雷符未用。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "thunder-tower",
      "resource_id": "conductive-copper-strip",
      "operation": "consume",
      "amount": 1,
      "unit": "段",
      "resulting_balance": 5,
      "source_or_destination": "西脊第二扣导雷断点修补",
      "change": "听雷塔导雷铜条裁用一段修补西脊第二扣导雷断点，余额从六段降为五段。",
      "source_evidence": "曹雨一笔一画写：“听雷塔导雷铜条，原余六段；裁用一段，去向：西脊第二扣导雷断点修补；现余五段。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "grounding-ridge-echo-delay",
      "state": "knows",
      "belief": "纪凌策知道西脊第二扣旧铜片被挤出一格并顶住接地扣，金属绷响是受力铜片回弹而非新雷，裴照野口述刻度与开扣所见相符。",
      "supersedes_fact_ids": [],
      "change": "纪凌策将西脊第二扣实物异常、绷响来源和裴照野口述相符写入检修记录。",
      "source_evidence": "纪凌策逐项写下：“西脊第二扣旧铜片被挤出一格，顶住接地扣。金属绷响为受力铜片回弹，非新雷。反卷起点可由实物确认。裴照野口述刻度与开扣所见相符。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策仍不正式更正裴照野泄露安全雷时之判断，因为东脊第四扣和封签时间尚未完成交叉复核。",
      "supersedes_fact_ids": [],
      "change": "纪凌策确认西脊实际导行顺序支持裴照野此前雷痕判断，但明确本章不正式更正泄露安全雷时判断。",
      "source_evidence": "纪凌策把西脊检修记录与站位表并放，沉声道：“西脊实际导行顺序，支持裴照野此前关于反卷从西入东、第二扣多一格的雷痕判断。回声角度也新增人员与位置对应。但东脊第四扣少半格尚未开验，封签时间尚未完成交叉复核。”\n\n他看向裴照野：“因此，本章不正式更正裴照野泄露安全雷时之判断。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "investigating",
      "belief": "纪凌策将未封校雷铜铃在值守廊偏东东三梁钩的位置、多人按铜铃回声调整候场位置且实际站位集中偏东，列入回声角度核查。",
      "supersedes_fact_ids": [],
      "change": "纪凌策把偏东铜铃暂挂位置、传播名册中的人员站位和回声角度纳入核查材料。",
      "source_evidence": "纪凌策取出方位盘，沿梁钩、廊柱、候场线逐点标记：“未封校雷铜铃申时一刻至酉时正在值守廊偏东东三梁钩。传播名册显示，多名弟子按回声先后调整候场位置，实际站位集中偏东。此项可入回声角度核查。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "temporary-thunder-clerk-qualification",
      "state": "investigating",
      "belief": "沈络知道西脊修补不等于裴照野右手恢复，裴照野仍只准低负荷抄录与口述，不得执符笔探痕和注灵复验，掌侧铜刺未查且定雷符未用。",
      "supersedes_fact_ids": [],
      "change": "沈络复核并维持裴照野伤势相关的临时登记资格限制。",
      "source_evidence": "沈络最后复核伤势限制：“西脊修补不等于右手恢复。裴照野仍只准低负荷抄录与口述，不得执符笔探痕，不得注灵复验。掌侧铜刺未查，定雷符未用。”"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "lucky-thunder-almanac-source",
      "state": "knows",
      "belief": "胡善知道自己需要逐个带名册所列人员来确认传播范围，不再用生门说法解释换位。",
      "supersedes_fact_ids": [],
      "change": "胡善承诺按名册带人确认，并停止解释生门。",
      "source_evidence": "胡善小声补充：“名册所列人员，我会逐个带来确认，不再解释生门。”"
    }
  ],
  "thread_changes": [
    {
      "change": "西脊检修主线推进：主导雷链已由纪凌策封闭，低压隔离成立。",
      "source_evidence": "纪凌策把三枚隔离扣依次压下。第一扣落，主链灯纹由白转灰；第二扣落，西脊沟内绷响短了一息；第三扣落，隔离罩上浮出低压刻度，停在一寸三分。"
    },
    {
      "change": "主链封闭时明确剩余一枚重置钉只可用于全塔失控阻断，不得用于检修试错。",
      "source_evidence": "纪凌策先验主链闸牌，念道：“申时后主导雷链未封闭，现由正式巡雷使封链。听雷塔剩余重置钉一枚，只作全塔失控阻断，不得用于检修试错。”"
    },
    {
      "change": "东脊第四扣仍少半格，南北两脊未低压查验，四处接地脊尚未完成校准。",
      "source_evidence": "纪凌策收起低压盘，又把东脊标牌翻开：“东脊第四扣仍少半格。南、北两脊未低压查验。四处接地脊尚未完成校准。”"
    },
    {
      "change": "下一步检修目标转向东脊第四扣，重点查明少半格是断裂还是被西脊牵偏。",
      "source_evidence": "纪凌策合上记录册，点向东侧值守廊：“下一处，东脊第四扣。先看少的那半格，是断了，还是被西脊牵偏。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "沈络用规章式冷幽默讽刺曹雨把风险寄托给铜片懂规章。",
      "source_evidence": "沈络看他一眼：“所以先封主链。不是先祈愿铜片懂规章。”"
    },
    {
      "change": "胡善带来的名册混入拜雷式换位理由，形成荒唐笑点。",
      "source_evidence": "第一行：听见第一响，原地勿动，以免抢雷。\n第二行：听见第二响，向东挪一步，东者生门。\n第三行：若第三响迟，蹲半息，显得恭敬。"
    },
    {
      "change": "胡善把黄历被戒律堂门房压平当成报告内容，延续避雷黄历笑点。",
      "source_evidence": "话音刚落，检修区外传来胡善的声音：“我带名册，不带黄历。黄历留在戒律堂门口，被门房压着，压得很平。”"
    }
  ],
  "new_constraints": [
    {
      "change": "听雷塔剩余一枚 storm-reset-pin 仍受限制，只能用于全塔失控阻断，不得用于检修试错。",
      "source_evidence": "纪凌策先验主链闸牌，念道：“申时后主导雷链未封闭，现由正式巡雷使封链。听雷塔剩余重置钉一枚，只作全塔失控阻断，不得用于检修试错。”"
    },
    {
      "change": "裴照野仍不得执符笔探痕，不得注灵复验。",
      "source_evidence": "“未加重不是恢复。”沈络道，“继续不得执符笔探痕，不得注灵复验。”"
    },
    {
      "change": "候场弟子因偏东越线需重新分组，偏东越线者明日补安全听训。",
      "source_evidence": "“你要解释的是传播范围。”沈络把名册拍到他怀里，“候场弟子重新分组，偏东越线者明日补安全听训。你的责任范围扩大到名册所列人员。”"
    }
  ],
  "resolved_constraints": [
    {
      "change": "西脊第二扣反卷起点已被截断，西脊该处低压回路不再倒窜。",
      "source_evidence": "低压灯纹沿西脊走了一圈，至第二扣不再倒窜，灰蓝线顺着接地扣入沟底，停在正刻。"
    }
  ],
  "next_chapter_inputs": [
    "裴照野仍为炼气五层，right-hand-thunder-numbness 未恢复；掌侧铜刺未查，定雷符未用。",
    "裴照野仍只准低负荷抄录与口述，不得执符笔探痕，不得注灵复验，也不得接触高压雷纹。",
    "纪凌策已封闭主导雷链并建立西脊低压隔离；storm-reset-pin 仍余 1 枚，且只作全塔失控阻断，不得用于检修试错。",
    "西脊第二扣旧铜片被确认外挤一格并顶住接地扣；金属绷响为受力旧铜片回弹，非随机新雷。",
    "西脊第二扣已裁用 1 段 conductive-copper-strip 修补并通过低压回路复核，反卷起点已截断。",
    "听雷塔 conductive-copper-strip 余额为 5 段；storm-reset-pin 仍为 1 枚；裴照野下品灵石仍为 5 枚，定雷符仍为 3 张。",
    "东脊第四扣仍少半格，南、北两脊未低压查验，四处接地脊尚未完成校准。",
    "纪凌策确认西脊实际导行顺序支持裴照野此前关于反卷从西入东、第二扣多一格的雷痕判断，但因东脊第四扣尚未开验、封签时间尚未完成交叉复核，仍不正式更正 pei-leaked-strike-window。",
    "传播名册已显示多名弟子按铜铃回声先后调整候场位置，实际站位集中偏东，可用于回声角度核查。",
    "候场弟子已被要求重新分组，偏东越线者明日补安全听训；胡善责任范围扩大到名册所列人员。",
    "下一处检修目标为东脊第四扣，需要查明少半格是断了还是被西脊牵偏。"
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
  "source_sha256": "42f8b138a440f37f01991adab443a00ff3dfb72abe73980460711f32f266dce5",
  "entity_changes": [
    {
      "change": "东脊第四扣确认不是独立断裂，而是受西脊反卷牵拉造成扣位少半格；残痕次序为先受牵引、后被反卷。",
      "source_evidence": "曹雨把量尺换了个角度，刮去扣舌下方一层黑灰。灰下露出的铜面并非整齐断口，而是细长的拉伸纹，纹路先朝西偏，末端又被硬生生掀向主塔。"
    },
    {
      "change": "东脊第四扣已用补片修入导雷槽，原拉伸纹被包入槽内但未抹去痕迹。",
      "source_evidence": "最后一锤落下，补片与旧铜面齐平，拉伸纹被完整包进导雷槽内，却没有强行抹去原有痕迹。"
    },
    {
      "change": "东、西两脊完成低压顺序复核，导行恢复为主塔至东脊、再回主链接地，未再出现西入东反卷。",
      "source_evidence": "低压复核由纪凌策亲自启阵。主塔阵枢亮起一线淡青电芒，沿封闭主链下行，先抵东脊。新补铜条微微发热，第四扣稳稳接住电芒，未见外跳。电芒穿过东脊末端，折回主链，随后沉入接地纹。"
    },
    {
      "change": "南、北两脊仍未查验，四脊校准未完成，听雷塔仍不得恢复运行。",
      "source_evidence": "“东、西顺序复核通过。”他合上阵枢，“南、北未查。四脊校准未成，听雷塔仍不得恢复运行。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "recovery",
      "change": "沈络从裴照野右掌掌侧取出残留铜刺，且全程没有接触高压雷纹；right-hand-thunder-numbness 完成取刺恢复步骤。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "沈络将铜刺封入证物纸：“掌侧残留铜刺，已取出。全程无高压雷纹接触。接下来用定雷符，只稳经脉，不恢复铜条，不替代接地校准，也不保证你立刻能执笔。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "recovery",
      "change": "裴照野使用定雷符稳定经脉后，右手雷麻由持续麻木转为间歇麻木，指节颤动减轻，right-hand-thunder-numbness 进入部分恢复但未解除。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "沈络用木片轻触裴照野四根手指：“症状。”\n\n“持续麻木转为间歇。指节颤动减轻。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野右手雷麻未解除，仍不得接触高压雷纹、不得执符笔探痕、不得独自登塔。",
      "state_id": "solo-high-voltage-thunder-pattern-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野不得独自登塔的限制继续存在。",
      "state_id": "solo-high-voltage-tower-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野临时登记仍须正式巡雷使复核。",
      "state_id": "solo-high-risk-thunder-registration-suspension",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "纪凌策补上一句：“临时登记仍须正式巡雷使复核。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "thunder-tower",
      "resource_id": "conductive-copper-strip",
      "operation": "consume",
      "amount": 1,
      "unit": "段",
      "resulting_balance": 4,
      "source_or_destination": "东脊第四扣导雷缺口修补",
      "change": "听雷塔消耗 1 段 conductive-copper-strip 修补东脊第四扣导雷缺口，余额由 5 段降为 4 段。",
      "source_evidence": "纪凌策写道：“导雷铜条一段，用于东脊第四扣导雷缺口修补。原存五段，现余四段。”"
    },
    {
      "owner_id": "pei-zhaoye",
      "resource_id": "grounding-talisman",
      "operation": "consume",
      "amount": 1,
      "unit": "张",
      "resulting_balance": 2,
      "source_or_destination": "右手雷麻恢复处理",
      "change": "裴照野消耗 1 张 grounding-talisman 用于右手雷麻恢复处理，余额由 3 张降为 2 张，且不得返还。",
      "source_evidence": "纪凌策记道：“定雷符一张，用于右手雷麻恢复处理，已消耗，不得返还。原有三张，现余两张。下品灵石仍为五枚。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "investigating",
      "belief": "纪凌策已将未封铜铃位于值守廊偏东东三梁钩、低限试雷节拍进入候场区域、胡善按名册扩大传播范围等内容记入器物传播路径和人为扩大范围核查。",
      "supersedes_fact_ids": [],
      "change": "纪凌策明确记录铜铃位置、器物传播路径以及胡善扩大传播范围。",
      "source_evidence": "纪凌策抽出一张新核查页：“曹雨，未封铜铃位于值守廊偏东东三梁钩，使低限试雷节拍进入候场区域，记器物传播路径。胡善，抄录回声并按名册传给他人，致传播范围扩大，记人为扩大范围。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策认为铜铃位置、传播站位回声角度、东脊先受牵引后反卷和西脊反卷起点实质削弱裴照野主动口头泄露安全雷时的旧判断，但因第二道封签时间缺口未获正式见证，仍未正式更正原裁记。",
      "supersedes_fact_ids": [],
      "change": "裴照野主动口头泄露安全雷时的旧判断受到实质削弱，但 pei-leaked-strike-window 未正式更正。",
      "source_evidence": "纪凌策将昨日站位表压在核查页旁，依次圈出东三梁钩、偏东候场线以及东、西两脊雷痕的先后：“铜铃位置、传播站位的回声角度、东脊先受牵引后反卷、西脊反卷起点，现可列在同一页。以上事实，实质削弱裴照野主动口头泄露安全雷时的旧判断。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "temporary-thunder-clerk-qualification",
      "state": "investigating",
      "belief": "沈络确认裴照野右手雷麻只属部分恢复，仍需完成低负荷抄录并由沈络复核落点、颤动与经脉回响后才能解除，期间不得接触高压雷纹、不得执符笔探痕、不得独自登塔。",
      "supersedes_fact_ids": [],
      "change": "沈络将裴照野临时登记资格限制更新为取刺和定雷符后部分恢复、但尚未解除。",
      "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
    }
  ],
  "thread_changes": [
    {
      "change": "第二道封签时间缺口仍未闭合，今日不作正式更正。",
      "source_evidence": "“第二道封签的时间缺口尚无正式见证。器物何时失去封闭、谁在何时应当补签，尚未闭合。今日不作正式更正。”"
    },
    {
      "change": "曹雨未做第二道封签的管理责任继续存在。",
      "source_evidence": "“你漏做第二道封签、无正式巡雷使复核便提前低限试雷，两项程序责任也仍在。”"
    },
    {
      "change": "裴照野漏做第二道封签和无正式巡雷使复核便提前低限试雷的程序责任继续存在。",
      "source_evidence": "“你漏做第二道封签、无正式巡雷使复核便提前低限试雷，两项程序责任也仍在。”"
    },
    {
      "change": "东、西脊修补通过和伤势好转均不抵消裴照野提前试雷、漏封等程序责任。",
      "source_evidence": "纪凌策将伤势页与程序责任页分别封好：“东、西脊修补通过，不抵提前试雷之责；伤势好转，也不抵漏封之责。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善把抄录并传播铜铃回声辩称为替铜铃整理措辞。",
      "source_evidence": "胡善忙道：“我也没泄露。我只是听见以后，替铜铃整理了一下措辞。”"
    },
    {
      "change": "胡善因把三声铃扩写成七行时刻被纪凌策指出扩大传播。",
      "source_evidence": "“你把三声铃整理成了七行时刻。”\n\n“我怕铜铃言简意赅，旁人看不明白。”"
    },
    {
      "change": "曹雨心疼半格缺口按一整段导雷铜条入账，被沈络以库房规则压回。",
      "source_evidence": "曹雨盯着那行字：“这半格，算一整段？”\n\n沈络道：“库房按领出算，不按你心疼多少算。”"
    }
  ],
  "new_constraints": [
    {
      "change": "定雷符只用于稳定经脉，不能恢复铜条、替代接地校准或保证裴照野立刻能执笔。",
      "source_evidence": "沈络将铜刺封入证物纸：“掌侧残留铜刺，已取出。全程无高压雷纹接触。接下来用定雷符，只稳经脉，不恢复铜条，不替代接地校准，也不保证你立刻能执笔。”"
    },
    {
      "change": "裴照野右手雷麻解除前必须完成规定低负荷抄录，并由沈络复核落点、颤动与经脉回响后确认。",
      "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
    },
    {
      "change": "裴照野接下来南、北读数只能明日左手低负荷抄，写偏一格就停。",
      "source_evidence": "裴照野点头：“南、北读数，明日左手抄。”\n\n“低负荷。”沈络道，“写偏一格就停。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "东脊第四扣已确认少半格并非独立断裂，而是西脊反卷牵拉造成；实物残痕印证东脊先受牵引、后被反卷。",
    "东脊第四扣已消耗 1 段 conductive-copper-strip 完成导雷缺口修补，听雷塔 conductive-copper-strip 余额为 4 段。",
    "东、西两脊已通过低压导行顺序复核，导行恢复为主塔至东脊、再回主链接地，且未再出现西入东反卷。",
    "南、北两脊仍未查验和修补；四脊校准未成，听雷塔仍不得恢复运行。",
    "storm-reset-pin 未消耗，余额仍为 1 枚。",
    "裴照野消耗 1 张 grounding-talisman 用于右手雷麻恢复处理，定雷符余额为 2 张；下品灵石仍为 5 枚。",
    "right-hand-thunder-numbness 已完成停止高压接触、取出掌侧残留铜刺、使用定雷符稳定经脉三项恢复步骤；症状由持续麻木转为间歇麻木，指节颤动减轻，但尚未解除。",
    "裴照野仍需完成规定低负荷抄录，并由沈络复核落点、颤动与经脉回响后确认，右手雷麻方可解除。",
    "裴照野在解除前仍不得接触高压雷纹，不得执符笔探痕，不得独自登塔；临时登记仍须正式巡雷使复核。",
    "纪凌策已将铜铃位置、传播站位回声角度、东脊先受牵引后反卷和西脊反卷起点列在同一核查页，实质削弱裴照野主动口头泄露安全雷时的旧判断。",
    "因第二道封签时间缺口尚无正式见证，纪凌策未正式更正 pei-leaked-strike-window，也未闭合最终泄密责任结论。",
    "曹雨未封铜铃位于值守廊偏东东三梁钩并使低限试雷节拍进入候场区域，缺失第二道封签的管理责任继续存在。",
    "胡善抄录回声并按名册传给他人，致传播范围扩大，传播管理责任继续按名册处置。",
    "裴照野漏做第二道封签、无正式巡雷使复核便提前低限试雷的程序责任未被东、西脊修补或伤势好转抵消。"
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
  "source_sha256": "926ea75ed146fcadd98c871b1658886e6f5d9c62dadcd463830d2f44f4bce2b5",
  "entity_changes": [
    {
      "change": "胡善提交的传播名册被改为按站位刻度、换位时刻、听闻来源记录，黄历类别仅作为传播路径，不作为雷时依据。",
      "source_evidence": "“保留原话。”纪凌策道，“另添站位刻度、换位时刻、听闻来源。黄历类别不作雷时依据，只作传播路径。”"
    },
    {
      "change": "一名弟子从西七位换至偏东五位的记录被确认与东三梁钩第一折回声角度相符。",
      "source_evidence": "纪凌策提笔，在那人名下添了一行：由西七位换至偏东五位，与东三梁钩第一折回声角度相符。"
    },
    {
      "change": "候场线向东退两丈，胡善原三类押响人群被转为三类待核责任并分开站位。",
      "source_evidence": "这句话落下，候场线当场向东退了两丈。胡善原先编出的三类押响人群，变成了三类待核责任，连站的位置也被分开。"
    },
    {
      "change": "南脊第三扣旧铜皮翘边造成低压导行慢半息，已用整段导雷铜条修补并通过低压导行顺序。",
      "source_evidence": "纪凌策核完刻度，当众记账：“南脊第三扣修补，导雷铜条消耗一段，余额由四段降至三段。低压导行顺序通过。”"
    },
    {
      "change": "北脊第一扣接地刻度虚浮，已用整段导雷铜条加固并通过低压导行顺序。",
      "source_evidence": "纪凌策逐项复核：“北脊第一扣加固，消耗导雷铜条一段，余额由三段降至两段。北脊低压导行顺序通过。”"
    },
    {
      "change": "东、西、南、北四脊器物修补均已完成，低压导行顺序均已通过。",
      "source_evidence": "他翻到前页，将四脊并列：“东、西、南、北，器物修补均已完成，低压导行顺序均已通过。余铜条两段，无富余可供试错。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "recovery",
      "change": "裴照野完成一轮右手低负荷抄录样页，但右手指节仍有轻微僵滞，沈络记录为可继续低负荷验证且未正式解除右手雷麻。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "裴照野继续抄到北脊。最后一行落笔时，中指又慢了半拍。他放下墨笔，右手指节仍有轻微僵滞。\n\n沈络查过落点、颤动和腕侧经脉回响，在样页下写道：“可继续低负荷验证，未正式解除右手雷麻。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野右手未解除前仍只可低负荷抄录，不得执符笔探痕、不得注灵、不得越隔离线。",
      "state_id": "solo-high-voltage-thunder-pattern-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“右手只作低负荷抄录。不执符笔探痕，不注灵，不越隔离线。”她将普通墨笔推过去，“抄四脊刻度。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "thunder-tower",
      "resource_id": "conductive-copper-strip",
      "operation": "consume",
      "amount": 1,
      "unit": "段",
      "resulting_balance": 3,
      "source_or_destination": "南脊第三扣修补",
      "change": "南脊第三扣修补消耗 1 段导雷铜条，余额由 4 段降至 3 段。",
      "source_evidence": "纪凌策核完刻度，当众记账：“南脊第三扣修补，导雷铜条消耗一段，余额由四段降至三段。低压导行顺序通过。”"
    },
    {
      "owner_id": "thunder-tower",
      "resource_id": "conductive-copper-strip",
      "operation": "consume",
      "amount": 1,
      "unit": "段",
      "resulting_balance": 2,
      "source_or_destination": "北脊第一扣加固",
      "change": "北脊第一扣加固消耗 1 段导雷铜条，余额由 3 段降至 2 段。",
      "source_evidence": "纪凌策逐项复核：“北脊第一扣加固，消耗导雷铜条一段，余额由三段降至两段。北脊低压导行顺序通过。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "纪凌策已取得值守廊见证：铜铃位于东三梁钩，铃口朝西南，酉时正前缺第二道封签。",
      "supersedes_fact_ids": [
        "unsealed-calibration-chime-at-duty-corridor"
      ],
      "change": "纪凌策取得并记录第二道封签时间缺口见证。",
      "source_evidence": "“铜铃位置？”\n\n“就在东三梁钩。铃口朝西南。”\n\n“第二道封签？”\n\n那弟子想了片刻：“酉时正前未见。第一道旧封在铃柄上，外层应加的第二道没有。酉时正换班时，我还提醒过曹师兄，说那铃风一吹便响。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "grounding-ridge-echo-delay",
      "state": "knows",
      "belief": "纪凌策确认铜铃位置、封签缺失时段、胡善名册偏东换位记录及东西脊雷痕先后已并列入核查页，四项证据能够彼此校验。",
      "supersedes_fact_ids": [
        "grounding-ridge-echo-delay"
      ],
      "change": "纪凌策将铜铃位置、封签时间、回声站位和雷痕先后合并为接近闭合的新证据链。",
      "source_evidence": "纪凌策没有接那句话，只让见证弟子在证言下按印。他把铜铃位置、铃口朝向、封签缺失时段，与胡善名册上的偏东换位记录并列，又将东、西脊雷痕先后附在后页。"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策认为旧推断方向应当推翻，现有证据已不足以支持只凭裴照野口头泄露，但原裁记需戒律堂复核签字，尚未正式更正。",
      "supersedes_fact_ids": [],
      "change": "纪凌策明确表示现有新证据足以推翻旧推断方向，但未正式更正 pei-leaked-strike-window。",
      "source_evidence": "“旧推断方向应当推翻。”纪凌策说得清楚，“现有证据已不足以支持‘只凭裴照野口头泄露’。但原裁记需戒律堂复核签字，今日不作正式更正。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "temporary-thunder-clerk-qualification",
      "state": "investigating",
      "belief": "沈络确认裴照野完成低负荷抄录但右手雷麻未解除，只可继续低负荷验证。",
      "supersedes_fact_ids": [
        "temporary-thunder-clerk-qualification"
      ],
      "change": "沈络将裴照野临时登记资格推进到低负荷抄录验证未解除阶段。",
      "source_evidence": "沈络查过落点、颤动和腕侧经脉回响，在样页下写道：“可继续低负荷验证，未正式解除右手雷麻。”"
    }
  ],
  "thread_changes": [
    {
      "change": "四项证据已接近闭合：铜铃位置、酉时正前缺第二道封签、回声折入候场位、东西脊雷痕先后与调用顺序不一致。",
      "source_evidence": "“铜铃位于东三梁钩，酉时正前缺第二道封签；回声向西南折入候场位；实际雷痕为东脊先受牵引、西脊再反卷，与时刻簿调用顺序不一致。”纪凌策合上半页，“四项已经能彼此校验。”"
    },
    {
      "change": "裴照野明确承认铜铃漏第二封签的登记责任和无正式巡雷使复核提前试雷的程序责任，且证据更正不抵记过。",
      "source_evidence": "“铜铃漏第二封签，我有登记责任。无正式巡雷使复核，提前试雷，我有程序责任。”裴照野道，“证据更正，不抵记过。”"
    },
    {
      "change": "听雷塔四脊虽修补并通过低压顺序，但未逢真实雷雨、未正式校准，仍不可恢复运行。",
      "source_evidence": "裴照野答：“修补完成。低压顺序通过。未逢真实雷雨，未作正式校准。听雷塔不可恢复运行。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善原本用来区分信黄历程度的三栏被戒律堂改造成责任和传播路径记录。",
      "source_evidence": "卷首写着三栏：听见一响就换位，听见两响才换位，没听见但跟着换位。\n\n沈络扫了一眼：“这是申诉，还是名册？”"
    },
    {
      "change": "试图把南三扣停顿解读成下一回安全时辰的弟子被沈络派去追加责任签字。",
      "source_evidence": "胡善正带人逐一按名，旁边一名弟子探头道：“南三扣处停了一息，莫非下一回安全时辰在——”\n\n沈络头也没抬：“你去名册末尾确认三名跟随换位者。确认完再回来抄安全分组，不抄时辰。”"
    }
  ],
  "new_constraints": [
    {
      "change": "听雷塔导雷铜条仅余两段，无富余可供试错，不许裁条试错。",
      "source_evidence": "沈络收起样页和核查页：“明日提交四脊正式低压校准申请，同时做最后一轮抄录复验。铜条只余两段，不许裁条试错。”"
    },
    {
      "change": "听雷塔未逢真实雷雨、未正式校准，仍不可恢复运行。",
      "source_evidence": "裴照野答：“修补完成。低压顺序通过。未逢真实雷雨，未作正式校准。听雷塔不可恢复运行。”"
    },
    {
      "change": "重置钉余额仍为一枚，本章未启用。",
      "source_evidence": "纪凌策则在资源账末逐项念明：“导雷铜条余额两段。重置钉余额一枚，本章未启用。裴照野下品灵石五枚，定雷符两张，均未消耗。”"
    },
    {
      "change": "裴照野下品灵石仍为五枚、定雷符仍为两张，本章均未消耗。",
      "source_evidence": "纪凌策则在资源账末逐项念明：“导雷铜条余额两段。重置钉余额一枚，本章未启用。裴照野下品灵石五枚，定雷符两张，均未消耗。”"
    },
    {
      "change": "原裁记未获沈络复核签字前仍然有效。",
      "source_evidence": "沈络接过核查页：“我先核风险、证言来源与记录连续性。未签之前，裁记仍在。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "南脊第三扣旧铜皮翘边导致低压导行慢半息，已消耗 1 段 conductive-copper-strip 修补并通过低压导行顺序。",
    "北脊第一扣接地刻度虚浮，已消耗 1 段 conductive-copper-strip 加固并通过低压导行顺序。",
    "东、西、南、北四处接地脊均完成器物修补并通过低压导行顺序复核。",
    "听雷塔 conductive-copper-strip 余额为 2 段，且无富余可供试错。",
    "storm-reset-pin 余额仍为 1 枚，本章未启用。",
    "裴照野 low-grade-spirit-stone 余额仍为 5 枚，grounding-talisman 余额仍为 2 张，本章均未消耗。",
    "四处接地脊尚未逢真实雷雨，未作正式校准，听雷塔不可恢复运行。",
    "胡善传播名册已按站位刻度、换位时刻、听闻来源重记，黄历类别只作传播路径；偏东四至六位另封一道线，不与未换位者混组。",
    "已有弟子由西七位换至偏东五位的记录与东三梁钩第一折回声角度相符，黄历传播范围已转为责任范围。",
    "曹雨找来的值守廊见证人证明酉时正前未见第二道封签，铜铃位于东三梁钩且铃口朝西南。",
    "纪凌策已将铜铃位置、铃口朝向、封签缺失时段、胡善名册偏东换位记录、东西脊雷痕先后并入核查页，四项证据已经能彼此校验。",
    "纪凌策认为旧推断方向应当推翻，现有证据已不足以支持只凭裴照野口头泄露，但 pei-leaked-strike-window 因需戒律堂复核签字尚未正式更正。",
    "沈络正在复核风险、证言来源与记录连续性；未签之前原裁记仍在。",
    "裴照野完成一轮低负荷抄录样页，但右手食指和中指仍有迟滞，right-hand-thunder-numbness 未正式解除。",
    "裴照野仍只可低负荷验证，不得执符笔探痕，不得注灵，不得越隔离线。",
    "曹雨缺失第二道封签的管理责任继续存在。",
    "胡善扩大回声传播范围的管理责任继续按名册逐人处置。",
    "裴照野承认铜铃漏第二封签的登记责任和无正式巡雷使复核提前试雷的程序责任，证据更正不抵记过。"
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
  "source_sha256": "47003c61f1da63b49359c680b6687bddb94dc56147001fbad55d43edf44e8fc5",
  "entity_changes": [
    {
      "change": "曹雨在复核文本中确认未封校雷铜铃曾挂在值守廊东三梁钩、铃口朝西南、酉时正前第二道封签缺失，且“暂挂”不改变事实性质。",
      "source_evidence": "曹雨只得逐字写下事实，又在末尾按了手印。“暂挂”二字没能落进正文，只被纪凌策留在旁注里，标作当事人最初陈述，不改变器物位置与封签状态。"
    },
    {
      "change": "四处接地脊正式校准申请已被受理并列入真实雷雨候测队列，正式校准要求正式巡雷使与戒律堂复核官同时在场。",
      "source_evidence": "榜上写的是：四处接地脊正式校准申请已受理，列入真实雷雨候测队列。校准时须正式巡雷使、戒律堂复核官同时在场。"
    }
  ],
  "relationship_changes": [
    {
      "change": "沈络继续作为复核与责任分栏裁定者，明确曹雨、裴照野、胡善三方责任分列，证据推进不抵消责任。",
      "source_evidence": "她又翻到责任分栏：“曹雨，铜铃未封管理责任单列。裴照野，漏做第二道封签与提前试雷程序责任单列。胡善，扩大回声传播范围，按名册逐人处置。任何一项证据推进，都不抵消这三栏。”"
    },
    {
      "change": "正式校准时由纪凌策与沈络同时在场。",
      "source_evidence": "沈络在校准申请末尾签下受理意见：“四脊器物修补完成，低压导行顺序通过。准入真实雷雨候测队列。正式校准时，纪凌策与我同时在场。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "recovery",
      "change": "裴照野右手雷麻正式解除，依据包括停止接触高压雷纹、掌侧残留铜刺已取出、此前消耗一张定雷符稳定经脉、完成低负荷抄录复验且食指中指无落点偏移。",
      "state_id": "right-hand-thunder-numbness",
      "state_action": "resolve",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“right-hand-thunder-numbness，右手雷麻，今日正式解除。依据四项：其一，停止接触高压雷纹；其二，掌侧残留铜刺已取出；其三，此前消耗一张定雷符稳定经脉；其四，完成低负荷抄录复验，食指、中指无落点偏移。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野因右手雷麻产生的低负荷抄录限制解除；他已在不探痕、不注灵、不越线条件下完成复验，右手落点未再偏移。",
      "state_id": "solo-high-voltage-thunder-pattern-ban",
      "state_action": "resolve",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络抽走三页复验纸，逐页对光。纸上没有灵气浸痕，说明裴照野未向墨笔注灵；鞋尖始终停在红签之外，右手的落点也没有再向右下偏移。"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野仍为炼气五层，临时雷时登记仍须正式巡雷使复核。",
      "state_id": "solo-high-risk-thunder-registration-suspension",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野伤势解除后仍不得独自值守高压雷塔。",
      "state_id": "solo-high-voltage-tower-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "shen-luo",
      "fact_id": "temporary-thunder-clerk-qualification",
      "state": "knows",
      "belief": "沈络确认裴照野右手雷麻已正式解除，但伤势解除不等于临时雷时登记资格恢复，仍须正式巡雷使复核且不得独自值守高压雷塔。",
      "supersedes_fact_ids": [
        "temporary-thunder-clerk-qualification"
      ],
      "change": "沈络对裴照野临时雷时登记资格作出新裁定：伤势解除但资格未恢复。",
      "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策认为铜铃位置、铃口朝向、封签时间和东西脊雷痕先后四项证据表明旧推断方向应当推翻，并已提交戒律堂核记录连续性，但原裁记尚未正式更正。",
      "supersedes_fact_ids": [],
      "change": "纪凌策将四项证据整理成待更正裁记复核文本并提交戒律堂核记录连续性。",
      "source_evidence": "“铜铃位置决定回声起点，铃口朝向决定折入候场廊的角度；封签时间说明该时段铜铃未完成封闭；东西脊雷痕先后与偏东换位名册相合。”他合上笔帽，“旧推断方向应当推翻。现将文本交戒律堂核记录连续性。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "pei-leaked-strike-window",
      "state": "investigating",
      "belief": "沈络确认四项证据可以进入正式更正流程，但受理不等于裁记更改，原裁记仍在。",
      "supersedes_fact_ids": [],
      "change": "沈络受理待更正裁记复核文本，但未正式更正原裁记。",
      "source_evidence": "“尚未更正。”沈络道，“受理不是裁记更改。复核签字未完，原裁记仍在。”"
    },
    {
      "character_id": "cao-yu",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "曹雨确认未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，酉时正前第二道封签缺失；“暂挂”不改变器物位置与封签状态。",
      "supersedes_fact_ids": [
        "unsealed-calibration-chime-at-duty-corridor"
      ],
      "change": "曹雨在复核文本中按手印确认校雷铜铃位置、朝向和封签缺失事实。",
      "source_evidence": "曹雨只得逐字写下事实，又在末尾按了手印。“暂挂”二字没能落进正文，只被纪凌策留在旁注里，标作当事人最初陈述，不改变器物位置与封签状态。"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "lucky-thunder-almanac-source",
      "state": "knows",
      "belief": "胡善知道自己对候测队列作出的押雷排号式解释被沈络纳入听闻来源记录，并导致所有听过解释的人重新签收安全告示。",
      "supersedes_fact_ids": [
        "lucky-thunder-almanac-source"
      ],
      "change": "胡善关于候测队列的解释被正式转化为分组签字与责任记录。",
      "source_evidence": "沈络走到榜前：“很好。既然你已向人解释过排号，所有听过解释的人，重新签收安全告示。”"
    }
  ],
  "thread_changes": [
    {
      "change": "最后一轮低负荷抄录复验完成，复验内容覆盖四脊同步刻度、铜铃封签时间缺口、低压导行顺序三类记录。",
      "source_evidence": "“只抄录，不探痕，不注灵，不越线。三类记录，缺一类，复验中止。”"
    },
    {
      "change": "待更正裁记复核文本已被沈络受理并准入正式更正流程，但 pei-leaked-strike-window 尚未正式更正。",
      "source_evidence": "“尚未更正。”沈络道，“受理不是裁记更改。复核签字未完，原裁记仍在。”"
    },
    {
      "change": "四脊器物修补完成且低压导行顺序通过，下一步进入真实雷雨候测队列。",
      "source_evidence": "沈络在校准申请末尾签下受理意见：“四脊器物修补完成，低压导行顺序通过。准入真实雷雨候测队列。正式校准时，纪凌策与我同时在场。”"
    },
    {
      "change": "下一章启动项为雨前布阵。",
      "source_evidence": "沈络封住申请册：“候测队列第一项，雨前布阵。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善把真实雷雨候测队列误读成人员押雷排号，导致听过解释的候场弟子全部重新签收安全告示。",
      "source_evidence": "“诸位，既然有队列，便有先后。排得靠前，先借校准雷；排得靠后，或可避开余雷。依我看，偏东第四位最——”"
    },
    {
      "change": "胡善的解释被拆成分组签收表，每一次解释都进入听闻来源记录。",
      "source_evidence": "半个时辰后，新分组全部按印。胡善的每一次解释都被记入听闻来源，候场弟子也依新表分开站位。"
    }
  ],
  "new_constraints": [
    {
      "change": "裴照野伤势解除后，临时雷时登记仍须正式巡雷使复核，仍不得独自值守高压雷塔。",
      "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
    },
    {
      "change": "裴照野漏做校雷铜铃第二道封签和无正式巡雷使复核便提前低限试雷的程序责任继续记过。",
      "source_evidence": "“还有，”沈络看着他，“漏做校雷铜铃第二道封签，以及无正式巡雷使复核便提前低限试雷，继续记过。”"
    },
    {
      "change": "曹雨铜铃未封管理责任、裴照野程序责任、胡善扩大回声传播范围责任均不被证据推进抵消。",
      "source_evidence": "她又翻到责任分栏：“曹雨，铜铃未封管理责任单列。裴照野，漏做第二道封签与提前试雷程序责任单列。胡善，扩大回声传播范围，按名册逐人处置。任何一项证据推进，都不抵消这三栏。”"
    },
    {
      "change": "四处接地脊正式校准必须在正式巡雷使、戒律堂复核官同时在场时进行。",
      "source_evidence": "榜上写的是：四处接地脊正式校准申请已受理，列入真实雷雨候测队列。校准时须正式巡雷使、戒律堂复核官同时在场。"
    },
    {
      "change": "听雷塔导雷铜条余额二段，不得用于校准试错；重置钉余额一枚，仅供全塔失控阻断，不得用于检修试错。",
      "source_evidence": "她又添了一行风险限制：“导雷铜条余额二段，不得用于校准试错；重置钉余额一枚，仅供全塔失控阻断，不得用于检修试错。”"
    }
  ],
  "resolved_constraints": [
    {
      "change": "裴照野右手雷麻及其导致的右手低负荷落点限制正式解除。",
      "source_evidence": "“right-hand-thunder-numbness，右手雷麻，今日正式解除。依据四项：其一，停止接触高压雷纹；其二，掌侧残留铜刺已取出；其三，此前消耗一张定雷符稳定经脉；其四，完成低负荷抄录复验，食指、中指无落点偏移。”"
    }
  ],
  "next_chapter_inputs": [
    "裴照野仍为炼气五层，right-hand-thunder-numbness 已由沈络正式解除。",
    "裴照野伤势解除后，临时雷时登记仍须正式巡雷使复核，仍不得独自值守高压雷塔。",
    "裴照野漏做校雷铜铃第二道封签、无正式巡雷使复核便提前低限试雷的程序责任继续记过。",
    "纪凌策已把铜铃位置、铃口朝向、封签时间缺口、东西脊雷痕先后整理成待更正裁记复核文本。",
    "沈络已受理待更正裁记复核文本并确认四项证据可以进入正式更正流程，但 pei-leaked-strike-window 尚未正式更正，原裁记仍在。",
    "曹雨确认未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，酉时正前第二道封签缺失；“暂挂”不改变事实性质。",
    "曹雨铜铃未封管理责任单列，继续存在。",
    "胡善扩大回声传播范围责任继续按名册逐人处置。",
    "胡善误读候测队列后，候场弟子已重新分组签收安全告示；胡善每一次解释均被记入听闻来源。",
    "四脊器物修补完成，低压导行顺序通过，四处接地脊正式校准申请已准入真实雷雨候测队列。",
    "正式校准时须纪凌策与沈络同时在场。",
    "下一项为雨前布阵。",
    "听雷塔仍未完成真实雷雨正式校准，未恢复可运行状态。",
    "裴照野 low-grade-spirit-stone 余额 5 枚，grounding-talisman 余额 2 张，本章无消耗。",
    "听雷塔 storm-reset-pin 余额 1 枚，conductive-copper-strip 余额 2 段，本章无消耗。",
    "导雷铜条余额二段，不得用于校准试错；重置钉余额一枚，仅供全塔失控阻断，不得用于检修试错。"
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
  "source_sha256": "761ecc0d3d8627e247259e56c22c2a6ad5e55dd188a7f611e3b56f178963e4d3",
  "entity_changes": [
    {
      "change": "东、西、南、北四处接地脊在真实雷雨中完成正式校准，四脊同步刻度入限。",
      "source_evidence": "他在末栏加盖巡雷复核印：“真实雷雨三次导行，四脊同步刻度入限。正式校准完成。”"
    },
    {
      "change": "听雷塔完成真实雷雨校准前置但仍未转入运行标识，仍待终签且不得高压独立值守。",
      "source_evidence": "听雷塔的阵光渐渐收拢，却没有转入运行标识。塔门上仍悬着“待终签，不得高压独立值守”的戒律牌。"
    }
  ],
  "relationship_changes": [
    {
      "change": "裴照野本章参与接地回路维持时处于纪凌策正式复核与沈络风险监看之下，没有独自值守或越线。",
      "source_evidence": "裴照野站在主塔基座内圈，纪凌策在他右后方持校准页，沈络守着资源封匣与总断纹。无人越线，塔门也没有合拢，正式巡雷使的复核印始终亮在阵心旁。"
    },
    {
      "change": "曹雨继续承担铜铃维护与封签管理责任，且不能再以“暂挂”模糊事实。",
      "source_evidence": "“责任呢？”沈络问。\n\n“由我承担铜铃维护与封签管理责任。”\n\n“不要再说暂挂。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "progress",
      "change": "裴照野在真实雷雨中维持完整接地回路，出现炼气五层至炼气六层的突破前兆，但未突破。",
      "stage_after": "炼气五层",
      "source_evidence": "“炼气五层关隘已现。未越。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "突破前兆出现后，裴照野被停止加压，不能借余雷强冲。",
      "state_id": "pre-breakthrough-no-forced-thunder-pressure",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "沈络抬手切断他面前的低压引导纹：“停止加压。今日校准前置已足，不能借余雷强冲。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野仍不得独自值守高压雷塔。",
      "state_id": "solo-high-voltage-tower-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "听雷塔的阵光渐渐收拢，却没有转入运行标识。塔门上仍悬着“待终签，不得高压独立值守”的戒律牌。"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "裴照野的临时雷时与回路动作仍必须在正式巡雷使复核下进行，不得独自登记。",
      "state_id": "solo-high-risk-thunder-registration-suspension",
      "state_action": "set",
      "stage_after": "炼气五层",
      "source_evidence": "“今日动作边界。”\n\n“纪巡雷使复核下维持回路。不上高压塔顶，不越隔离线，不独自登记。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "believes_false",
      "belief": "纪凌策认为旧裁记所依据的“裴照野口头泄露安全雷时”与现有事实链条不合，铜铃回声足以形成传播路径，雨中记录补齐四脊雷痕连续性，旧判断应在终签时正式更正，但此刻尚未正式更正。",
      "supersedes_fact_ids": [],
      "change": "纪凌策将雨中四脊同步刻度并入待更正裁记，并明确旧判断应在终签时正式更正。",
      "source_evidence": "他逐行核过，才道：“旧裁记所依据的‘裴照野口头泄露安全雷时’，与现有事实链条不合。铜铃回声足以形成传播路径，雨中记录又补齐了四脊雷痕连续性。我的旧判断应在终签时正式更正。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "pei-leaked-strike-window",
      "state": "investigating",
      "belief": "沈络确认本章只确认记录连续；恢复运行签字、原裁记更正和责任拆分仍须等待最终风险复核，原裁记尚未正式更正。",
      "supersedes_fact_ids": [],
      "change": "沈络未在本章落印更正裁记，将恢复运行签字、原裁记更正和责任拆分推迟到最终风险复核后。",
      "source_evidence": "沈络按住裁记末页，没有落印：“今日只确认记录连续。恢复运行签字、原裁记更正、责任拆分，等最终风险复核。”"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "rain-pause-thunder-timing-misread",
      "state": "believes_false",
      "belief": "胡善把纪凌策雨前停顿和校准页留空误读为押雷口诀。",
      "supersedes_fact_ids": [],
      "change": "胡善误读雨前停顿与校准页留空，写下新的押时内容。",
      "source_evidence": "纸上写着：风停三息，东位为吉；页留一格，逢雷宜避。"
    },
    {
      "character_id": "cao-yu",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "曹雨知道未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，且第二道封签缺失。",
      "supersedes_fact_ids": [],
      "change": "曹雨再次确认校雷铜铃位置、朝向与第二道封签缺失。",
      "source_evidence": "曹雨站在案台另一边，被问到铜铃时只答：“未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南。第二道封签缺失。”"
    }
  ],
  "thread_changes": [
    {
      "change": "胡善雨前误读造成候场弟子再次调整分组，并追加安全听训签收和听闻来源记录。",
      "source_evidence": "偏东组重新退回隔离线，按新表排成两列。纪凌策在附页记下挪动时刻、听闻来源和重新签收的次序。原本混在一处的候场弟子因此分得更清，连谁先听见胡善第一句、谁只听见第二句，都有了落笔处。"
    },
    {
      "change": "旧裁记更正进入终签前最后程序障碍：记录连续已确认，但恢复运行签字、原裁记更正、责任拆分均待最终风险复核。",
      "source_evidence": "沈络按住裁记末页，没有落印：“今日只确认记录连续。恢复运行签字、原裁记更正、责任拆分，等最终风险复核。”"
    },
    {
      "change": "裴照野、曹雨、胡善各自程序责任继续单列，不因校准完成、听训补做或维持回路抵消。",
      "source_evidence": "“单列。”沈络道，“校准完成不抵封签缺失。”\n\n胡善也凑近半步：“那我今日让众人重新签收，传播一项是否——”\n\n“单列。补做听训不抵扩大传播。”\n\n裴照野道：“我的两项也单列。漏第二封签，提前低限试雷。”\n\n沈络看他一眼：“记过不因你维持回路而消失。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善把纪凌策停三息和校准页留空误编成押雷口诀，随即被沈络改成安全禁令并要求逐人签收。",
      "source_evidence": "沈络把听训纸铺平，逐句划线：“‘风停三息，东位为吉’，改成‘风停期间不得擅自换位’。‘页留一格，逢雷宜避’，改成‘未录刻度前不得推定雷时’。你念一遍，偏东组逐人签收。”"
    },
    {
      "change": "胡善又试图把裴照野突破前兆理解为最准押雷，被纪凌策准备用传播责任记录吓回安全听训疑问。",
      "source_evidence": "胡善迟疑着举手：“这等前兆，能否算四脊校准后最准的一条押雷——”\n\n纪凌策把附页翻到传播责任补充栏：“原话再说一遍，我记听闻来源。”\n\n胡善立刻放下手：“我申请改成安全听训疑问。”"
    }
  ],
  "new_constraints": [
    {
      "change": "本章资源封匣未开启：导雷铜条余额两段，重置钉余额一枚，灵石与定雷符未启用。",
      "source_evidence": "沈络检查总断纹与资源封匣，封签均未开启：“导雷铜条未动，余额两段。重置钉未动，余额一枚。灵石与定雷符未启用。”"
    },
    {
      "change": "裴照野下品灵石余额五枚、定雷符余额两张，本章均未消耗；若第十章风险复核通过，突破需按三枚灵石、一张定雷符正式流程监督。",
      "source_evidence": "沈络核完最后一遍封匣：“下品灵石五枚，定雷符两张，均未消耗。明日若风险复核通过，再按三枚灵石、一张定雷符的正式流程监督突破。塔的最终运行签字与裁记更正也在明日处理。”"
    },
    {
      "change": "听雷塔库存导雷铜条两段和重置钉一枚不得用于校准试错，重置钉只作失控阻断。",
      "source_evidence": "纪凌策核对封匣：“裴照野下品灵石五枚，定雷符两张，今日不启用。塔库存导雷铜条两段，重置钉一枚，只作失控阻断，不作校准试错。”"
    },
    {
      "change": "南脊慢差不允许先补铜，异常必须先停，不能用库存试错。",
      "source_evidence": "沈络点头：“南脊若慢，不许先补铜。全程异常先停。”"
    },
    {
      "change": "第十章前听雷塔仍待终签，不得高压独立值守。",
      "source_evidence": "听雷塔的阵光渐渐收拢，却没有转入运行标识。塔门上仍悬着“待终签，不得高压独立值守”的戒律牌。"
    },
    {
      "change": "裴照野今夜不得冲关，下一道雷来前必须先做最终风险复核。",
      "source_evidence": "“今夜不冲关。下一道雷来前，先做最终风险复核。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "东、西、南、北四处接地脊已在真实雷雨中完成正式校准，四脊同步刻度入限并由纪凌策记入校准页。",
    "听雷塔已具备申请恢复运行的技术前置，但仍未转入运行标识；第 10 章前仍待最终恢复运行签字，不得高压独立值守。",
    "裴照野仍为炼气五层；真实雷雨中维持完整接地回路后已出现炼气五层关隘，但本章未越关、未突破。",
    "裴照野突破前兆出现后已停止加压，今夜不冲关；下一道雷来前须先做最终风险复核。",
    "第 10 章若风险复核通过，裴照野突破流程需消耗 3 枚下品灵石和 1 张定雷符并受正式监督。",
    "裴照野 low-grade-spirit-stone 余额仍为 5 枚，grounding-talisman 余额仍为 2 张，本章未消耗。",
    "听雷塔 conductive-copper-strip 余额仍为 2 段，storm-reset-pin 余额仍为 1 枚，本章未启用。",
    "导雷铜条两段不得用于校准试错；重置钉一枚只作失控阻断，不作校准试错。",
    "纪凌策已将铜铃位置、东西脊雷痕先后、第二道封签缺失、回声角度、雨中四脊同步刻度并列成待更正事实链，并认为旧裁记应在终签时正式更正。",
    "pei-leaked-strike-window 本章尚未正式更正；沈络只确认记录连续，恢复运行签字、原裁记更正和责任拆分均待最终风险复核。",
    "曹雨继续承担铜铃维护与封签管理责任，校准完成不抵封签缺失。",
    "胡善因雨前停顿押时误读，已追加安全听训签收、分组隔离和听闻来源记录；补做听训不抵扩大传播责任。",
    "裴照野漏做校雷铜铃第二道封签、无正式巡雷使复核便提前低限试雷的程序责任继续记过，不因维持回路而消失。",
    "right-hand-thunder-numbness 承接上一章已解除状态，本章未复发，也未被突破前兆重新定义。"
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
  "source_sha256": "59075f66a4ac93a32f2e4913df75b5ac0fa6239bcebac0d2a8d9145ba4e8760d",
  "entity_changes": [
    {
      "change": "听雷塔通过低强度复核运行，恢复为可复核运行状态，但不得升级高压测试。",
      "source_evidence": "沈络合上风险册：“复核运行通过。听雷塔具备恢复为可复核运行状态的条件。不得升级高压测试。”"
    },
    {
      "change": "听雷塔终签已落，塔门重新开启半扇，但高压值守位仍空置。",
      "source_evidence": "听雷塔终签已落，塔门重新开启半扇。\n\n高压值守位，仍然空着。"
    }
  ],
  "relationship_changes": [
    {
      "change": "纪凌策在裴照野突破后接管雷时口令，裴照野只报方向和回路。",
      "source_evidence": "纪凌策当即收起突破记录：“下一轮复核运行，我报时。你只报方向和回路。”"
    },
    {
      "change": "胡善带领原黄历传播组退出高压值守区，按低强度安全听训排班管理人员。",
      "source_evidence": "最后一笔落下，整张押雷班次变成了低强度安全听训排班。原黄历传播组全部编入甲组，由胡善带队退出高压值守区；未传播者编入乙组，在外廊学习接地告示。"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "pre-breakthrough-no-forced-thunder-pressure 因沈络正式批准裴照野在监督下突破而解除。",
      "state_id": "pre-breakthrough-no-forced-thunder-pressure",
      "state_action": "resolve",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络逐项落印：“四脊已校准，旧伤已解除，真实雷雨中的完整接地回路已维持。准许裴照野在正式巡雷使监督下突破。只准守回路，不准接管高压雷时，不准独自登塔。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "breakthrough",
      "change": "裴照野在真实雷雨中维持完整接地回路并消耗 3 枚下品灵石和 1 张定雷符后，从炼气五层突破至炼气六层。",
      "state_id": "",
      "state_action": "",
      "stage_after": "炼气六层",
      "from_stage": "炼气五层",
      "to_stage": "炼气六层",
      "prerequisites": [
        "四脊已校准",
        "旧伤已解除",
        "真实雷雨中的完整接地回路已维持"
      ],
      "costs": [
        "3 枚下品灵石",
        "1 张定雷符",
        "突破后雷声回响限制"
      ],
      "new_limits": [
        {
          "state_id": "post-breakthrough-thunder-echo",
          "description": "停雷后仍闻双重雷声，落雷时刻判断延迟。"
        },
        {
          "state_id": "solo-high-voltage-tower-ban",
          "description": "三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查。"
        },
        {
          "state_id": "one-ridge-simultaneous-maintenance-limit",
          "description": "可同时维持主塔与一处接地脊，不能同时维持超过一处接地脊。"
        }
      ],
      "source_evidence": "裴照野闭住呼吸，将主塔与西脊一并维持。四脊雷光绕过汇流台，完整走完一周，再从北脊泄入地层。\n\n他体内那道卡了许久的关隘随之松开。\n\n灵力扩过主阵，又稳稳搭住西脊，没有牵动其余两处。炼气六层的气息在雷雨里展开，只比原先多承一线，并未替塔上任何铜扣归位，也未让时刻簿自己添上一笔。"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "ability",
      "change": "裴照野突破后获得同时维持主塔与一处接地脊的能力，且该能力不能替代器物复核或责任裁定。",
      "state_id": "one-ridge-simultaneous-maintenance",
      "state_action": "set",
      "stage_after": "炼气六层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "沈络看了一眼阵纹：“境界确认，炼气六层。能力边界：可同时维持主塔与一处接地脊。器物仍按器物复核，责任仍按责任裁定。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "突破后新增 post-breakthrough-thunder-echo，裴照野停雷后仍听见双重雷声，并出现落雷时刻判断延迟。",
      "state_id": "post-breakthrough-thunder-echo",
      "state_action": "set",
      "stage_after": "炼气六层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "雷声忽然停了一瞬。\n\n裴照野却仍听见两道。\n\n一道在云上，一道像贴着耳骨滚过，慢了半拍。\n\n他睁开眼：“停雷后有回响。双声。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "solo-high-voltage-tower-ban 更新为三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查。",
      "state_id": "solo-high-voltage-tower-ban",
      "state_action": "set",
      "stage_after": "炼气六层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“症状：停雷后仍闻双重雷声，落雷时刻判断延迟。活动限制：三日内不得独自值守高压雷塔。每日仅准在正式巡雷使复核下进行低强度接地检查。”"
    },
    {
      "subject_id": "pei-zhaoye",
      "kind": "restriction",
      "change": "solo-high-risk-thunder-registration-suspension 更新为裴照野不再报雷时，正式记录由纪凌策接管，裴照野只报雷痕方向。",
      "state_id": "solo-high-risk-thunder-registration-suspension",
      "state_action": "set",
      "stage_after": "炼气六层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“正式记录以戌初二刻半入册。”纪凌策接管雷时口令，“裴照野只报雷痕方向。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "pei-zhaoye",
      "resource_id": "low-grade-spirit-stone",
      "operation": "consume",
      "amount": 3,
      "unit": "枚",
      "resulting_balance": 2,
      "source_or_destination": "炼气五层突破至炼气六层",
      "change": "裴照野突破消耗 3 枚下品灵石，余额 2 枚。",
      "source_evidence": "“下品灵石消耗三枚，余额二枚。”沈络声音不高，“定雷符消耗一张，余额一张。”"
    },
    {
      "owner_id": "pei-zhaoye",
      "resource_id": "grounding-talisman",
      "operation": "consume",
      "amount": 1,
      "unit": "张",
      "resulting_balance": 1,
      "source_or_destination": "炼气五层突破至炼气六层时稳定雷意",
      "change": "裴照野突破消耗 1 张定雷符，余额 1 张。",
      "source_evidence": "“下品灵石消耗三枚，余额二枚。”沈络声音不高，“定雷符消耗一张，余额一张。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-leaked-strike-window",
      "state": "knows",
      "belief": "纪凌策正式确认所谓安全雷时来自铜铃回声传播，不是裴照野主动口头泄露，原判断已正式更正。",
      "supersedes_fact_ids": [
        "pei-leaked-strike-window"
      ],
      "change": "纪凌策正式更正 pei-leaked-strike-window。",
      "source_evidence": "“以上证据足以证明所谓安全雷时来自铜铃回声传播，不是裴照野主动口头泄露。原判断正式更正。”"
    },
    {
      "character_id": "shen-luo",
      "fact_id": "pei-leaked-strike-window",
      "state": "knows",
      "belief": "沈络已在更正文书与恢复运行书之间落印，接受原裁记正式更正，同时恢复运行不改变封签缺失和程序责任。",
      "supersedes_fact_ids": [
        "pei-leaked-strike-window"
      ],
      "change": "沈络结束对 pei-leaked-strike-window 的调查状态并落印确认更正。",
      "source_evidence": "沈络在更正文书与恢复运行书之间各落一印。"
    },
    {
      "character_id": "cao-yu",
      "fact_id": "unsealed-calibration-chime-at-duty-corridor",
      "state": "knows",
      "belief": "曹雨承认未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，第二道封签当时没有补齐。",
      "supersedes_fact_ids": [
        "unsealed-calibration-chime-at-duty-corridor"
      ],
      "change": "曹雨承认未封校雷铜铃位置与第二道封签缺失。",
      "source_evidence": "曹雨顿了顿：“未封校雷铜铃，曾挂在值守廊东三梁钩，铃口朝西南。第二道封签当时没有补齐。”"
    },
    {
      "character_id": "hu-shan",
      "fact_id": "lucky-thunder-almanac-source",
      "state": "knows",
      "belief": "胡善承认避雷黄历来自铜铃回声，扩大传播是他抄发的。",
      "supersedes_fact_ids": [
        "lucky-thunder-almanac-source",
        "rain-pause-thunder-timing-misread"
      ],
      "change": "胡善确认避雷黄历来源并承认扩大传播。",
      "source_evidence": "“来自铜铃回声。”胡善道，“扩大传播是我抄发的。”"
    },
    {
      "character_id": "ji-lingce",
      "fact_id": "pei-procedure-liabilities-retained",
      "state": "knows",
      "belief": "纪凌策正式保留裴照野漏做校雷铜铃第二道封签、无正式巡雷使复核便提前低限试雷两项程序责任，修塔、维持回路与突破均不抵扣记过。",
      "supersedes_fact_ids": [],
      "change": "纪凌策在更正文书中保留裴照野两项程序责任。",
      "source_evidence": "“同时保留裴照野两项程序责任：漏做校雷铜铃第二道封签；无正式巡雷使复核便提前进行低限试雷。修塔、维持回路与突破，均不抵扣记过。”"
    }
  ],
  "thread_changes": [
    {
      "change": "裴照野两项程序责任继续记过，不因修塔、维持回路或突破抵扣。",
      "source_evidence": "“同时保留裴照野两项程序责任：漏做校雷铜铃第二道封签；无正式巡雷使复核便提前进行低限试雷。修塔、维持回路与突破，均不抵扣记过。”"
    },
    {
      "change": "曹雨因未封校雷铜铃和第二道封签缺失进入管理责任处置流程。",
      "source_evidence": "“管理责任进入处置流程。”沈络道，“恢复运行不改变封签缺失。”"
    },
    {
      "change": "胡善因避雷黄历来自铜铃回声且由其扩大传播，按名册进入处置流程。",
      "source_evidence": "“来自铜铃回声。”胡善道，“扩大传播是我抄发的。”\n\n“按名册进入处置流程。”"
    },
    {
      "change": "章末资源余额封存为裴照野下品灵石二枚、定雷符一张；听雷塔重置钉一枚、导雷铜条二段，已耗资源不得返还。",
      "source_evidence": "终签册最后一页，纪凌策逐笔登记：裴照野下品灵石二枚，定雷符一张；听雷塔重置钉一枚，导雷铜条二段。余额封存承接，不得返还已耗资源。"
    }
  ],
  "comedy_changes": [
    {
      "change": "胡善误把恢复运行理解为可以重新排押雷班次。",
      "source_evidence": "胡善听见“恢复运行”，立刻从袖中抽出一张排得密密麻麻的纸：“既然恢复了，我把新押雷班次也排好了。偏东组守戌初，西廊组押戌正——”"
    },
    {
      "change": "裴照野将胡善的押雷班次改成安全听训排班，并把胡善职责改为看人和补签。",
      "source_evidence": "最后一笔落下，整张押雷班次变成了低强度安全听训排班。原黄历传播组全部编入甲组，由胡善带队退出高压值守区；未传播者编入乙组，在外廊学习接地告示。\n\n胡善捧着改完的纸：“那我这个领队，主要看哪一道雷？”\n\n裴照野指向最下方：“看人。少一个，你补签。”"
    }
  ],
  "new_constraints": [
    {
      "change": "裴照野突破后不能独自值守高压雷塔，只能在正式巡雷使复核下进行低强度接地检查。",
      "source_evidence": "“症状：停雷后仍闻双重雷声，落雷时刻判断延迟。活动限制：三日内不得独自值守高压雷塔。每日仅准在正式巡雷使复核下进行低强度接地检查。”"
    },
    {
      "change": "听雷塔恢复为可复核运行状态不等于全面开放，高压值守仍须正式巡雷使主持。",
      "source_evidence": "“听雷塔自此恢复为可复核运行状态。不是全面开放。高压值守仍须正式巡雷使主持。”"
    },
    {
      "change": "裴照野突破后能力边界限定为可同时维持主塔与一处接地脊，不能替代器物复核或责任裁定。",
      "source_evidence": "沈络看了一眼阵纹：“境界确认，炼气六层。能力边界：可同时维持主塔与一处接地脊。器物仍按器物复核，责任仍按责任裁定。”"
    },
    {
      "change": "已耗资源不得返还；听雷塔剩余重置钉一枚、导雷铜条二段封存承接。",
      "source_evidence": "终签册最后一页，纪凌策逐笔登记：裴照野下品灵石二枚，定雷符一张；听雷塔重置钉一枚，导雷铜条二段。余额封存承接，不得返还已耗资源。"
    }
  ],
  "resolved_constraints": [
    {
      "change": "裴照野突破前停止加压、不能借余雷强冲的限制因正式监督突破流程完成而解除。",
      "source_evidence": "沈络逐项落印：“四脊已校准，旧伤已解除，真实雷雨中的完整接地回路已维持。准许裴照野在正式巡雷使监督下突破。只准守回路，不准接管高压雷时，不准独自登塔。”"
    }
  ],
  "next_chapter_inputs": [
    "裴照野已从炼气五层突破至炼气六层，能力边界为可同时维持主塔与一处接地脊。",
    "裴照野新增 post-breakthrough-thunder-echo：停雷后仍闻双重雷声，落雷时刻判断延迟。",
    "裴照野三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查；雷时口令由纪凌策接管。",
    "听雷塔已恢复为可复核运行状态，但不是全面开放，高压值守仍须正式巡雷使主持。",
    "听雷塔终签已落，塔门重新开启半扇，高压值守位仍空着。",
    "pei-leaked-strike-window 已由纪凌策依据铜铃位置、雷痕先后、封签时间和回声角度正式更正：裴照野没有主动口头泄露安全雷时。",
    "裴照野漏做校雷铜铃第二道封签、无正式巡雷使复核便提前进行低限试雷两项程序责任继续记过，修塔、维持回路与突破均不抵扣。",
    "曹雨承认未封校雷铜铃曾挂在值守廊东三梁钩且第二道封签未补齐，管理责任进入处置流程。",
    "胡善承认避雷黄历来自铜铃回声且扩大传播是其抄发，按名册进入处置流程。",
    "胡善的押雷班次已被改写为低强度安全听训排班，原黄历传播组编入甲组并退出高压值守区，未传播者编入乙组在外廊学习接地告示。",
    "章末资源余额：裴照野 low-grade-spirit-stone 2 枚、grounding-talisman 1 张；听雷塔 storm-reset-pin 1 枚、conductive-copper-strip 2 段；已耗资源不得返还。",
    "right-hand-thunder-numbness 已在突破前正式解除，突破未被记作治伤原因。"
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
        "change": "外门候场弟子持有并传阅写有所谓安全雷时和站位的避雷黄历。",
        "source_evidence": "纸边被汗浸软，上头写着歪歪扭扭的字：辰时三刻半，东风铃二响，西南柱阴影内可避；巳初一响后退三步；值守廊不得停留三息以上，三息后雷不认人。"
      },
      {
        "change": "校雷铜铃曾被曹雨暂挂在值守廊西梁钩且第二道复位封签缺失。",
        "source_evidence": "纪凌策写下三项：铜铃曾暂挂值守廊西梁钩；第二道封签缺失；黄历节拍与低限校雷回声相似。"
      },
      {
        "change": "胡善交出《避雷黄历初校》抄本，抄本包含按回声和站位解释的避雷规则。",
        "source_evidence": "胡善忍痛似的交出最厚一本。封皮上写着《避雷黄历初校》，旁边还画了一个笑眯眯的铃。纪凌策翻开，见每条后头都配着站位：“廊口闻半响者不宜贪；西南闻二响者可小进；告示下三息为一小周天。”"
      },
      {
        "change": "校雷铜铃未封期间曾挂在值守廊偏东第三根梁下旧钩，离东墙约四尺。‘暂挂’不能替代封签。",
        "source_evidence": "片刻后，曹雨指向偏东那根梁：“第三根梁下的旧钩。离东墙约四尺。”\n\n“为何挂那里？”\n\n“铃架漆未干，检修间又在搬铜料。我想着只挂半日。”\n\n“未封器物进入值守廊，半日也有回声。”沈络道，“‘暂挂’说明时长，不改变位置，也不替代封签。”"
      },
      {
        "change": "听雷塔东、西两处接地脊回声异常成立，南、北暂不能判定完好。",
        "source_evidence": "纪凌策复看裴照野的标位，又亲自以低强度灵识扫过，不作引雷，只核对回声方向。\n\n“东、西两处异常成立。南、北暂不能判定完好。”"
      },
      {
        "change": "听雷塔低限试雷出现错序反卷，主塔未修复，四处接地脊未校准。",
        "source_evidence": "纪凌策封闭试雷阵枢，又在时刻簿上补录：“本次试雷未提高强度。确认东、西两处接地脊先后倒置，并存在反卷牵连。主塔未修复，四脊未校准。”"
      },
      {
        "change": "曹雨未封校雷铜铃偏东梁钩位置与回声角度再次被验证，但封签时间仍待核。",
        "source_evidence": "铜铃先接主链节拍，回声沿铃口朝向折入值守廊，恰与胡善抄本上最早几页的间隔相合。\n\n“位置成立。”沈络道，“角度成立到值守廊。封签时间仍待核。”"
      },
      {
        "change": "曹雨提交的铜铃维护记录明确未封校雷铜铃曾于申时一刻至酉时正暂挂在值守廊偏东东三梁钩，且第二道封签缺失。",
        "source_evidence": "纪凌策写下这七字，又补记：未封校雷铜铃自申时一刻至酉时正，暂挂值守廊偏东东三梁钩。"
      },
      {
        "change": "胡善提交的避雷黄历抄本来源被明确为铜铃回声，不是正式巡雷记录。",
        "source_evidence": "“黄历来源？”\n\n“铜铃回声。”\n\n“是否经正式巡雷记录核验？”\n\n“没有。”"
      },
      {
        "change": "听雷塔西脊第二扣旧铜片被确认外挤一格并顶住接地扣，金属绷响来源被实物确认。",
        "source_evidence": "曹雨赶紧伏下，用量尺抵住扣缝，报数：“第二扣旧片外挤一格，顶住接地扣舌。不是新断，是被反卷挤出来的。”"
      },
      {
        "change": "西脊第二扣导雷断点已嵌入裁好的导雷铜条修补。",
        "source_evidence": "他把裁好的铜条嵌入第二扣导雷断点，用扣钉压平，再由纪凌策接上低压回路。"
      },
      {
        "change": "西脊低压回路通过复核，反卷起点被截断。",
        "source_evidence": "纪凌策报：“西脊低压回路通过。反卷起点截断。”"
      },
      {
        "change": "传播名册被用于整理候场弟子原候场线、实际站位和铜铃回声先后，确认多人站位偏东或越线。",
        "source_evidence": "纪凌策接过一看，右栏果然列着二十来个人名，每个名字后有原候场线、实际站位和听到铜铃回声的先后。有五人从中线挪到偏东，有三人越过了原定半步线，还有两人把“不得停留”告示抄成“不可久留，须快步向东”。"
      },
      {
        "change": "东脊第四扣确认不是独立断裂，而是受西脊反卷牵拉造成扣位少半格；残痕次序为先受牵引、后被反卷。",
        "source_evidence": "曹雨把量尺换了个角度，刮去扣舌下方一层黑灰。灰下露出的铜面并非整齐断口，而是细长的拉伸纹，纹路先朝西偏，末端又被硬生生掀向主塔。"
      },
      {
        "change": "东脊第四扣已用补片修入导雷槽，原拉伸纹被包入槽内但未抹去痕迹。",
        "source_evidence": "最后一锤落下，补片与旧铜面齐平，拉伸纹被完整包进导雷槽内，却没有强行抹去原有痕迹。"
      },
      {
        "change": "东、西两脊完成低压顺序复核，导行恢复为主塔至东脊、再回主链接地，未再出现西入东反卷。",
        "source_evidence": "低压复核由纪凌策亲自启阵。主塔阵枢亮起一线淡青电芒，沿封闭主链下行，先抵东脊。新补铜条微微发热，第四扣稳稳接住电芒，未见外跳。电芒穿过东脊末端，折回主链，随后沉入接地纹。"
      },
      {
        "change": "南、北两脊仍未查验，四脊校准未完成，听雷塔仍不得恢复运行。",
        "source_evidence": "“东、西顺序复核通过。”他合上阵枢，“南、北未查。四脊校准未成，听雷塔仍不得恢复运行。”"
      },
      {
        "change": "胡善提交的传播名册被改为按站位刻度、换位时刻、听闻来源记录，黄历类别仅作为传播路径，不作为雷时依据。",
        "source_evidence": "“保留原话。”纪凌策道，“另添站位刻度、换位时刻、听闻来源。黄历类别不作雷时依据，只作传播路径。”"
      },
      {
        "change": "一名弟子从西七位换至偏东五位的记录被确认与东三梁钩第一折回声角度相符。",
        "source_evidence": "纪凌策提笔，在那人名下添了一行：由西七位换至偏东五位，与东三梁钩第一折回声角度相符。"
      },
      {
        "change": "候场线向东退两丈，胡善原三类押响人群被转为三类待核责任并分开站位。",
        "source_evidence": "这句话落下，候场线当场向东退了两丈。胡善原先编出的三类押响人群，变成了三类待核责任，连站的位置也被分开。"
      },
      {
        "change": "南脊第三扣旧铜皮翘边造成低压导行慢半息，已用整段导雷铜条修补并通过低压导行顺序。",
        "source_evidence": "纪凌策核完刻度，当众记账：“南脊第三扣修补，导雷铜条消耗一段，余额由四段降至三段。低压导行顺序通过。”"
      },
      {
        "change": "北脊第一扣接地刻度虚浮，已用整段导雷铜条加固并通过低压导行顺序。",
        "source_evidence": "纪凌策逐项复核：“北脊第一扣加固，消耗导雷铜条一段，余额由三段降至两段。北脊低压导行顺序通过。”"
      },
      {
        "change": "东、西、南、北四脊器物修补均已完成，低压导行顺序均已通过。",
        "source_evidence": "他翻到前页，将四脊并列：“东、西、南、北，器物修补均已完成，低压导行顺序均已通过。余铜条两段，无富余可供试错。”"
      },
      {
        "change": "曹雨在复核文本中确认未封校雷铜铃曾挂在值守廊东三梁钩、铃口朝西南、酉时正前第二道封签缺失，且“暂挂”不改变事实性质。",
        "source_evidence": "曹雨只得逐字写下事实，又在末尾按了手印。“暂挂”二字没能落进正文，只被纪凌策留在旁注里，标作当事人最初陈述，不改变器物位置与封签状态。"
      },
      {
        "change": "四处接地脊正式校准申请已被受理并列入真实雷雨候测队列，正式校准要求正式巡雷使与戒律堂复核官同时在场。",
        "source_evidence": "榜上写的是：四处接地脊正式校准申请已受理，列入真实雷雨候测队列。校准时须正式巡雷使、戒律堂复核官同时在场。"
      },
      {
        "change": "东、西、南、北四处接地脊在真实雷雨中完成正式校准，四脊同步刻度入限。",
        "source_evidence": "他在末栏加盖巡雷复核印：“真实雷雨三次导行，四脊同步刻度入限。正式校准完成。”"
      },
      {
        "change": "听雷塔完成真实雷雨校准前置但仍未转入运行标识，仍待终签且不得高压独立值守。",
        "source_evidence": "听雷塔的阵光渐渐收拢，却没有转入运行标识。塔门上仍悬着“待终签，不得高压独立值守”的戒律牌。"
      },
      {
        "change": "听雷塔通过低强度复核运行，恢复为可复核运行状态，但不得升级高压测试。",
        "source_evidence": "沈络合上风险册：“复核运行通过。听雷塔具备恢复为可复核运行状态的条件。不得升级高压测试。”"
      },
      {
        "change": "听雷塔终签已落，塔门重新开启半扇，但高压值守位仍空置。",
        "source_evidence": "听雷塔终签已落，塔门重新开启半扇。\n\n高压值守位，仍然空着。"
      }
    ],
    "relationship_changes": [
      {
        "change": "胡善被沈络调整为远端回声样本，不得参与站位解释。",
        "source_evidence": "沈络在风险表上添了一行：“黄历传播者改为远端回声样本。不得参与站位解释。”"
      },
      {
        "change": "下一次低限试雷由纪凌策在场复核，曹雨只控铃，裴照野负责辨序且受右手限制。",
        "source_evidence": "“谁操作？”\n\n“裴照野辨序，我控铃。”曹雨答。\n\n“谁复核？”\n\n纪凌策道：“我在场。”"
      },
      {
        "change": "低负荷抄录流程中，裴照野负责口述雷痕方向与刻度，纪凌策负责代笔和分栏复核。",
        "source_evidence": "沈络把符笔从他右手下抽走，放到纪凌策面前：“你代笔。他口述。原始时刻簿与现场残痕分栏，不准拿一项覆盖另一项。”"
      },
      {
        "change": "次日低压隔离检修分工确定：裴照野只口述刻度，纪凌策复核，曹雨带铜条量尺，胡善带传播名册且不带黄历。",
        "source_evidence": "沈络收起复核页：“明日先封主链，做低压隔离。裴照野只口述刻度，纪凌策复核。曹雨带铜条量尺。胡善带传播名册，不带黄历。”"
      },
      {
        "change": "曹雨的暂挂铜铃位置、铜铃回声和候场弟子换位之间被沈络拆分为三项责任链条，不能互相抵消。",
        "source_evidence": "沈络没看他，只在名册上画线：“暂挂造成偏东回声；回声造成换位；换位越过候场线。三件事分别记，不互相抵消。”"
      },
      {
        "change": "胡善的传播责任范围扩大到名册所列人员。",
        "source_evidence": "“你要解释的是传播范围。”沈络把名册拍到他怀里，“候场弟子重新分组，偏东越线者明日补安全听训。你的责任范围扩大到名册所列人员。”"
      },
      {
        "change": "沈络继续作为复核与责任分栏裁定者，明确曹雨、裴照野、胡善三方责任分列，证据推进不抵消责任。",
        "source_evidence": "她又翻到责任分栏：“曹雨，铜铃未封管理责任单列。裴照野，漏做第二道封签与提前试雷程序责任单列。胡善，扩大回声传播范围，按名册逐人处置。任何一项证据推进，都不抵消这三栏。”"
      },
      {
        "change": "正式校准时由纪凌策与沈络同时在场。",
        "source_evidence": "沈络在校准申请末尾签下受理意见：“四脊器物修补完成，低压导行顺序通过。准入真实雷雨候测队列。正式校准时，纪凌策与我同时在场。”"
      },
      {
        "change": "裴照野本章参与接地回路维持时处于纪凌策正式复核与沈络风险监看之下，没有独自值守或越线。",
        "source_evidence": "裴照野站在主塔基座内圈，纪凌策在他右后方持校准页，沈络守着资源封匣与总断纹。无人越线，塔门也没有合拢，正式巡雷使的复核印始终亮在阵心旁。"
      },
      {
        "change": "曹雨继续承担铜铃维护与封签管理责任，且不能再以“暂挂”模糊事实。",
        "source_evidence": "“责任呢？”沈络问。\n\n“由我承担铜铃维护与封签管理责任。”\n\n“不要再说暂挂。”"
      },
      {
        "change": "纪凌策在裴照野突破后接管雷时口令，裴照野只报方向和回路。",
        "source_evidence": "纪凌策当即收起突破记录：“下一轮复核运行，我报时。你只报方向和回路。”"
      },
      {
        "change": "胡善带领原黄历传播组退出高压值守区，按低强度安全听训排班管理人员。",
        "source_evidence": "最后一笔落下，整张押雷班次变成了低强度安全听训排班。原黄历传播组全部编入甲组，由胡善带队退出高压值守区；未传播者编入乙组，在外廊学习接地告示。"
      }
    ],
    "cultivation_changes": [
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野被纪凌策要求暂停单独登记高风险雷时，只能在巡雷使可见范围内记录低限雷痕。",
        "state_id": "solo-high-risk-thunder-registration-suspension",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“我先按记录判断。”纪凌策看向他，“自此刻起，你暂停单独登记高风险雷时，只在我可见范围内记录低限雷痕。所有黄历抄本交出核验。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "injury",
        "change": "裴照野右手雷麻旧伤仍存在，但本章未加重也未减轻。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "裴照野看见了，没有分辩，只把雷痕先后、接地刻度、疑似回声角度逐项补入低限记录。右手旧麻仍伏在指节里，未重也未轻，他没有碰高压塔梯。"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "injury",
        "change": "裴照野右手雷麻旧伤仍未解除，状态未加重也未恢复。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络看向裴照野的右手：“旧伤何时发作？”\n\n“接触高压雷纹时。指节麻，符笔偏。”\n\n“今日状态？”\n\n“旧伤。未加重，未恢复。”\n\n“是否取出铜刺、用定雷符、完成低负荷抄录复核？”\n\n“没有。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野仍不得独自登高压塔，且不得借查证扩大试雷强度。",
        "state_id": "solo-high-voltage-tower-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络将右手雷麻写入操作风险：“那就仍按未解除处理。不得独自登高压塔，不得借查证扩大试雷强度。你漏封铜铃与提前试雷的程序责任，也不因提出铜铃线索而撤销。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野在检修沟内只能读残痕，不得注灵试压。",
        "state_id": "solo-high-risk-thunder-registration-suspension",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "纪凌策先在沟口布下监督线：“裴照野只读残痕，不注灵试压。曹雨报链号。沈络记录接触时长。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "ability",
        "change": "裴照野在监督下使用雷痕辨序发现东、西两处接地脊回声滞后，但仅凭残痕不能定是链扣错位还是脊端错序。",
        "state_id": "thunder-mark-sequencing",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“西脊也滞后。一处半拍，一处至少一拍。仅凭残痕，不能定是链扣错位还是脊端错序。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "ability",
        "change": "裴照野在低限试雷中用雷痕辨序确认东、西两处接地脊先后倒置，并指出链扣间牵连。",
        "state_id": "thunder-mark-sequencing",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "裴照野放低符笔：“东、西两脊次序倒置。链扣间有牵连。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "injury",
        "change": "裴照野右手雷麻旧伤加重，表现为指节颤动、符笔落点偏移。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络按住记录页，不让他继续：“右手雷麻加重。症状，指节颤动，符笔落点偏移。自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。后续先处理伤势风险。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "沈络新增限制：裴照野不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。",
        "state_id": "solo-high-voltage-thunder-pattern-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络按住记录页，不让他继续：“右手雷麻加重。症状，指节颤动，符笔落点偏移。自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。后续先处理伤势风险。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "沈络正式收紧裴照野接触高压雷纹的资格，要求其停止接触高压雷纹，只准低负荷抄录、口述方向与刻度，并禁止执符笔探痕和注灵复验。",
        "state_id": "solo-high-voltage-thunder-pattern-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "“停止接触高压雷纹。”沈络道，“从现在起，只准低负荷抄录、口述方向与刻度。不得执符笔探痕，不得注灵复验。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "injury",
        "change": "裴照野的右手雷麻仍处于加重状态，表现为右手指节颤动、掌侧旧伤青紫、细微雷意沿筋脉跳动。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "裴照野指节仍在颤。掌侧旧伤处泛着青紫，细微雷意沿筋脉一跳一跳，像有根看不见的铜丝埋在皮下。"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "recovery",
        "change": "裴照野右手雷麻进入恢复流程第一步：停止高压接触；但尚未部分恢复，也不得解除限制。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "沈络又在旁添了一行：“右手雷麻仍属加重状态。停止高压接触，仅为恢复流程第一步。未见部分恢复，不得解除限制。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "ability",
        "change": "裴照野在低负荷状态下继续使用雷痕辨序，能口述错序雷痕的方向、落雷次序和接地刻度，但仍不能确定动机。",
        "state_id": "thunder-mark-sequencing",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "裴照野道：“再记。东脊第四扣，接地刻度少半格。西脊第二扣，多一格。反卷从西入东。”\n\n“能确定是器物错序，不是你落笔错记？”\n\n“能确定方向。不能确定动机。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "ability",
        "change": "裴照野在不触碰雷纹、不执笔、不注灵、不越线的低负荷条件下，继续以雷痕辨序口述西脊残痕方向、逆行时长和扣位异常，并被纪凌策代录。",
        "state_id": "thunder-mark-sequencing",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "纪凌策提笔代录：“裴照野口述：西入东、逆行二刻半、第二扣多一格。未触碰雷纹。”\n\n沈络补了一句：“未执笔，未注灵，未越线。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野右手未恢复，沈络继续禁止他执符笔探痕和注灵复验。",
        "state_id": "solo-high-voltage-thunder-pattern-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“未加重不是恢复。”沈络道，“继续不得执符笔探痕，不得注灵复验。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "injury",
        "change": "裴照野右手雷麻仍未恢复，西脊修补未解除伤势状态。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络最后复核伤势限制：“西脊修补不等于右手恢复。裴照野仍只准低负荷抄录与口述，不得执符笔探痕，不得注灵复验。掌侧铜刺未查，定雷符未用。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "recovery",
        "change": "沈络从裴照野右掌掌侧取出残留铜刺，且全程没有接触高压雷纹；right-hand-thunder-numbness 完成取刺恢复步骤。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "沈络将铜刺封入证物纸：“掌侧残留铜刺，已取出。全程无高压雷纹接触。接下来用定雷符，只稳经脉，不恢复铜条，不替代接地校准，也不保证你立刻能执笔。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "recovery",
        "change": "裴照野使用定雷符稳定经脉后，右手雷麻由持续麻木转为间歇麻木，指节颤动减轻，right-hand-thunder-numbness 进入部分恢复但未解除。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "沈络用木片轻触裴照野四根手指：“症状。”\n\n“持续麻木转为间歇。指节颤动减轻。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野右手雷麻未解除，仍不得接触高压雷纹、不得执符笔探痕、不得独自登塔。",
        "state_id": "solo-high-voltage-thunder-pattern-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野不得独自登塔的限制继续存在。",
        "state_id": "solo-high-voltage-tower-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野临时登记仍须正式巡雷使复核。",
        "state_id": "solo-high-risk-thunder-registration-suspension",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "纪凌策补上一句：“临时登记仍须正式巡雷使复核。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "recovery",
        "change": "裴照野完成一轮右手低负荷抄录样页，但右手指节仍有轻微僵滞，沈络记录为可继续低负荷验证且未正式解除右手雷麻。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "裴照野继续抄到北脊。最后一行落笔时，中指又慢了半拍。他放下墨笔，右手指节仍有轻微僵滞。\n\n沈络查过落点、颤动和腕侧经脉回响，在样页下写道：“可继续低负荷验证，未正式解除右手雷麻。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野右手未解除前仍只可低负荷抄录，不得执符笔探痕、不得注灵、不得越隔离线。",
        "state_id": "solo-high-voltage-thunder-pattern-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“右手只作低负荷抄录。不执符笔探痕，不注灵，不越隔离线。”她将普通墨笔推过去，“抄四脊刻度。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "recovery",
        "change": "裴照野右手雷麻正式解除，依据包括停止接触高压雷纹、掌侧残留铜刺已取出、此前消耗一张定雷符稳定经脉、完成低负荷抄录复验且食指中指无落点偏移。",
        "state_id": "right-hand-thunder-numbness",
        "state_action": "resolve",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“right-hand-thunder-numbness，右手雷麻，今日正式解除。依据四项：其一，停止接触高压雷纹；其二，掌侧残留铜刺已取出；其三，此前消耗一张定雷符稳定经脉；其四，完成低负荷抄录复验，食指、中指无落点偏移。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野因右手雷麻产生的低负荷抄录限制解除；他已在不探痕、不注灵、不越线条件下完成复验，右手落点未再偏移。",
        "state_id": "solo-high-voltage-thunder-pattern-ban",
        "state_action": "resolve",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络抽走三页复验纸，逐页对光。纸上没有灵气浸痕，说明裴照野未向墨笔注灵；鞋尖始终停在红签之外，右手的落点也没有再向右下偏移。"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野仍为炼气五层，临时雷时登记仍须正式巡雷使复核。",
        "state_id": "solo-high-risk-thunder-registration-suspension",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野伤势解除后仍不得独自值守高压雷塔。",
        "state_id": "solo-high-voltage-tower-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "progress",
        "change": "裴照野在真实雷雨中维持完整接地回路，出现炼气五层至炼气六层的突破前兆，但未突破。",
        "stage_after": "炼气五层",
        "source_evidence": "“炼气五层关隘已现。未越。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "突破前兆出现后，裴照野被停止加压，不能借余雷强冲。",
        "state_id": "pre-breakthrough-no-forced-thunder-pressure",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "沈络抬手切断他面前的低压引导纹：“停止加压。今日校准前置已足，不能借余雷强冲。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野仍不得独自值守高压雷塔。",
        "state_id": "solo-high-voltage-tower-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "听雷塔的阵光渐渐收拢，却没有转入运行标识。塔门上仍悬着“待终签，不得高压独立值守”的戒律牌。"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "裴照野的临时雷时与回路动作仍必须在正式巡雷使复核下进行，不得独自登记。",
        "state_id": "solo-high-risk-thunder-registration-suspension",
        "state_action": "set",
        "stage_after": "炼气五层",
        "source_evidence": "“今日动作边界。”\n\n“纪巡雷使复核下维持回路。不上高压塔顶，不越隔离线，不独自登记。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "pre-breakthrough-no-forced-thunder-pressure 因沈络正式批准裴照野在监督下突破而解除。",
        "state_id": "pre-breakthrough-no-forced-thunder-pressure",
        "state_action": "resolve",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络逐项落印：“四脊已校准，旧伤已解除，真实雷雨中的完整接地回路已维持。准许裴照野在正式巡雷使监督下突破。只准守回路，不准接管高压雷时，不准独自登塔。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "breakthrough",
        "change": "裴照野在真实雷雨中维持完整接地回路并消耗 3 枚下品灵石和 1 张定雷符后，从炼气五层突破至炼气六层。",
        "state_id": "",
        "state_action": "",
        "stage_after": "炼气六层",
        "from_stage": "炼气五层",
        "to_stage": "炼气六层",
        "prerequisites": [
          "四脊已校准",
          "旧伤已解除",
          "真实雷雨中的完整接地回路已维持"
        ],
        "costs": [
          "3 枚下品灵石",
          "1 张定雷符",
          "突破后雷声回响限制"
        ],
        "new_limits": [
          {
            "state_id": "post-breakthrough-thunder-echo",
            "description": "停雷后仍闻双重雷声，落雷时刻判断延迟。"
          },
          {
            "state_id": "solo-high-voltage-tower-ban",
            "description": "三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查。"
          },
          {
            "state_id": "one-ridge-simultaneous-maintenance-limit",
            "description": "可同时维持主塔与一处接地脊，不能同时维持超过一处接地脊。"
          }
        ],
        "source_evidence": "裴照野闭住呼吸，将主塔与西脊一并维持。四脊雷光绕过汇流台，完整走完一周，再从北脊泄入地层。\n\n他体内那道卡了许久的关隘随之松开。\n\n灵力扩过主阵，又稳稳搭住西脊，没有牵动其余两处。炼气六层的气息在雷雨里展开，只比原先多承一线，并未替塔上任何铜扣归位，也未让时刻簿自己添上一笔。"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "ability",
        "change": "裴照野突破后获得同时维持主塔与一处接地脊的能力，且该能力不能替代器物复核或责任裁定。",
        "state_id": "one-ridge-simultaneous-maintenance",
        "state_action": "set",
        "stage_after": "炼气六层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "沈络看了一眼阵纹：“境界确认，炼气六层。能力边界：可同时维持主塔与一处接地脊。器物仍按器物复核，责任仍按责任裁定。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "突破后新增 post-breakthrough-thunder-echo，裴照野停雷后仍听见双重雷声，并出现落雷时刻判断延迟。",
        "state_id": "post-breakthrough-thunder-echo",
        "state_action": "set",
        "stage_after": "炼气六层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "雷声忽然停了一瞬。\n\n裴照野却仍听见两道。\n\n一道在云上，一道像贴着耳骨滚过，慢了半拍。\n\n他睁开眼：“停雷后有回响。双声。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "solo-high-voltage-tower-ban 更新为三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查。",
        "state_id": "solo-high-voltage-tower-ban",
        "state_action": "set",
        "stage_after": "炼气六层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“症状：停雷后仍闻双重雷声，落雷时刻判断延迟。活动限制：三日内不得独自值守高压雷塔。每日仅准在正式巡雷使复核下进行低强度接地检查。”"
      },
      {
        "subject_id": "pei-zhaoye",
        "kind": "restriction",
        "change": "solo-high-risk-thunder-registration-suspension 更新为裴照野不再报雷时，正式记录由纪凌策接管，裴照野只报雷痕方向。",
        "state_id": "solo-high-risk-thunder-registration-suspension",
        "state_action": "set",
        "stage_after": "炼气六层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“正式记录以戌初二刻半入册。”纪凌策接管雷时口令，“裴照野只报雷痕方向。”"
      }
    ],
    "resource_changes": [
      {
        "owner_id": "thunder-tower",
        "resource_id": "storm-reset-pin",
        "operation": "consume",
        "amount": 1,
        "unit": "枚",
        "resulting_balance": 1,
        "source_or_destination": "阻断低限试雷错序引发的接地链反卷",
        "change": "听雷塔启用并永久消耗 1 枚 storm-reset-pin，余额从 2 枚降为 1 枚。",
        "source_evidence": "“原有两枚，永久消耗一枚，余额一枚。”沈络当场记入安全复核簿，“用途：阻断低限试雷错序引发的接地链反卷。”"
      },
      {
        "owner_id": "thunder-tower",
        "resource_id": "conductive-copper-strip",
        "operation": "consume",
        "amount": 1,
        "unit": "段",
        "resulting_balance": 5,
        "source_or_destination": "西脊第二扣导雷断点修补",
        "change": "听雷塔导雷铜条裁用一段修补西脊第二扣导雷断点，余额从六段降为五段。",
        "source_evidence": "曹雨一笔一画写：“听雷塔导雷铜条，原余六段；裁用一段，去向：西脊第二扣导雷断点修补；现余五段。”"
      },
      {
        "owner_id": "thunder-tower",
        "resource_id": "conductive-copper-strip",
        "operation": "consume",
        "amount": 1,
        "unit": "段",
        "resulting_balance": 4,
        "source_or_destination": "东脊第四扣导雷缺口修补",
        "change": "听雷塔消耗 1 段 conductive-copper-strip 修补东脊第四扣导雷缺口，余额由 5 段降为 4 段。",
        "source_evidence": "纪凌策写道：“导雷铜条一段，用于东脊第四扣导雷缺口修补。原存五段，现余四段。”"
      },
      {
        "owner_id": "pei-zhaoye",
        "resource_id": "grounding-talisman",
        "operation": "consume",
        "amount": 1,
        "unit": "张",
        "resulting_balance": 2,
        "source_or_destination": "右手雷麻恢复处理",
        "change": "裴照野消耗 1 张 grounding-talisman 用于右手雷麻恢复处理，余额由 3 张降为 2 张，且不得返还。",
        "source_evidence": "纪凌策记道：“定雷符一张，用于右手雷麻恢复处理，已消耗，不得返还。原有三张，现余两张。下品灵石仍为五枚。”"
      },
      {
        "owner_id": "thunder-tower",
        "resource_id": "conductive-copper-strip",
        "operation": "consume",
        "amount": 1,
        "unit": "段",
        "resulting_balance": 3,
        "source_or_destination": "南脊第三扣修补",
        "change": "南脊第三扣修补消耗 1 段导雷铜条，余额由 4 段降至 3 段。",
        "source_evidence": "纪凌策核完刻度，当众记账：“南脊第三扣修补，导雷铜条消耗一段，余额由四段降至三段。低压导行顺序通过。”"
      },
      {
        "owner_id": "thunder-tower",
        "resource_id": "conductive-copper-strip",
        "operation": "consume",
        "amount": 1,
        "unit": "段",
        "resulting_balance": 2,
        "source_or_destination": "北脊第一扣加固",
        "change": "北脊第一扣加固消耗 1 段导雷铜条，余额由 3 段降至 2 段。",
        "source_evidence": "纪凌策逐项复核：“北脊第一扣加固，消耗导雷铜条一段，余额由三段降至两段。北脊低压导行顺序通过。”"
      },
      {
        "owner_id": "pei-zhaoye",
        "resource_id": "low-grade-spirit-stone",
        "operation": "consume",
        "amount": 3,
        "unit": "枚",
        "resulting_balance": 2,
        "source_or_destination": "炼气五层突破至炼气六层",
        "change": "裴照野突破消耗 3 枚下品灵石，余额 2 枚。",
        "source_evidence": "“下品灵石消耗三枚，余额二枚。”沈络声音不高，“定雷符消耗一张，余额一张。”"
      },
      {
        "owner_id": "pei-zhaoye",
        "resource_id": "grounding-talisman",
        "operation": "consume",
        "amount": 1,
        "unit": "张",
        "resulting_balance": 1,
        "source_or_destination": "炼气五层突破至炼气六层时稳定雷意",
        "change": "裴照野突破消耗 1 张定雷符，余额 1 张。",
        "source_evidence": "“下品灵石消耗三枚，余额二枚。”沈络声音不高，“定雷符消耗一张，余额一张。”"
      }
    ],
    "knowledge_changes": [
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策依据时刻簿、调度记录和裴照野当班登记位置，仍保留裴照野泄露安全雷时的嫌疑记录。",
        "supersedes_fact_ids": [],
        "change": "纪凌策没有更正对裴照野泄露安全雷时的误信，只将其作为未排除嫌疑继续记录。",
        "source_evidence": "纪凌策写下三项：铜铃曾暂挂值守廊西梁钩；第二道封签缺失；黄历节拍与低限校雷回声相似。他笔尖停了停，又另起一行：裴照野当班登记位置与黄历所列时段重合，泄露安全雷时嫌疑未排除。"
      },
      {
        "character_id": "pei-zhaoye",
        "fact_id": "shared-safe-window-origin",
        "state": "investigating",
        "belief": "裴照野认为黄历来源可能与校雷铜铃位置、雷痕先后和回声角度有关，而非同一路正式雷时泄露。",
        "supersedes_fact_ids": [],
        "change": "裴照野提出黄历抄录顺序与墙上雷痕方向相反，需核对铜铃位置和回声角度。",
        "source_evidence": "“黄历抄录顺序是西南先响、东柱后响。”他说，“墙上雷痕方向相反。东柱残纹在前，西南回纹在后。不是同一路正式雷时抄出。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "纪凌策知道校雷铜铃曾暂挂值守廊西梁钩，且第二道复位封签缺失。",
        "supersedes_fact_ids": [],
        "change": "纪凌策查问曹雨后确认暂挂说法和第二道封签缺失线索。",
        "source_evidence": "曹雨把铜铃换了个胳膊抱，像那铃忽然重了三倍：“当时赶低限校雷，想着先挂梁钩上避潮，随后便取下。第二道……许是补在工房。”"
      },
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime",
        "state": "knows",
        "belief": "曹雨知道自己曾把校雷铜铃暂挂值守廊，并且第二道复位封签还未补。",
        "supersedes_fact_ids": [
          "unsealed-calibration-chime"
        ],
        "change": "曹雨不再完全隐瞒未封校雷铜铃暂挂值守廊一事，在纪凌策面前承认第二道封签还未补。",
        "source_evidence": "曹雨低头翻袖袋，翻出一枚铜刷、一段旧绳、一张买灯油的欠条，唯独没有封签。他声音更低：“还未补。”"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善知道自己抄过值守廊铜铃声并传给同组，但自称不知真实落雷时刻，只把告示和铃声误解成避雷门道。",
        "supersedes_fact_ids": [
          "lucky-thunder-almanac-source"
        ],
        "change": "胡善不再隐瞒抄录并传播铜铃声一事，但仍否认知道真实落雷时刻。",
        "source_evidence": "胡善蔫了：“承认抄过铃声，也传给同组。弟子不知真实落雷时刻，只以为塔中告示藏得深。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "hu-shan-copied-chime-echo",
        "state": "knows",
        "belief": "纪凌策知道胡善承认抄录并传播值守廊铜铃回声，但胡善不承认知道真实落雷时刻。",
        "supersedes_fact_ids": [],
        "change": "纪凌策获得胡善关于黄历传播来源的口供。",
        "source_evidence": "“从现在起，候场弟子按接地刻度排队，不按黄历。胡善，你承认抄录并传播铜铃回声？”\n\n胡善蔫了：“承认抄过铃声，也传给同组。弟子不知真实落雷时刻，只以为塔中告示藏得深。”"
      },
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "曹雨知道未封校雷铜铃曾暂挂在值守廊偏东第三根梁下旧钩，离东墙约四尺，且暂挂不能替代封签。",
        "supersedes_fact_ids": [
          "unsealed-calibration-chime"
        ],
        "change": "曹雨明确指出未封校雷铜铃的具体暂挂位置，并接受其封签责任。",
        "source_evidence": "片刻后，曹雨指向偏东那根梁：“第三根梁下的旧钩。离东墙约四尺。”\n\n“为何挂那里？”\n\n“铃架漆未干，检修间又在搬铜料。我想着只挂半日。”\n\n“未封器物进入值守廊，半日也有回声。”沈络道，“‘暂挂’说明时长，不改变位置，也不替代封签。”\n\n曹雨没再辩。"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "沈络确认未封校雷铜铃曾挂在值守廊偏东梁钩，且未封器物进入值守廊会造成回声风险，暂挂不替代封签。",
        "supersedes_fact_ids": [],
        "change": "沈络将未封铜铃位置和封签责任纳入复核。",
        "source_evidence": "“未封器物进入值守廊，半日也有回声。”沈络道，“‘暂挂’说明时长，不改变位置，也不替代封签。”"
      },
      {
        "character_id": "pei-zhaoye",
        "fact_id": "shared-safe-window-origin",
        "state": "knows",
        "belief": "裴照野确认避雷黄历来源是校雷铜铃回声节拍，不是后续随机天雷时刻。",
        "supersedes_fact_ids": [
          "shared-safe-window-origin"
        ],
        "change": "裴照野对黄历来源的调查从怀疑转为确认。",
        "source_evidence": "裴照野道：“抄的是铃声。不是天雷。”"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善被现场比对证明其避雷黄历不是预知随机落雷，只是把校验节拍写成押时秘诀；两次避开落雷属于偶合。",
        "supersedes_fact_ids": [
          "lucky-thunder-almanac-source"
        ],
        "change": "胡善的避雷黄历被确认并非真正预知雷击。",
        "source_evidence": "沈络问胡善：“你知道后续落雷时刻吗？”\n\n“不知道。”\n\n“那两次避开，是偶合。你把校验节拍写成押时秘诀，诱使候场弟子按所谓吉位停留，增加聚集风险。记管理责任，人数待核。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "hu-shan-copied-chime-echo",
        "state": "knows",
        "belief": "纪凌策通过黄历、试雷记录和真实雷雨记录比对，确认黄历所抄主要对应低限试雷铜铃节拍而非随机落雷。",
        "supersedes_fact_ids": [
          "hu-shan-copied-chime-echo"
        ],
        "change": "纪凌策完成对胡善黄历来源的当场比对。",
        "source_evidence": "纪凌策逐页展开，又从时刻簿中抽出前三次低限试雷记录。他先对年月，再对铜铃维护册，最后将黄历上那些被圈作“宜出门”的时刻逐个压在试雷节拍下。"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策仍因裴照野当班、调度记录缺口和第二道封签缺失，未正式更正裴照野泄露安全雷时的判断。",
        "supersedes_fact_ids": [],
        "change": "纪凌策保留对裴照野泄露安全雷时的误信，同时把铜铃位置和回声角度列入核查。",
        "source_evidence": "纪凌策在核查单上添入“铜铃偏东梁钩”“铃口朝向”“候场区回声范围”三项，却没有划去裴照野名下的嫌疑。\n\n“时刻簿显示，黄历首批节拍出现时，裴照野正在当班。调度记录也没有第二条正式调用。曹雨所说的挂铃时刻，仍缺第二道封签佐证。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "investigating",
        "belief": "沈络已把裴照野右手旧伤、漏封铜铃和提前试雷程序责任纳入临时登记资格复核，且不因他提出铜铃线索而撤销责任。",
        "supersedes_fact_ids": [
          "temporary-thunder-clerk-qualification"
        ],
        "change": "沈络对裴照野资格复核新增旧伤操作风险和程序责任记录。",
        "source_evidence": "沈络将右手雷麻写入操作风险：“那就仍按未解除处理。不得独自登高压塔，不得借查证扩大试雷强度。你漏封铜铃与提前试雷的程序责任，也不因提出铜铃线索而撤销。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "grounding-ridge-echo-delay",
        "state": "knows",
        "belief": "纪凌策确认听雷塔东、西两处接地脊回声异常成立，南、北暂不能判定完好。",
        "supersedes_fact_ids": [],
        "change": "纪凌策复核裴照野标位后确认东、西两处异常。",
        "source_evidence": "纪凌策复看裴照野的标位，又亲自以低强度灵识扫过，不作引雷，只核对回声方向。\n\n“东、西两处异常成立。南、北暂不能判定完好。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "low-limit-test-thunder-procedure",
        "state": "knows",
        "belief": "沈络批准下一章仅可进行低限一刻试雷，须纪凌策在场复核，storm-reset-pin 预备待命但不得提前启用，启用后永久消耗。",
        "supersedes_fact_ids": [],
        "change": "沈络正式限定下一次试雷程序和重置钉启用条件。",
        "source_evidence": "沈络看过编号：“两枚，只能预备一枚待命。本次不得提前启用。若接地链失序，是否启用由纪凌策当场判断。重置钉入阵即永久消耗，不返还，不补记成暂借。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "grounding-ridge-echo-delay",
        "state": "knows",
        "belief": "纪凌策确认东、西两处接地脊存在先后倒置，并存在反卷牵连；主塔未修复，四脊未校准。",
        "supersedes_fact_ids": [
          "grounding-ridge-echo-delay"
        ],
        "change": "纪凌策从上一章的回声滞后待判定更新为确认东、西两处接地脊先后倒置并存在反卷牵连。",
        "source_evidence": "纪凌策封闭试雷阵枢，又在时刻簿上补录：“本次试雷未提高强度。确认东、西两处接地脊先后倒置，并存在反卷牵连。主塔未修复，四脊未校准。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策仍认为目前证据不足以更正裴照野泄露安全雷时的判断。",
        "supersedes_fact_ids": [],
        "change": "纪凌策维持对裴照野泄露安全雷时的误信，未正式更正。",
        "source_evidence": "“铜铃位置与回声角度继续核查。封签时间另查。错序雷痕另查。”他合上时刻簿，“目前证据不足以更正裴照野泄露安全雷时的判断。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "investigating",
        "belief": "纪凌策承认铜铃位置与回声角度需要继续核查，封签时间和错序雷痕也要另查。",
        "supersedes_fact_ids": [],
        "change": "纪凌策未把铜铃线索用于更正泄露判断，只将铜铃位置、回声角度、封签时间、错序雷痕继续列为核查内容。",
        "source_evidence": "“铜铃位置与回声角度继续核查。封签时间另查。错序雷痕另查。”他合上时刻簿，“目前证据不足以更正裴照野泄露安全雷时的判断。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "investigating",
        "belief": "沈络将重置钉消耗、旧伤加重、提前试雷程序风险和禁止裴照野独自接触高压雷纹纳入安全复核，既有程序责任不抵扣。",
        "supersedes_fact_ids": [
          "temporary-thunder-clerk-qualification"
        ],
        "change": "沈络的临时登记资格复核更新为包含本次低限试雷后果、伤势加重和新的接触限制，且不抵扣此前责任。",
        "source_evidence": "沈络把另一份记录推到他面前：“提前试雷的既有程序风险也继续保留。今日受监督试雷，不抵扣此前责任。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "沈络确认校雷铜铃的非正式悬位实际参与回声传递，第二道封签缺失。",
        "supersedes_fact_ids": [
          "unsealed-calibration-chime-at-duty-corridor"
        ],
        "change": "沈络将曹雨所称暂挂的铜铃记录为实际参与回声传递且缺失第二道封签。",
        "source_evidence": "沈络在簿上写道：“非正式悬位，实际参与回声传递。第二道封签缺失。”"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善被当场告知他避雷黄历中准的是铜铃响过，而不是正式雷时或宜忌。",
        "supersedes_fact_ids": [
          "lucky-thunder-almanac-source"
        ],
        "change": "胡善的黄历来源被进一步压实为铜铃回声节拍，他本人被禁止添宜忌。",
        "source_evidence": "胡善隔着两道线道：“那上面有三处很准。”\n\n纪凌策道：“准的是铜铃响过。”\n\n胡善闭嘴了。"
      },
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "曹雨知道校雷铜铃当时挂在偏东第三根梁的旧钩，铃口朝西南，未补第二道封签，并且下一次核查要带封签簿与铜铃维护记录说明缺失原因。",
        "supersedes_fact_ids": [
          "unsealed-calibration-chime-at-duty-corridor"
        ],
        "change": "曹雨对未封铜铃位置与第二道封签缺失责任的知情状态更新为需提交封签簿和维护记录说明。",
        "source_evidence": "沈络抬笔，在复核簿末尾添了一行：“曹雨，下一次核查带封签簿与铜铃维护记录。说明第二道封签为何缺失。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "grounding-ridge-echo-delay",
        "state": "knows",
        "belief": "纪凌策确认低限试雷中时刻簿记录的调用顺序与残痕显示的实际导行顺序不一致，时刻簿不足以单独解释错序雷痕。",
        "supersedes_fact_ids": [
          "grounding-ridge-echo-delay"
        ],
        "change": "纪凌策纠正了只依赖时刻簿判断试雷顺序的旧认知，确认必须区分调用顺序与实际导行顺序。",
        "source_evidence": "“时刻簿记录调用顺序。”纪凌策道，“残痕记录实际导行顺序。两者不一致。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "investigating",
        "belief": "纪凌策将铜铃位置、雷痕先后、封签时间和回声角度列为合并核查材料，但现阶段仍不足以更正泄露判断。",
        "supersedes_fact_ids": [],
        "change": "纪凌策的核查证据项更新为铜铃位置、雷痕先后、封签时间、回声角度四项合并核查。",
        "source_evidence": "纪凌策把四项材料列在同页：铜铃位置、雷痕先后、封签时间、回声角度。\n\n“合并核查。”他说，“现阶段仍不足以更正泄露判断。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策仍认为现有证据不足以更正裴照野泄露安全雷时的核查结论。",
        "supersedes_fact_ids": [],
        "change": "纪凌策没有正式更正裴照野泄露安全雷时的判断。",
        "source_evidence": "他随后看向裴照野：“此项只纠正试雷顺序判断，不足以更正泄露安全雷时的核查结论。”"
      },
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "曹雨知道维护册显示第二道封签缺失，且格式申诉不能改变梁钩位置或补出第二道封签。",
        "supersedes_fact_ids": [],
        "change": "曹雨已面对第二道封签缺失和偏东梁钩暂挂记录，但责任处置尚未完成。",
        "source_evidence": "沈络又道：“格式不改变梁钩位置，也不补出第二道封签。”\n\n曹雨的神色重新落了回去。"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善承认避雷黄历来源是铜铃回声，不能预测后续随机雷，且没有经过正式巡雷记录核验。",
        "supersedes_fact_ids": [
          "lucky-thunder-almanac-source"
        ],
        "change": "胡善旧有“黄历能押后续随机雷”的认知被随机空响和复核事实纠正。",
        "source_evidence": "沈络问：“这算什么？”\n\n胡善小声道：“随机空响。”\n\n“能押后续随机雷？”\n\n“不能。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "investigating",
        "belief": "沈络将裴照野右手雷麻加重后的高压接触限制、低负荷抄录流程和未解除限制纳入临时登记资格复核。",
        "supersedes_fact_ids": [],
        "change": "沈络确认停止高压接触只是恢复流程第一步，裴照野的限制仍有效。",
        "source_evidence": "沈络又在旁添了一行：“右手雷麻仍属加重状态。停止高压接触，仅为恢复流程第一步。未见部分恢复，不得解除限制。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "grounding-ridge-echo-delay",
        "state": "knows",
        "belief": "纪凌策知道西脊第二扣旧铜片被挤出一格并顶住接地扣，金属绷响是受力铜片回弹而非新雷，裴照野口述刻度与开扣所见相符。",
        "supersedes_fact_ids": [],
        "change": "纪凌策将西脊第二扣实物异常、绷响来源和裴照野口述相符写入检修记录。",
        "source_evidence": "纪凌策逐项写下：“西脊第二扣旧铜片被挤出一格，顶住接地扣。金属绷响为受力铜片回弹，非新雷。反卷起点可由实物确认。裴照野口述刻度与开扣所见相符。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策仍不正式更正裴照野泄露安全雷时之判断，因为东脊第四扣和封签时间尚未完成交叉复核。",
        "supersedes_fact_ids": [],
        "change": "纪凌策确认西脊实际导行顺序支持裴照野此前雷痕判断，但明确本章不正式更正泄露安全雷时判断。",
        "source_evidence": "纪凌策把西脊检修记录与站位表并放，沉声道：“西脊实际导行顺序，支持裴照野此前关于反卷从西入东、第二扣多一格的雷痕判断。回声角度也新增人员与位置对应。但东脊第四扣少半格尚未开验，封签时间尚未完成交叉复核。”\n\n他看向裴照野：“因此，本章不正式更正裴照野泄露安全雷时之判断。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "investigating",
        "belief": "纪凌策将未封校雷铜铃在值守廊偏东东三梁钩的位置、多人按铜铃回声调整候场位置且实际站位集中偏东，列入回声角度核查。",
        "supersedes_fact_ids": [],
        "change": "纪凌策把偏东铜铃暂挂位置、传播名册中的人员站位和回声角度纳入核查材料。",
        "source_evidence": "纪凌策取出方位盘，沿梁钩、廊柱、候场线逐点标记：“未封校雷铜铃申时一刻至酉时正在值守廊偏东东三梁钩。传播名册显示，多名弟子按回声先后调整候场位置，实际站位集中偏东。此项可入回声角度核查。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "investigating",
        "belief": "沈络知道西脊修补不等于裴照野右手恢复，裴照野仍只准低负荷抄录与口述，不得执符笔探痕和注灵复验，掌侧铜刺未查且定雷符未用。",
        "supersedes_fact_ids": [],
        "change": "沈络复核并维持裴照野伤势相关的临时登记资格限制。",
        "source_evidence": "沈络最后复核伤势限制：“西脊修补不等于右手恢复。裴照野仍只准低负荷抄录与口述，不得执符笔探痕，不得注灵复验。掌侧铜刺未查，定雷符未用。”"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善知道自己需要逐个带名册所列人员来确认传播范围，不再用生门说法解释换位。",
        "supersedes_fact_ids": [],
        "change": "胡善承诺按名册带人确认，并停止解释生门。",
        "source_evidence": "胡善小声补充：“名册所列人员，我会逐个带来确认，不再解释生门。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "investigating",
        "belief": "纪凌策已将未封铜铃位于值守廊偏东东三梁钩、低限试雷节拍进入候场区域、胡善按名册扩大传播范围等内容记入器物传播路径和人为扩大范围核查。",
        "supersedes_fact_ids": [],
        "change": "纪凌策明确记录铜铃位置、器物传播路径以及胡善扩大传播范围。",
        "source_evidence": "纪凌策抽出一张新核查页：“曹雨，未封铜铃位于值守廊偏东东三梁钩，使低限试雷节拍进入候场区域，记器物传播路径。胡善，抄录回声并按名册传给他人，致传播范围扩大，记人为扩大范围。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策认为铜铃位置、传播站位回声角度、东脊先受牵引后反卷和西脊反卷起点实质削弱裴照野主动口头泄露安全雷时的旧判断，但因第二道封签时间缺口未获正式见证，仍未正式更正原裁记。",
        "supersedes_fact_ids": [],
        "change": "裴照野主动口头泄露安全雷时的旧判断受到实质削弱，但 pei-leaked-strike-window 未正式更正。",
        "source_evidence": "纪凌策将昨日站位表压在核查页旁，依次圈出东三梁钩、偏东候场线以及东、西两脊雷痕的先后：“铜铃位置、传播站位的回声角度、东脊先受牵引后反卷、西脊反卷起点，现可列在同一页。以上事实，实质削弱裴照野主动口头泄露安全雷时的旧判断。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "investigating",
        "belief": "沈络确认裴照野右手雷麻只属部分恢复，仍需完成低负荷抄录并由沈络复核落点、颤动与经脉回响后才能解除，期间不得接触高压雷纹、不得执符笔探痕、不得独自登塔。",
        "supersedes_fact_ids": [],
        "change": "沈络将裴照野临时登记资格限制更新为取刺和定雷符后部分恢复、但尚未解除。",
        "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "纪凌策已取得值守廊见证：铜铃位于东三梁钩，铃口朝西南，酉时正前缺第二道封签。",
        "supersedes_fact_ids": [
          "unsealed-calibration-chime-at-duty-corridor"
        ],
        "change": "纪凌策取得并记录第二道封签时间缺口见证。",
        "source_evidence": "“铜铃位置？”\n\n“就在东三梁钩。铃口朝西南。”\n\n“第二道封签？”\n\n那弟子想了片刻：“酉时正前未见。第一道旧封在铃柄上，外层应加的第二道没有。酉时正换班时，我还提醒过曹师兄，说那铃风一吹便响。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "grounding-ridge-echo-delay",
        "state": "knows",
        "belief": "纪凌策确认铜铃位置、封签缺失时段、胡善名册偏东换位记录及东西脊雷痕先后已并列入核查页，四项证据能够彼此校验。",
        "supersedes_fact_ids": [
          "grounding-ridge-echo-delay"
        ],
        "change": "纪凌策将铜铃位置、封签时间、回声站位和雷痕先后合并为接近闭合的新证据链。",
        "source_evidence": "纪凌策没有接那句话，只让见证弟子在证言下按印。他把铜铃位置、铃口朝向、封签缺失时段，与胡善名册上的偏东换位记录并列，又将东、西脊雷痕先后附在后页。"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策认为旧推断方向应当推翻，现有证据已不足以支持只凭裴照野口头泄露，但原裁记需戒律堂复核签字，尚未正式更正。",
        "supersedes_fact_ids": [],
        "change": "纪凌策明确表示现有新证据足以推翻旧推断方向，但未正式更正 pei-leaked-strike-window。",
        "source_evidence": "“旧推断方向应当推翻。”纪凌策说得清楚，“现有证据已不足以支持‘只凭裴照野口头泄露’。但原裁记需戒律堂复核签字，今日不作正式更正。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "investigating",
        "belief": "沈络确认裴照野完成低负荷抄录但右手雷麻未解除，只可继续低负荷验证。",
        "supersedes_fact_ids": [
          "temporary-thunder-clerk-qualification"
        ],
        "change": "沈络将裴照野临时登记资格推进到低负荷抄录验证未解除阶段。",
        "source_evidence": "沈络查过落点、颤动和腕侧经脉回响，在样页下写道：“可继续低负荷验证，未正式解除右手雷麻。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "knows",
        "belief": "沈络确认裴照野右手雷麻已正式解除，但伤势解除不等于临时雷时登记资格恢复，仍须正式巡雷使复核且不得独自值守高压雷塔。",
        "supersedes_fact_ids": [
          "temporary-thunder-clerk-qualification"
        ],
        "change": "沈络对裴照野临时雷时登记资格作出新裁定：伤势解除但资格未恢复。",
        "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策认为铜铃位置、铃口朝向、封签时间和东西脊雷痕先后四项证据表明旧推断方向应当推翻，并已提交戒律堂核记录连续性，但原裁记尚未正式更正。",
        "supersedes_fact_ids": [],
        "change": "纪凌策将四项证据整理成待更正裁记复核文本并提交戒律堂核记录连续性。",
        "source_evidence": "“铜铃位置决定回声起点，铃口朝向决定折入候场廊的角度；封签时间说明该时段铜铃未完成封闭；东西脊雷痕先后与偏东换位名册相合。”他合上笔帽，“旧推断方向应当推翻。现将文本交戒律堂核记录连续性。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "pei-leaked-strike-window",
        "state": "investigating",
        "belief": "沈络确认四项证据可以进入正式更正流程，但受理不等于裁记更改，原裁记仍在。",
        "supersedes_fact_ids": [],
        "change": "沈络受理待更正裁记复核文本，但未正式更正原裁记。",
        "source_evidence": "“尚未更正。”沈络道，“受理不是裁记更改。复核签字未完，原裁记仍在。”"
      },
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "曹雨确认未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，酉时正前第二道封签缺失；“暂挂”不改变器物位置与封签状态。",
        "supersedes_fact_ids": [
          "unsealed-calibration-chime-at-duty-corridor"
        ],
        "change": "曹雨在复核文本中按手印确认校雷铜铃位置、朝向和封签缺失事实。",
        "source_evidence": "曹雨只得逐字写下事实，又在末尾按了手印。“暂挂”二字没能落进正文，只被纪凌策留在旁注里，标作当事人最初陈述，不改变器物位置与封签状态。"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善知道自己对候测队列作出的押雷排号式解释被沈络纳入听闻来源记录，并导致所有听过解释的人重新签收安全告示。",
        "supersedes_fact_ids": [
          "lucky-thunder-almanac-source"
        ],
        "change": "胡善关于候测队列的解释被正式转化为分组签字与责任记录。",
        "source_evidence": "沈络走到榜前：“很好。既然你已向人解释过排号，所有听过解释的人，重新签收安全告示。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "believes_false",
        "belief": "纪凌策认为旧裁记所依据的“裴照野口头泄露安全雷时”与现有事实链条不合，铜铃回声足以形成传播路径，雨中记录补齐四脊雷痕连续性，旧判断应在终签时正式更正，但此刻尚未正式更正。",
        "supersedes_fact_ids": [],
        "change": "纪凌策将雨中四脊同步刻度并入待更正裁记，并明确旧判断应在终签时正式更正。",
        "source_evidence": "他逐行核过，才道：“旧裁记所依据的‘裴照野口头泄露安全雷时’，与现有事实链条不合。铜铃回声足以形成传播路径，雨中记录又补齐了四脊雷痕连续性。我的旧判断应在终签时正式更正。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "pei-leaked-strike-window",
        "state": "investigating",
        "belief": "沈络确认本章只确认记录连续；恢复运行签字、原裁记更正和责任拆分仍须等待最终风险复核，原裁记尚未正式更正。",
        "supersedes_fact_ids": [],
        "change": "沈络未在本章落印更正裁记，将恢复运行签字、原裁记更正和责任拆分推迟到最终风险复核后。",
        "source_evidence": "沈络按住裁记末页，没有落印：“今日只确认记录连续。恢复运行签字、原裁记更正、责任拆分，等最终风险复核。”"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "rain-pause-thunder-timing-misread",
        "state": "believes_false",
        "belief": "胡善把纪凌策雨前停顿和校准页留空误读为押雷口诀。",
        "supersedes_fact_ids": [],
        "change": "胡善误读雨前停顿与校准页留空，写下新的押时内容。",
        "source_evidence": "纸上写着：风停三息，东位为吉；页留一格，逢雷宜避。"
      },
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "曹雨知道未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，且第二道封签缺失。",
        "supersedes_fact_ids": [],
        "change": "曹雨再次确认校雷铜铃位置、朝向与第二道封签缺失。",
        "source_evidence": "曹雨站在案台另一边，被问到铜铃时只答：“未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南。第二道封签缺失。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "knows",
        "belief": "纪凌策正式确认所谓安全雷时来自铜铃回声传播，不是裴照野主动口头泄露，原判断已正式更正。",
        "supersedes_fact_ids": [
          "pei-leaked-strike-window"
        ],
        "change": "纪凌策正式更正 pei-leaked-strike-window。",
        "source_evidence": "“以上证据足以证明所谓安全雷时来自铜铃回声传播，不是裴照野主动口头泄露。原判断正式更正。”"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "pei-leaked-strike-window",
        "state": "knows",
        "belief": "沈络已在更正文书与恢复运行书之间落印，接受原裁记正式更正，同时恢复运行不改变封签缺失和程序责任。",
        "supersedes_fact_ids": [
          "pei-leaked-strike-window"
        ],
        "change": "沈络结束对 pei-leaked-strike-window 的调查状态并落印确认更正。",
        "source_evidence": "沈络在更正文书与恢复运行书之间各落一印。"
      },
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "曹雨承认未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，第二道封签当时没有补齐。",
        "supersedes_fact_ids": [
          "unsealed-calibration-chime-at-duty-corridor"
        ],
        "change": "曹雨承认未封校雷铜铃位置与第二道封签缺失。",
        "source_evidence": "曹雨顿了顿：“未封校雷铜铃，曾挂在值守廊东三梁钩，铃口朝西南。第二道封签当时没有补齐。”"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善承认避雷黄历来自铜铃回声，扩大传播是他抄发的。",
        "supersedes_fact_ids": [
          "lucky-thunder-almanac-source",
          "rain-pause-thunder-timing-misread"
        ],
        "change": "胡善确认避雷黄历来源并承认扩大传播。",
        "source_evidence": "“来自铜铃回声。”胡善道，“扩大传播是我抄发的。”"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-procedure-liabilities-retained",
        "state": "knows",
        "belief": "纪凌策正式保留裴照野漏做校雷铜铃第二道封签、无正式巡雷使复核便提前低限试雷两项程序责任，修塔、维持回路与突破均不抵扣记过。",
        "supersedes_fact_ids": [],
        "change": "纪凌策在更正文书中保留裴照野两项程序责任。",
        "source_evidence": "“同时保留裴照野两项程序责任：漏做校雷铜铃第二道封签；无正式巡雷使复核便提前进行低限试雷。修塔、维持回路与突破，均不抵扣记过。”"
      }
    ],
    "thread_changes": [
      {
        "change": "共享安全雷时外泄疑云公开化，黄历抄本被统一交出核验。",
        "source_evidence": "“我先按记录判断。”纪凌策看向他，“自此刻起，你暂停单独登记高风险雷时，只在我可见范围内记录低限雷痕。所有黄历抄本交出核验。”"
      },
      {
        "change": "听雷塔修复结论暂缓，后续需完成铜铃梁钩、回声节拍和雷痕证据链核对。",
        "source_evidence": "他看向塔身未校的四处接地脊，声音沉下去：“在证据链完成前，听雷塔不作修复结论，你也不得单独登记高风险雷时。”"
      },
      {
        "change": "胡善的抄本将被逐条比对回声节拍。",
        "source_evidence": "纪凌策收起时刻簿：“裴照野，接下来在我监督下补录值守廊雷痕。曹雨，带人确认此铃挂过的梁钩。胡善的抄本，逐条比对回声节拍。”"
      },
      {
        "change": "听雷塔修复仍未完成，下一步只能通过低限试雷确认接地链错序范围。",
        "source_evidence": "“东、西两处异常成立。南、北暂不能判定完好。”\n\n曹雨问：“那便做一次低限试雷？”"
      },
      {
        "change": "裴照野泄露安全雷时的嫌疑线未正式更正，继续受封签时间缺口影响。",
        "source_evidence": "“列入核查，不等于完成证明。”纪凌策合上簿册，“在封签时间缺口补齐前，泄露安全雷时的判断不正式更正。”"
      },
      {
        "change": "胡善黄历传播责任被记录，传播人数仍待核。",
        "source_evidence": "“那两次避开，是偶合。你把校验节拍写成押时秘诀，诱使候场弟子按所谓吉位停留，增加聚集风险。记管理责任，人数待核。”"
      },
      {
        "change": "听雷塔修复线进入低压隔离、查明两脊断点、再定铜条修补方案阶段。",
        "source_evidence": "纪凌策封上停试签：“下一步先做低压隔离，查明两脊断点，再定铜条修补方案。剩余重置钉只有一枚，不得再靠试错。”"
      },
      {
        "change": "铜铃证据链尚未完整，仍需核查封签时间、错序雷痕和回声角度。",
        "source_evidence": "“铜铃位置与回声角度继续核查。封签时间另查。错序雷痕另查。”他合上时刻簿，“目前证据不足以更正裴照野泄露安全雷时的判断。”"
      },
      {
        "change": "胡善避雷黄历只允许作为节拍对照，不作为雷时记录。",
        "source_evidence": "纪凌策检查远端抄录席，又把胡善的黄历抄本翻到最早一页，搁在时刻簿旁。\n\n“此册只作节拍对照，不作雷时记录。”"
      },
      {
        "change": "听雷塔检修方向确定为先低压隔离，东脊第四扣和西脊第二扣需要导雷铜条修补，南北两脊只先做低压查验。",
        "source_evidence": "裴照野铺开四脊简图，以左手压尺，逐处口述：“东脊第四扣，西脊第二扣，先隔离。两处都需导雷铜条修补。南、北两脊只做低压查验，未查明前不定用量。”"
      },
      {
        "change": "听雷塔检修架已为东、西两脊挂上隔离牌，但铜条去向仍未填写，修补和校准尚未完成。",
        "source_evidence": "廊外云层缓缓压低。纪凌策将东、西两脊的隔离牌挂上检修架，最下方留着两处尚未填写的铜条去向。"
      },
      {
        "change": "下一步优先检查西脊第二扣，因裴照野判断反卷从那里起；西脊沟内出现细小金属绷响，提示隐患仍在。",
        "source_evidence": "裴照野看了一眼：“明日先开西脊第二扣。反卷从那里起。”\n\n检修架后，封闭的西脊沟内忽然传来一声细小的金属绷响。"
      },
      {
        "change": "曹雨的铜铃暂挂和第二道封签缺失仍造成管理责任风险，申诉格式不能消除事实后果。",
        "source_evidence": "沈络道：“位置有回声后果，时长有传播后果。自然记。”"
      },
      {
        "change": "胡善需要列出避雷黄历传播范围，传播管理责任尚未处置完成。",
        "source_evidence": "沈络指向候场登记栏：“把抄过、看过、按此换过候场位置的人名列出。不是新天机，是传播范围。”"
      },
      {
        "change": "西脊检修主线推进：主导雷链已由纪凌策封闭，低压隔离成立。",
        "source_evidence": "纪凌策把三枚隔离扣依次压下。第一扣落，主链灯纹由白转灰；第二扣落，西脊沟内绷响短了一息；第三扣落，隔离罩上浮出低压刻度，停在一寸三分。"
      },
      {
        "change": "主链封闭时明确剩余一枚重置钉只可用于全塔失控阻断，不得用于检修试错。",
        "source_evidence": "纪凌策先验主链闸牌，念道：“申时后主导雷链未封闭，现由正式巡雷使封链。听雷塔剩余重置钉一枚，只作全塔失控阻断，不得用于检修试错。”"
      },
      {
        "change": "东脊第四扣仍少半格，南北两脊未低压查验，四处接地脊尚未完成校准。",
        "source_evidence": "纪凌策收起低压盘，又把东脊标牌翻开：“东脊第四扣仍少半格。南、北两脊未低压查验。四处接地脊尚未完成校准。”"
      },
      {
        "change": "下一步检修目标转向东脊第四扣，重点查明少半格是断裂还是被西脊牵偏。",
        "source_evidence": "纪凌策合上记录册，点向东侧值守廊：“下一处，东脊第四扣。先看少的那半格，是断了，还是被西脊牵偏。”"
      },
      {
        "change": "第二道封签时间缺口仍未闭合，今日不作正式更正。",
        "source_evidence": "“第二道封签的时间缺口尚无正式见证。器物何时失去封闭、谁在何时应当补签，尚未闭合。今日不作正式更正。”"
      },
      {
        "change": "曹雨未做第二道封签的管理责任继续存在。",
        "source_evidence": "“你漏做第二道封签、无正式巡雷使复核便提前低限试雷，两项程序责任也仍在。”"
      },
      {
        "change": "裴照野漏做第二道封签和无正式巡雷使复核便提前低限试雷的程序责任继续存在。",
        "source_evidence": "“你漏做第二道封签、无正式巡雷使复核便提前低限试雷，两项程序责任也仍在。”"
      },
      {
        "change": "东、西脊修补通过和伤势好转均不抵消裴照野提前试雷、漏封等程序责任。",
        "source_evidence": "纪凌策将伤势页与程序责任页分别封好：“东、西脊修补通过，不抵提前试雷之责；伤势好转，也不抵漏封之责。”"
      },
      {
        "change": "四项证据已接近闭合：铜铃位置、酉时正前缺第二道封签、回声折入候场位、东西脊雷痕先后与调用顺序不一致。",
        "source_evidence": "“铜铃位于东三梁钩，酉时正前缺第二道封签；回声向西南折入候场位；实际雷痕为东脊先受牵引、西脊再反卷，与时刻簿调用顺序不一致。”纪凌策合上半页，“四项已经能彼此校验。”"
      },
      {
        "change": "裴照野明确承认铜铃漏第二封签的登记责任和无正式巡雷使复核提前试雷的程序责任，且证据更正不抵记过。",
        "source_evidence": "“铜铃漏第二封签，我有登记责任。无正式巡雷使复核，提前试雷，我有程序责任。”裴照野道，“证据更正，不抵记过。”"
      },
      {
        "change": "听雷塔四脊虽修补并通过低压顺序，但未逢真实雷雨、未正式校准，仍不可恢复运行。",
        "source_evidence": "裴照野答：“修补完成。低压顺序通过。未逢真实雷雨，未作正式校准。听雷塔不可恢复运行。”"
      },
      {
        "change": "最后一轮低负荷抄录复验完成，复验内容覆盖四脊同步刻度、铜铃封签时间缺口、低压导行顺序三类记录。",
        "source_evidence": "“只抄录，不探痕，不注灵，不越线。三类记录，缺一类，复验中止。”"
      },
      {
        "change": "待更正裁记复核文本已被沈络受理并准入正式更正流程，但 pei-leaked-strike-window 尚未正式更正。",
        "source_evidence": "“尚未更正。”沈络道，“受理不是裁记更改。复核签字未完，原裁记仍在。”"
      },
      {
        "change": "四脊器物修补完成且低压导行顺序通过，下一步进入真实雷雨候测队列。",
        "source_evidence": "沈络在校准申请末尾签下受理意见：“四脊器物修补完成，低压导行顺序通过。准入真实雷雨候测队列。正式校准时，纪凌策与我同时在场。”"
      },
      {
        "change": "下一章启动项为雨前布阵。",
        "source_evidence": "沈络封住申请册：“候测队列第一项，雨前布阵。”"
      },
      {
        "change": "胡善雨前误读造成候场弟子再次调整分组，并追加安全听训签收和听闻来源记录。",
        "source_evidence": "偏东组重新退回隔离线，按新表排成两列。纪凌策在附页记下挪动时刻、听闻来源和重新签收的次序。原本混在一处的候场弟子因此分得更清，连谁先听见胡善第一句、谁只听见第二句，都有了落笔处。"
      },
      {
        "change": "旧裁记更正进入终签前最后程序障碍：记录连续已确认，但恢复运行签字、原裁记更正、责任拆分均待最终风险复核。",
        "source_evidence": "沈络按住裁记末页，没有落印：“今日只确认记录连续。恢复运行签字、原裁记更正、责任拆分，等最终风险复核。”"
      },
      {
        "change": "裴照野、曹雨、胡善各自程序责任继续单列，不因校准完成、听训补做或维持回路抵消。",
        "source_evidence": "“单列。”沈络道，“校准完成不抵封签缺失。”\n\n胡善也凑近半步：“那我今日让众人重新签收，传播一项是否——”\n\n“单列。补做听训不抵扩大传播。”\n\n裴照野道：“我的两项也单列。漏第二封签，提前低限试雷。”\n\n沈络看他一眼：“记过不因你维持回路而消失。”"
      },
      {
        "change": "裴照野两项程序责任继续记过，不因修塔、维持回路或突破抵扣。",
        "source_evidence": "“同时保留裴照野两项程序责任：漏做校雷铜铃第二道封签；无正式巡雷使复核便提前进行低限试雷。修塔、维持回路与突破，均不抵扣记过。”"
      },
      {
        "change": "曹雨因未封校雷铜铃和第二道封签缺失进入管理责任处置流程。",
        "source_evidence": "“管理责任进入处置流程。”沈络道，“恢复运行不改变封签缺失。”"
      },
      {
        "change": "胡善因避雷黄历来自铜铃回声且由其扩大传播，按名册进入处置流程。",
        "source_evidence": "“来自铜铃回声。”胡善道，“扩大传播是我抄发的。”\n\n“按名册进入处置流程。”"
      },
      {
        "change": "章末资源余额封存为裴照野下品灵石二枚、定雷符一张；听雷塔重置钉一枚、导雷铜条二段，已耗资源不得返还。",
        "source_evidence": "终签册最后一页，纪凌策逐笔登记：裴照野下品灵石二枚，定雷符一张；听雷塔重置钉一枚，导雷铜条二段。余额封存承接，不得返还已耗资源。"
      }
    ],
    "comedy_changes": [
      {
        "change": "胡善把安全告示曲解成押雷秘诀，形成后续可复用的误解笑点。",
        "source_evidence": "“巡雷使明鉴，”胡善拱手，“弟子只是把告示和铃声合参。告示说不得停留三息以上，可见三息以内尚有余地；三息以后雷不认人，此乃塔中慈悲，写得含蓄。”"
      },
      {
        "change": "裴照野以“耳朵无证，胆子有证”给乱写黄历者分组，形成查案中的冷面吐槽风格。",
        "source_evidence": "“为何另列？”胡善问。\n\n“耳朵无证，胆子有证。”"
      },
      {
        "change": "胡善继续把回声与黄历解释成秘格，被裴照野用站位打断。",
        "source_evidence": "胡善从后头探脑袋：“那便是黄历秘格。眼见为反，耳听为真，西南先占——”\n\n裴照野指向地面刻度：“你站在三尺外，秘格失效。”"
      },
      {
        "change": "胡善试图把复核要点包装成新的吉位黄历，被纪凌策当场制止。",
        "source_evidence": "纪凌策按住纸角：“你抄什么？”\n\n“复核要点。”\n\n“题头为何是‘新订东廊吉位’？”\n\n“便于记忆。”\n\n纪凌策收走空纸，指向院墙最远处一张矮桌：“你去远端抄录席。只记听见几响、相隔几息，不许加吉凶。”"
      },
      {
        "change": "胡善从避雷黄历传播者变成了自己黄历的反证样本。",
        "source_evidence": "胡善只得坐回矮桌，成了自己那本黄历的反证。"
      },
      {
        "change": "曹雨对“暂借”重置钉的念头被沈络规则堵死后闭嘴。",
        "source_evidence": "曹雨的目光在“暂借”二字上停了停，识趣地闭嘴。"
      },
      {
        "change": "胡善继续把候场分组线误当避雷黄历用途，被裴照野纠正。",
        "source_evidence": "胡善抬头：“我知道。我的意思是，站在线后，东时避东，西时——”\n\n“分两组。不是黄历。”"
      },
      {
        "change": "胡善被要求只抄节拍不许添宜忌，黄历式记录被沈络纳入传播未核雷时风险。",
        "source_evidence": "裴照野将他的抄本抽走，压在远端抄录席上：“你去第二组，离铜铃回声最远。只抄听见的节拍，不许添宜忌。”\n\n胡善望着被没收的册子，迟疑道：“若恰好又对了一次呢？”\n\n沈络翻开安全复核簿：“就多记一次你传播未核雷时。”"
      },
      {
        "change": "裴照野把字写偏到责任人栏，形成本章申诉格式搞笑点。",
        "source_evidence": "纸上“东脊二刻”四字，最后一笔偏出去半寸，正好戳进“责任人”一栏。"
      },
      {
        "change": "胡善面对随机空响无法继续用黄历解释后续落雷，喜剧性地被迫承认不能预测。",
        "source_evidence": "胡善等了三息。\n\n天上很给面子地一片安静。"
      },
      {
        "change": "候场弟子按是否看过黄历、是否依黄历换位分组，胡善作为原抄人被单独归类，强化黄历传播笑点。",
        "source_evidence": "几名候场弟子原本还想问空响能否另开一页，闻言只得分成两组：看过黄历的站西栏，依黄历换过值守位置的站东栏。胡善站在两栏中间，抱着抄本，一时不知自己该归哪边。"
      },
      {
        "change": "沈络用规章式冷幽默讽刺曹雨把风险寄托给铜片懂规章。",
        "source_evidence": "沈络看他一眼：“所以先封主链。不是先祈愿铜片懂规章。”"
      },
      {
        "change": "胡善带来的名册混入拜雷式换位理由，形成荒唐笑点。",
        "source_evidence": "第一行：听见第一响，原地勿动，以免抢雷。\n第二行：听见第二响，向东挪一步，东者生门。\n第三行：若第三响迟，蹲半息，显得恭敬。"
      },
      {
        "change": "胡善把黄历被戒律堂门房压平当成报告内容，延续避雷黄历笑点。",
        "source_evidence": "话音刚落，检修区外传来胡善的声音：“我带名册，不带黄历。黄历留在戒律堂门口，被门房压着，压得很平。”"
      },
      {
        "change": "胡善把抄录并传播铜铃回声辩称为替铜铃整理措辞。",
        "source_evidence": "胡善忙道：“我也没泄露。我只是听见以后，替铜铃整理了一下措辞。”"
      },
      {
        "change": "胡善因把三声铃扩写成七行时刻被纪凌策指出扩大传播。",
        "source_evidence": "“你把三声铃整理成了七行时刻。”\n\n“我怕铜铃言简意赅，旁人看不明白。”"
      },
      {
        "change": "曹雨心疼半格缺口按一整段导雷铜条入账，被沈络以库房规则压回。",
        "source_evidence": "曹雨盯着那行字：“这半格，算一整段？”\n\n沈络道：“库房按领出算，不按你心疼多少算。”"
      },
      {
        "change": "胡善原本用来区分信黄历程度的三栏被戒律堂改造成责任和传播路径记录。",
        "source_evidence": "卷首写着三栏：听见一响就换位，听见两响才换位，没听见但跟着换位。\n\n沈络扫了一眼：“这是申诉，还是名册？”"
      },
      {
        "change": "试图把南三扣停顿解读成下一回安全时辰的弟子被沈络派去追加责任签字。",
        "source_evidence": "胡善正带人逐一按名，旁边一名弟子探头道：“南三扣处停了一息，莫非下一回安全时辰在——”\n\n沈络头也没抬：“你去名册末尾确认三名跟随换位者。确认完再回来抄安全分组，不抄时辰。”"
      },
      {
        "change": "胡善把真实雷雨候测队列误读成人员押雷排号，导致听过解释的候场弟子全部重新签收安全告示。",
        "source_evidence": "“诸位，既然有队列，便有先后。排得靠前，先借校准雷；排得靠后，或可避开余雷。依我看，偏东第四位最——”"
      },
      {
        "change": "胡善的解释被拆成分组签收表，每一次解释都进入听闻来源记录。",
        "source_evidence": "半个时辰后，新分组全部按印。胡善的每一次解释都被记入听闻来源，候场弟子也依新表分开站位。"
      },
      {
        "change": "胡善把纪凌策停三息和校准页留空误编成押雷口诀，随即被沈络改成安全禁令并要求逐人签收。",
        "source_evidence": "沈络把听训纸铺平，逐句划线：“‘风停三息，东位为吉’，改成‘风停期间不得擅自换位’。‘页留一格，逢雷宜避’，改成‘未录刻度前不得推定雷时’。你念一遍，偏东组逐人签收。”"
      },
      {
        "change": "胡善又试图把裴照野突破前兆理解为最准押雷，被纪凌策准备用传播责任记录吓回安全听训疑问。",
        "source_evidence": "胡善迟疑着举手：“这等前兆，能否算四脊校准后最准的一条押雷——”\n\n纪凌策把附页翻到传播责任补充栏：“原话再说一遍，我记听闻来源。”\n\n胡善立刻放下手：“我申请改成安全听训疑问。”"
      },
      {
        "change": "胡善误把恢复运行理解为可以重新排押雷班次。",
        "source_evidence": "胡善听见“恢复运行”，立刻从袖中抽出一张排得密密麻麻的纸：“既然恢复了，我把新押雷班次也排好了。偏东组守戌初，西廊组押戌正——”"
      },
      {
        "change": "裴照野将胡善的押雷班次改成安全听训排班，并把胡善职责改为看人和补签。",
        "source_evidence": "最后一笔落下，整张押雷班次变成了低强度安全听训排班。原黄历传播组全部编入甲组，由胡善带队退出高压值守区；未传播者编入乙组，在外廊学习接地告示。\n\n胡善捧着改完的纸：“那我这个领队，主要看哪一道雷？”\n\n裴照野指向最下方：“看人。少一个，你补签。”"
      }
    ],
    "new_constraints": [
      {
        "change": "候场弟子改为按接地刻度排队，不再按避雷黄历站位。",
        "source_evidence": "纪凌策把抄本合上：“从现在起，候场弟子按接地刻度排队，不按黄历。胡善，你承认抄录并传播铜铃回声？”"
      },
      {
        "change": "裴照野接下来必须在纪凌策监督下补录值守廊雷痕。",
        "source_evidence": "纪凌策收起时刻簿：“裴照野，接下来在我监督下补录值守廊雷痕。曹雨，带人确认此铃挂过的梁钩。胡善的抄本，逐条比对回声节拍。”"
      },
      {
        "change": "曹雨需要带人确认校雷铜铃挂过的梁钩。",
        "source_evidence": "纪凌策收起时刻簿：“裴照野，接下来在我监督下补录值守廊雷痕。曹雨，带人确认此铃挂过的梁钩。胡善的抄本，逐条比对回声节拍。”"
      },
      {
        "change": "证据链完成前，听雷塔不作修复结论。",
        "source_evidence": "他看向塔身未校的四处接地脊，声音沉下去：“在证据链完成前，听雷塔不作修复结论，你也不得单独登记高风险雷时。”"
      },
      {
        "change": "下一章低限试雷仅允许低限一刻，不得上调。",
        "source_evidence": "沈络又问：“试雷强度？”\n\n“低限一刻。”纪凌策道。\n\n“不得上调。裴照野右手不得持续接触高压雷纹，符笔偏移即停。曹雨只控校雷铜铃，不得改接地链。试雷前复核封签、清空候场廊、核对远端抄录席。”"
      },
      {
        "change": "下一次低限试雷必须由纪凌策在场复核。",
        "source_evidence": "纪凌策接过试雷令，在复核人一栏签名：“明日低限试雷，我在场。”"
      },
      {
        "change": "storm-reset-pin 两枚余额不变，其中一枚移入待命槽；不得提前启用，启用将永久消耗。",
        "source_evidence": "沈络看过编号：“两枚，只能预备一枚待命。本次不得提前启用。若接地链失序，是否启用由纪凌策当场判断。重置钉入阵即永久消耗，不返还，不补记成暂借。”"
      },
      {
        "change": "下一次试雷前必须复核封签、清空候场廊、核对远端抄录席。",
        "source_evidence": "“不得上调。裴照野右手不得持续接触高压雷纹，符笔偏移即停。曹雨只控校雷铜铃，不得改接地链。试雷前复核封签、清空候场廊、核对远端抄录席。”"
      },
      {
        "change": "曹雨下一次试雷只可控制校雷铜铃，不得改接地链。",
        "source_evidence": "“不得上调。裴照野右手不得持续接触高压雷纹，符笔偏移即停。曹雨只控校雷铜铃，不得改接地链。试雷前复核封签、清空候场廊、核对远端抄录席。”"
      },
      {
        "change": "胡善作为黄历传播者被改为远端回声样本，不得参与站位解释。",
        "source_evidence": "沈络在风险表上添了一行：“黄历传播者改为远端回声样本。不得参与站位解释。”"
      },
      {
        "change": "裴照野自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。",
        "source_evidence": "沈络按住记录页，不让他继续：“右手雷麻加重。症状，指节颤动，符笔落点偏移。自此不得独自接触高压雷纹，只许低负荷抄录、口述方向与刻度。后续先处理伤势风险。”"
      },
      {
        "change": "剩余 storm-reset-pin 只有 1 枚，不得再靠试错。",
        "source_evidence": "纪凌策封上停试签：“下一步先做低压隔离，查明两脊断点，再定铜条修补方案。剩余重置钉只有一枚，不得再靠试错。”"
      },
      {
        "change": "曹雨下一次核查必须带封签簿与铜铃维护记录说明第二道封签缺失原因。",
        "source_evidence": "沈络抬笔，在复核簿末尾添了一行：“曹雨，下一次核查带封签簿与铜铃维护记录。说明第二道封签为何缺失。”"
      },
      {
        "change": "提前试雷的既有程序风险继续保留，今日受监督试雷不抵扣此前责任。",
        "source_evidence": "沈络把另一份记录推到他面前：“提前试雷的既有程序风险也继续保留。今日受监督试雷，不抵扣此前责任。”"
      },
      {
        "change": "裴照野不得接触高压雷纹，不得执符笔探痕，不得注灵复验，只准低负荷抄录和口述方向与刻度。",
        "source_evidence": "“停止接触高压雷纹。”沈络道，“从现在起，只准低负荷抄录、口述方向与刻度。不得执符笔探痕，不得注灵复验。”"
      },
      {
        "change": "右手雷麻尚未部分恢复或解除，停止高压接触仅是恢复流程第一步。",
        "source_evidence": "沈络又在旁添了一行：“右手雷麻仍属加重状态。停止高压接触，仅为恢复流程第一步。未见部分恢复，不得解除限制。”"
      },
      {
        "change": "听雷塔剩余一枚重置钉不得用于试错。",
        "source_evidence": "“重置钉一枚。”沈络道，“不得用于试错。”"
      },
      {
        "change": "塔库现有 conductive-copper-strip 六段，本章不领用，待断点确认后才能登记去向。",
        "source_evidence": "纪凌策在东、西两脊上各画一道红线：“塔库现有导雷铜条六段，本章不领用。待断点确认后再登记去向。”"
      },
      {
        "change": "次日修塔必须先封主链并做低压隔离。",
        "source_evidence": "沈络收起复核页：“明日先封主链，做低压隔离。裴照野只口述刻度，纪凌策复核。曹雨带铜条量尺。胡善带传播名册，不带黄历。”"
      },
      {
        "change": "听雷塔剩余一枚 storm-reset-pin 仍受限制，只能用于全塔失控阻断，不得用于检修试错。",
        "source_evidence": "纪凌策先验主链闸牌，念道：“申时后主导雷链未封闭，现由正式巡雷使封链。听雷塔剩余重置钉一枚，只作全塔失控阻断，不得用于检修试错。”"
      },
      {
        "change": "裴照野仍不得执符笔探痕，不得注灵复验。",
        "source_evidence": "“未加重不是恢复。”沈络道，“继续不得执符笔探痕，不得注灵复验。”"
      },
      {
        "change": "候场弟子因偏东越线需重新分组，偏东越线者明日补安全听训。",
        "source_evidence": "“你要解释的是传播范围。”沈络把名册拍到他怀里，“候场弟子重新分组，偏东越线者明日补安全听训。你的责任范围扩大到名册所列人员。”"
      },
      {
        "change": "定雷符只用于稳定经脉，不能恢复铜条、替代接地校准或保证裴照野立刻能执笔。",
        "source_evidence": "沈络将铜刺封入证物纸：“掌侧残留铜刺，已取出。全程无高压雷纹接触。接下来用定雷符，只稳经脉，不恢复铜条，不替代接地校准，也不保证你立刻能执笔。”"
      },
      {
        "change": "裴照野右手雷麻解除前必须完成规定低负荷抄录，并由沈络复核落点、颤动与经脉回响后确认。",
        "source_evidence": "“完成规定的低负荷抄录，我复核落点、颤动与经脉回响后，再确认。此前不得接触高压雷纹，不得执符笔探痕，不得独自登塔。”"
      },
      {
        "change": "裴照野接下来南、北读数只能明日左手低负荷抄，写偏一格就停。",
        "source_evidence": "裴照野点头：“南、北读数，明日左手抄。”\n\n“低负荷。”沈络道，“写偏一格就停。”"
      },
      {
        "change": "听雷塔导雷铜条仅余两段，无富余可供试错，不许裁条试错。",
        "source_evidence": "沈络收起样页和核查页：“明日提交四脊正式低压校准申请，同时做最后一轮抄录复验。铜条只余两段，不许裁条试错。”"
      },
      {
        "change": "听雷塔未逢真实雷雨、未正式校准，仍不可恢复运行。",
        "source_evidence": "裴照野答：“修补完成。低压顺序通过。未逢真实雷雨，未作正式校准。听雷塔不可恢复运行。”"
      },
      {
        "change": "重置钉余额仍为一枚，本章未启用。",
        "source_evidence": "纪凌策则在资源账末逐项念明：“导雷铜条余额两段。重置钉余额一枚，本章未启用。裴照野下品灵石五枚，定雷符两张，均未消耗。”"
      },
      {
        "change": "裴照野下品灵石仍为五枚、定雷符仍为两张，本章均未消耗。",
        "source_evidence": "纪凌策则在资源账末逐项念明：“导雷铜条余额两段。重置钉余额一枚，本章未启用。裴照野下品灵石五枚，定雷符两张，均未消耗。”"
      },
      {
        "change": "原裁记未获沈络复核签字前仍然有效。",
        "source_evidence": "沈络接过核查页：“我先核风险、证言来源与记录连续性。未签之前，裁记仍在。”"
      },
      {
        "change": "裴照野伤势解除后，临时雷时登记仍须正式巡雷使复核，仍不得独自值守高压雷塔。",
        "source_evidence": "“伤势解除，不等于资格恢复。裴照野仍为炼气五层。临时雷时登记，须正式巡雷使复核；不得独自值守高压雷塔。”"
      },
      {
        "change": "裴照野漏做校雷铜铃第二道封签和无正式巡雷使复核便提前低限试雷的程序责任继续记过。",
        "source_evidence": "“还有，”沈络看着他，“漏做校雷铜铃第二道封签，以及无正式巡雷使复核便提前低限试雷，继续记过。”"
      },
      {
        "change": "曹雨铜铃未封管理责任、裴照野程序责任、胡善扩大回声传播范围责任均不被证据推进抵消。",
        "source_evidence": "她又翻到责任分栏：“曹雨，铜铃未封管理责任单列。裴照野，漏做第二道封签与提前试雷程序责任单列。胡善，扩大回声传播范围，按名册逐人处置。任何一项证据推进，都不抵消这三栏。”"
      },
      {
        "change": "四处接地脊正式校准必须在正式巡雷使、戒律堂复核官同时在场时进行。",
        "source_evidence": "榜上写的是：四处接地脊正式校准申请已受理，列入真实雷雨候测队列。校准时须正式巡雷使、戒律堂复核官同时在场。"
      },
      {
        "change": "听雷塔导雷铜条余额二段，不得用于校准试错；重置钉余额一枚，仅供全塔失控阻断，不得用于检修试错。",
        "source_evidence": "她又添了一行风险限制：“导雷铜条余额二段，不得用于校准试错；重置钉余额一枚，仅供全塔失控阻断，不得用于检修试错。”"
      },
      {
        "change": "本章资源封匣未开启：导雷铜条余额两段，重置钉余额一枚，灵石与定雷符未启用。",
        "source_evidence": "沈络检查总断纹与资源封匣，封签均未开启：“导雷铜条未动，余额两段。重置钉未动，余额一枚。灵石与定雷符未启用。”"
      },
      {
        "change": "裴照野下品灵石余额五枚、定雷符余额两张，本章均未消耗；若第十章风险复核通过，突破需按三枚灵石、一张定雷符正式流程监督。",
        "source_evidence": "沈络核完最后一遍封匣：“下品灵石五枚，定雷符两张，均未消耗。明日若风险复核通过，再按三枚灵石、一张定雷符的正式流程监督突破。塔的最终运行签字与裁记更正也在明日处理。”"
      },
      {
        "change": "听雷塔库存导雷铜条两段和重置钉一枚不得用于校准试错，重置钉只作失控阻断。",
        "source_evidence": "纪凌策核对封匣：“裴照野下品灵石五枚，定雷符两张，今日不启用。塔库存导雷铜条两段，重置钉一枚，只作失控阻断，不作校准试错。”"
      },
      {
        "change": "南脊慢差不允许先补铜，异常必须先停，不能用库存试错。",
        "source_evidence": "沈络点头：“南脊若慢，不许先补铜。全程异常先停。”"
      },
      {
        "change": "第十章前听雷塔仍待终签，不得高压独立值守。",
        "source_evidence": "听雷塔的阵光渐渐收拢，却没有转入运行标识。塔门上仍悬着“待终签，不得高压独立值守”的戒律牌。"
      },
      {
        "change": "裴照野今夜不得冲关，下一道雷来前必须先做最终风险复核。",
        "source_evidence": "“今夜不冲关。下一道雷来前，先做最终风险复核。”"
      },
      {
        "change": "裴照野突破后不能独自值守高压雷塔，只能在正式巡雷使复核下进行低强度接地检查。",
        "source_evidence": "“症状：停雷后仍闻双重雷声，落雷时刻判断延迟。活动限制：三日内不得独自值守高压雷塔。每日仅准在正式巡雷使复核下进行低强度接地检查。”"
      },
      {
        "change": "听雷塔恢复为可复核运行状态不等于全面开放，高压值守仍须正式巡雷使主持。",
        "source_evidence": "“听雷塔自此恢复为可复核运行状态。不是全面开放。高压值守仍须正式巡雷使主持。”"
      },
      {
        "change": "裴照野突破后能力边界限定为可同时维持主塔与一处接地脊，不能替代器物复核或责任裁定。",
        "source_evidence": "沈络看了一眼阵纹：“境界确认，炼气六层。能力边界：可同时维持主塔与一处接地脊。器物仍按器物复核，责任仍按责任裁定。”"
      },
      {
        "change": "已耗资源不得返还；听雷塔剩余重置钉一枚、导雷铜条二段封存承接。",
        "source_evidence": "终签册最后一页，纪凌策逐笔登记：裴照野下品灵石二枚，定雷符一张；听雷塔重置钉一枚，导雷铜条二段。余额封存承接，不得返还已耗资源。"
      }
    ],
    "resolved_constraints": [
      {
        "change": "西脊第二扣反卷起点已被截断，西脊该处低压回路不再倒窜。",
        "source_evidence": "低压灯纹沿西脊走了一圈，至第二扣不再倒窜，灰蓝线顺着接地扣入沟底，停在正刻。"
      },
      {
        "change": "裴照野右手雷麻及其导致的右手低负荷落点限制正式解除。",
        "source_evidence": "“right-hand-thunder-numbness，右手雷麻，今日正式解除。依据四项：其一，停止接触高压雷纹；其二，掌侧残留铜刺已取出；其三，此前消耗一张定雷符稳定经脉；其四，完成低负荷抄录复验，食指、中指无落点偏移。”"
      },
      {
        "change": "裴照野突破前停止加压、不能借余雷强冲的限制因正式监督突破流程完成而解除。",
        "source_evidence": "沈络逐项落印：“四脊已校准，旧伤已解除，真实雷雨中的完整接地回路已维持。准许裴照野在正式巡雷使监督下突破。只准守回路，不准接管高压雷时，不准独自登塔。”"
      }
    ]
  },
  "structured_state": {
    "cultivation": [
      {
        "subject_id": "cao-yu",
        "stage": "炼气四层",
        "abilities": [
          "校雷铜铃清洁",
          "浅层接地纹维护"
        ],
        "injuries": [],
        "limits": [
          "无权修改正式雷时、封签或值守记录"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "hu-shan",
        "stage": "炼气四层",
        "abilities": [
          "基础引气",
          "落雷时刻速记"
        ],
        "injuries": [],
        "limits": [
          "不得接触巡雷封签、接地阵枢或高压塔区"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "ji-lingce",
        "stage": "炼气六层",
        "abilities": [
          "正式巡雷",
          "封签复核",
          "雷时调用日志审查"
        ],
        "injuries": [],
        "limits": [
          "必须依据正式记录和可复核证据更正裁定"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "pei-zhaoye",
        "stage": "炼气六层",
        "abilities": [
          "接地小周天",
          "基础听雷塔登记",
          "裴照野在不触碰雷纹、不执笔、不注灵、不越线的低负荷条件下，继续以雷痕辨序口述西脊残痕方向、逆行时长和扣位异常，并被纪凌策代录。",
          "裴照野突破后获得同时维持主塔与一处接地脊的能力，且该能力不能替代器物复核或责任裁定。"
        ],
        "injuries": [],
        "limits": [
          "临时雷时登记必须由正式巡雷使复核",
          "可同时维持主塔与一处接地脊，不能同时维持超过一处接地脊。",
          "突破后新增 post-breakthrough-thunder-echo，裴照野停雷后仍听见双重雷声，并出现落雷时刻判断延迟。",
          "solo-high-voltage-tower-ban 更新为三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查。",
          "solo-high-risk-thunder-registration-suspension 更新为裴照野不再报雷时，正式记录由纪凌策接管，裴照野只报雷痕方向。"
        ],
        "tracked_states": [
          {
            "state_id": "one-ridge-simultaneous-maintenance",
            "kind": "ability",
            "description": "裴照野突破后获得同时维持主塔与一处接地脊的能力，且该能力不能替代器物复核或责任裁定。"
          },
          {
            "state_id": "one-ridge-simultaneous-maintenance-limit",
            "kind": "restriction",
            "description": "可同时维持主塔与一处接地脊，不能同时维持超过一处接地脊。"
          },
          {
            "state_id": "post-breakthrough-thunder-echo",
            "kind": "restriction",
            "description": "突破后新增 post-breakthrough-thunder-echo，裴照野停雷后仍听见双重雷声，并出现落雷时刻判断延迟。"
          },
          {
            "state_id": "solo-high-risk-thunder-registration-suspension",
            "kind": "restriction",
            "description": "solo-high-risk-thunder-registration-suspension 更新为裴照野不再报雷时，正式记录由纪凌策接管，裴照野只报雷痕方向。"
          },
          {
            "state_id": "solo-high-voltage-tower-ban",
            "kind": "restriction",
            "description": "solo-high-voltage-tower-ban 更新为三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查。"
          },
          {
            "state_id": "thunder-mark-sequencing",
            "kind": "ability",
            "description": "裴照野在不触碰雷纹、不执笔、不注灵、不越线的低负荷条件下，继续以雷痕辨序口述西脊残痕方向、逆行时长和扣位异常，并被纪凌策代录。"
          }
        ],
        "last_kind": "restriction",
        "last_change": "solo-high-risk-thunder-registration-suspension 更新为裴照野不再报雷时，正式记录由纪凌策接管，裴照野只报雷痕方向。"
      },
      {
        "subject_id": "shen-luo",
        "stage": "炼气七层",
        "abilities": [
          "戒律堂安全复核",
          "高压雷塔停机裁定"
        ],
        "injuries": [],
        "limits": [
          "不能因救场、修塔或突破免除已确认的程序违规"
        ],
        "tracked_states": []
      }
    ],
    "resources": [
      {
        "owner_id": "pei-zhaoye",
        "resource_id": "grounding-talisman",
        "amount": 1.0,
        "unit": "张",
        "last_operation": "consume",
        "last_source_or_destination": "炼气五层突破至炼气六层时稳定雷意"
      },
      {
        "owner_id": "pei-zhaoye",
        "resource_id": "low-grade-spirit-stone",
        "amount": 2.0,
        "unit": "枚",
        "last_operation": "consume",
        "last_source_or_destination": "炼气五层突破至炼气六层"
      },
      {
        "owner_id": "thunder-tower",
        "resource_id": "conductive-copper-strip",
        "amount": 2.0,
        "unit": "段",
        "last_operation": "consume",
        "last_source_or_destination": "北脊第一扣加固"
      },
      {
        "owner_id": "thunder-tower",
        "resource_id": "storm-reset-pin",
        "amount": 1.0,
        "unit": "枚",
        "last_operation": "consume",
        "last_source_or_destination": "阻断低限试雷错序引发的接地链反卷"
      }
    ],
    "knowledge": [
      {
        "character_id": "cao-yu",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "曹雨承认未封校雷铜铃曾挂在值守廊东三梁钩，铃口朝西南，第二道封签当时没有补齐。",
        "last_change": "曹雨承认未封校雷铜铃位置与第二道封签缺失。"
      },
      {
        "character_id": "hu-shan",
        "fact_id": "lucky-thunder-almanac-source",
        "state": "knows",
        "belief": "胡善承认避雷黄历来自铜铃回声，扩大传播是他抄发的。",
        "last_change": "胡善确认避雷黄历来源并承认扩大传播。"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "grounding-ridge-echo-delay",
        "state": "knows",
        "belief": "纪凌策确认铜铃位置、封签缺失时段、胡善名册偏东换位记录及东西脊雷痕先后已并列入核查页，四项证据能够彼此校验。",
        "last_change": "纪凌策将铜铃位置、封签时间、回声站位和雷痕先后合并为接近闭合的新证据链。"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "hu-shan-copied-chime-echo",
        "state": "knows",
        "belief": "纪凌策通过黄历、试雷记录和真实雷雨记录比对，确认黄历所抄主要对应低限试雷铜铃节拍而非随机落雷。",
        "last_change": "纪凌策完成对胡善黄历来源的当场比对。"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-leaked-strike-window",
        "state": "knows",
        "belief": "纪凌策正式确认所谓安全雷时来自铜铃回声传播，不是裴照野主动口头泄露，原判断已正式更正。",
        "last_change": "纪凌策正式更正 pei-leaked-strike-window。"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "pei-procedure-liabilities-retained",
        "state": "knows",
        "belief": "纪凌策正式保留裴照野漏做校雷铜铃第二道封签、无正式巡雷使复核便提前低限试雷两项程序责任，修塔、维持回路与突破均不抵扣记过。",
        "last_change": "纪凌策在更正文书中保留裴照野两项程序责任。"
      },
      {
        "character_id": "ji-lingce",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "纪凌策已取得值守廊见证：铜铃位于东三梁钩，铃口朝西南，酉时正前缺第二道封签。",
        "last_change": "纪凌策取得并记录第二道封签时间缺口见证。"
      },
      {
        "character_id": "pei-zhaoye",
        "fact_id": "shared-safe-window-origin",
        "state": "knows",
        "belief": "裴照野确认避雷黄历来源是校雷铜铃回声节拍，不是后续随机天雷时刻。",
        "last_change": "裴照野对黄历来源的调查从怀疑转为确认。"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "low-limit-test-thunder-procedure",
        "state": "knows",
        "belief": "沈络批准下一章仅可进行低限一刻试雷，须纪凌策在场复核，storm-reset-pin 预备待命但不得提前启用，启用后永久消耗。",
        "last_change": "沈络正式限定下一次试雷程序和重置钉启用条件。"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "pei-leaked-strike-window",
        "state": "knows",
        "belief": "沈络已在更正文书与恢复运行书之间落印，接受原裁记正式更正，同时恢复运行不改变封签缺失和程序责任。",
        "last_change": "沈络结束对 pei-leaked-strike-window 的调查状态并落印确认更正。"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "temporary-thunder-clerk-qualification",
        "state": "knows",
        "belief": "沈络确认裴照野右手雷麻已正式解除，但伤势解除不等于临时雷时登记资格恢复，仍须正式巡雷使复核且不得独自值守高压雷塔。",
        "last_change": "沈络对裴照野临时雷时登记资格作出新裁定：伤势解除但资格未恢复。"
      },
      {
        "character_id": "shen-luo",
        "fact_id": "unsealed-calibration-chime-at-duty-corridor",
        "state": "knows",
        "belief": "沈络确认校雷铜铃的非正式悬位实际参与回声传递，第二道封签缺失。",
        "last_change": "沈络将曹雨所称暂挂的铜铃记录为实际参与回声传递且缺失第二道封签。"
      }
    ]
  },
  "next_chapter_inputs": [
    "裴照野已从炼气五层突破至炼气六层，能力边界为可同时维持主塔与一处接地脊。",
    "裴照野新增 post-breakthrough-thunder-echo：停雷后仍闻双重雷声，落雷时刻判断延迟。",
    "裴照野三日内不得独自值守高压雷塔，每日仅准在正式巡雷使复核下进行低强度接地检查；雷时口令由纪凌策接管。",
    "听雷塔已恢复为可复核运行状态，但不是全面开放，高压值守仍须正式巡雷使主持。",
    "听雷塔终签已落，塔门重新开启半扇，高压值守位仍空着。",
    "pei-leaked-strike-window 已由纪凌策依据铜铃位置、雷痕先后、封签时间和回声角度正式更正：裴照野没有主动口头泄露安全雷时。",
    "裴照野漏做校雷铜铃第二道封签、无正式巡雷使复核便提前进行低限试雷两项程序责任继续记过，修塔、维持回路与突破均不抵扣。",
    "曹雨承认未封校雷铜铃曾挂在值守廊东三梁钩且第二道封签未补齐，管理责任进入处置流程。",
    "胡善承认避雷黄历来自铜铃回声且扩大传播是其抄发，按名册进入处置流程。",
    "胡善的押雷班次已被改写为低强度安全听训排班，原黄历传播组编入甲组并退出高压值守区，未传播者编入乙组在外廊学习接地告示。",
    "章末资源余额：裴照野 low-grade-spirit-stone 2 枚、grounding-talisman 1 张；听雷塔 storm-reset-pin 1 枚、conductive-copper-strip 2 段；已耗资源不得返还。",
    "right-hand-thunder-numbness 已在突破前正式解除，突破未被记作治伤原因。"
  ],
  "deviations": [],
  "last_source_draft": "chapters/0010/draft.final.md",
  "last_source_sha256": "59075f66a4ac93a32f2e4913df75b5ac0fa6239bcebac0d2a8d9145ba4e8760d",
  "source": "chapters/0010/state-event.json"
}
```
