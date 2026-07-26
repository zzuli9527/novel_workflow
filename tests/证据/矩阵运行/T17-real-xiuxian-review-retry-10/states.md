# 逐章正式状态事件

## 第 1 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0001",
  "chapter": 1,
  "source_draft": "chapters/0001/draft.final.md",
  "source_sha256": "7e96df9e5f4a1d80abb431b3e56dbeafc5c207b594473a259b88b9844319509c",
  "entity_changes": [
    {
      "change": "第一轮试炼中止，所有考生须原地闭目并依座次退出，且不得交谈、交换纸笔或毁弃随身物。",
      "source_evidence": "“第一轮试炼中止。”他声音不高，却盖住了所有争辩，“所有考生原地闭目，依座次退出。不得交谈，不得交换纸笔，不得毁弃随身物。”"
    },
    {
      "change": "二十四块座次牌背面新增每名考生在雾桥上的位置与绕行次序。",
      "source_evidence": "薛简取出封签，先封阵门，又令执役弟子按座次领人。原本只记姓名的二十四块座次牌，被他逐一翻到背面，添上每人在雾桥上的位置与绕行次序。"
    },
    {
      "change": "唐桥的运气图被发现，其路线与第一层泥沼幻象外沿和三处雾坑位置相近。",
      "source_evidence": "那道弯线并不精确，却恰好从第一层泥沼幻象的外沿绕过；三团墨点的位置，也和开场最容易触发的三处雾坑相近。"
    },
    {
      "change": "运气图、警示抄本、座次牌和行动次序被分列封存，第一轮重排时辰被记入，考生后续心境关取消并转送候场廊分区看管。",
      "source_evidence": "封签一张接一张落下。运气图、警示抄本、座次牌和行动次序被分列封存，第一轮重排的时辰也一并记入。考生原定的后续心境关全部取消，转送候场廊分区看管。"
    },
    {
      "change": "候场廊三处分区门合拢，唐桥的运气图被夹入证物册。",
      "source_evidence": "最后一道封签落在主镜铜框上。候场廊三处分区门同时合拢，唐桥的运气图被夹入证物册，露出的那截弯线，正贴着雾桥陷阱的边缘。"
    }
  ],
  "relationship_changes": [
    {
      "change": "薛简公开判断岑照涉嫌向同乡考生泄露第一层路线。",
      "source_evidence": "“流程要求先核名册，再由正式监考复签。你提前启阵，没有复核签；随后与安全路线相似的图出现在候场考生手里。主镜封签未破，外人无法直接接触阵图。依现有记录，我有理由判断，你涉嫌向同乡考生泄露第一层路线。”"
    },
    {
      "change": "薛简将岑照视为涉事监考，允许查残痕但不许岑照独查。",
      "source_evidence": "“可以查，但不是现在由你独查。”薛简把调用册合上，“你已是涉事监考。”"
    },
    {
      "change": "安苇介入后要求先封存证据，不先裁定动机。",
      "source_evidence": "安苇点头：“先封存，不先定动机。主镜、座次牌、调用册、考生纸片，分别加双签。候场廊内与反光有关的器物原位封住，任何人不得挪动。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照的左眼镜灼复发，出现刺痛、重影、神识刺痛和距离误判，并导致他不能保证下一次不误触阵枢。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇问：“旧伤？”\n\n“左眼镜灼。”\n\n“方才发生距离误判？”\n\n“是。”\n\n“能否保证下一次不误触阵枢？”\n\n岑照没有辩解：“不能保证。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照临时监考资格尚未冻结但进入风险复核；结果出来前不得单独操作镜阵，不得独自进入深层幻境；辨残痕须有正式监考在场并记录角度与时长。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇又看向岑照：“你的临时监考资格尚未冻结，但已进入风险复核。在结果出来前，不得单独操作镜阵，不得独自进入深层幻境。需要辨残痕，须由正式监考在场，并记录你所看角度与时长。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "believes_false",
      "belief": "薛简依据岑照提前启阵且无正式监考复核、唐桥等同乡关系、主镜封签未破以及相似路线图出现在候场考生手里，判断岑照涉嫌向同乡考生泄露第一层路线。",
      "supersedes_fact_ids": [],
      "change": "薛简公开提出岑照涉嫌向同乡考生泄露第一层路线的判断。",
      "source_evidence": "“流程要求先核名册，再由正式监考复签。你提前启阵，没有复核签；随后与安全路线相似的图出现在候场考生手里。主镜封签未破，外人无法直接接触阵图。依现有记录，我有理由判断，你涉嫌向同乡考生泄露第一层路线。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "investigating",
      "belief": "岑照认为调用记录只能证明自己启过阵，不能证明路线从自己这里出去；主镜、节点和廊下器物留下的残痕方向与先后可用于追查路线来源。",
      "supersedes_fact_ids": [],
      "change": "岑照提出应查主镜、节点和廊下器物残痕的方向与先后。",
      "source_evidence": "岑照没有看考生，只看调用册：“记录能证明我启过阵，不能证明路线从我这里出去。先查残痕。灵力经过主镜、节点和廊下器物，方向与先后会留下。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "investigating",
      "belief": "安苇认定岑照临时监考资格尚未冻结但已进入风险复核，后续不得单独操作镜阵或独自进入深层幻境，辨残痕必须由正式监考在场并记录角度与时长。",
      "supersedes_fact_ids": [],
      "change": "安苇明确岑照临时监考资格进入风险复核。",
      "source_evidence": "安苇又看向岑照：“你的临时监考资格尚未冻结，但已进入风险复核。在结果出来前，不得单独操作镜阵，不得独自进入深层幻境。需要辨残痕，须由正式监考在场，并记录你所看角度与时长。”"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "conceals",
      "belief": "唐桥承认运气图是照着候场廊下反光所画，并承认同组都看过、邻组有人借去看，但未承认接触正式考题。",
      "supersedes_fact_ids": [],
      "change": "唐桥声称运气图来源于候场廊下反光，并承认图被同组和邻组考生看过。",
      "source_evidence": "“同组的都看过。邻组有人借去，说只看铜钱，不看路线。”"
    }
  ],
  "thread_changes": [
    {
      "change": "第一轮试炼因二十四名考生集体绕开同一路线而中止，并转入依座次退出和封存核查流程。",
      "source_evidence": "“第一轮试炼中止。”他声音不高，却盖住了所有争辩，“所有考生原地闭目，依座次退出。不得交谈，不得交换纸笔，不得毁弃随身物。”"
    },
    {
      "change": "考场异常升级为岑照涉嫌泄露第一层路线的正式核查。",
      "source_evidence": "“流程要求先核名册，再由正式监考复签。你提前启阵，没有复核签；随后与安全路线相似的图出现在候场考生手里。主镜封签未破，外人无法直接接触阵图。依现有记录，我有理由判断，你涉嫌向同乡考生泄露第一层路线。”"
    },
    {
      "change": "岑照申请从座次、封签和调用记录开始核验，再在监督下查看主镜残痕。",
      "source_evidence": "岑照睁开右眼：“我申请从座次、封签和调用记录开始核验，再在监督下查看主镜残痕。”"
    },
    {
      "change": "安苇暂未准许岑照立即动手，要求先把现场封完整。",
      "source_evidence": "“准许提出，不等于准许立即动手。”安苇道，“先把现场封完整。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥把“不得触碰左侧雾桥”的安全警示理解为押题提示，推导出左侧必有题眼、安全处在右。",
      "source_evidence": "唐桥谨慎地指向那块警示牌：“不得触碰左侧雾桥。字面上是不许碰，深意自然是左侧必有题眼。既然题眼在左，安全处便在右。如今又叫我们别动，可见动者有失。”"
    },
    {
      "change": "唐桥把考生贴右侧遇险后被监考救回，也解释成右侧是生路。",
      "source_evidence": "这一弹牵动整队。前后六人撞成一串，唐桥被挤得抱住桥柱，仍不忘高声提醒：“看见没有，右侧虽险，却有监考相救，果然是生路！”"
    },
    {
      "change": "有考生抄下警示牌并加注“左侧必有题眼，右行三步”，与二十四人在桥上的动作一致。",
      "source_evidence": "薛简把他的纸也收走。纸上端端正正写着“不得触碰左侧雾桥”，下面另加一行小字：左侧必有题眼，右行三步。\n\n这行小字与二十四人在桥上的动作分毫不差。"
    }
  ],
  "new_constraints": [
    {
      "change": "岑照不得再动主镜。",
      "source_evidence": "“所以才停。”薛简看向他，“你不得再动主镜。”"
    },
    {
      "change": "主镜、座次牌、调用册、考生纸片须分别加双签；候场廊内与反光有关的器物须原位封住，任何人不得挪动。",
      "source_evidence": "安苇点头：“先封存，不先定动机。主镜、座次牌、调用册、考生纸片，分别加双签。候场廊内与反光有关的器物原位封住，任何人不得挪动。”"
    },
    {
      "change": "岑照临时监考资格尚未冻结但进入风险复核；结果出来前不得单独操作镜阵，不得独自进入深层幻境；辨残痕须由正式监考在场并记录角度与时长。",
      "source_evidence": "安苇又看向岑照：“你的临时监考资格尚未冻结，但已进入风险复核。在结果出来前，不得单独操作镜阵，不得独自进入深层幻境。需要辨残痕，须由正式监考在场，并记录你所看角度与时长。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "第一轮试炼已中止，考生依座次退出并转送候场廊分区看管。",
    "运气图、警示抄本、座次牌、行动次序、主镜、调用册、考生纸片及候场廊反光相关器物已封存或被要求封存。",
    "薛简依据提前启阵无复核、同乡关系、主镜封签未破和相似路线图，公开判断岑照涉嫌向同乡考生泄露第一层路线。",
    "岑照的 left-eye-mirror-burn 复发，出现左眼重影、神识刺痛、距离误判，并承认不能保证下一次不误触阵枢。",
    "安苇认定岑照临时监考资格尚未冻结但进入风险复核；岑照不得单独操作镜阵或独自进入深层幻境，辨残痕须有正式监考在场并记录。",
    "岑照申请从座次、封签和调用记录开始核验，再在监督下查看主镜残痕；安苇要求先把现场封完整。"
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
  "source_sha256": "25c1528f2af76b1c792a087421677c7fec235b619a81c1274d1b01cad14e284e",
  "entity_changes": [
    {
      "change": "座次核对确认绕过开场落藤陷阱的十一名考生中只有两名来自临川郡，绕行人群并非都与岑照同乡。",
      "source_evidence": "一块块座次牌移到封存桌左侧。绕过开场落藤陷阱的十一名考生中，只有唐桥和另外一人来自临川郡，另有三人此前同岑照说过话，却只是进场时问过警示牌能不能抄。"
    },
    {
      "change": "主镜残痕显示安全纹路在第一批考生入场前已有回照，且残痕经过候场副镜方向。",
      "source_evidence": "岑照看向主镜下方的启阵时标。银纹重影晃了一下，他退开半步，重新对准：“早于第一批考生入场。部分第一层安全纹路，在他们进场前已经留下回照残痕。”"
    },
    {
      "change": "候场廊校准副镜在特定复原角度下能把第一层安全纹路的一部分反射到唐桥纸面上。",
      "source_evidence": "一道极淡的银光从副镜边缘斜落下来，在纸上折出三段断续细线。它们拼不成完整路线，却恰好显出落藤区左侧的空隙、石壁转角和第一处安全落脚点。"
    },
    {
      "change": "阮青承认校准副镜在开考前辰时二刻左右暂放候场廊，且未能回答何时封存。",
      "source_evidence": "安苇问：“副镜为何在这里？”\n\n“校准后暂放。”\n\n“何时开始暂放？”\n\n阮青抿了抿唇：“开考前。”\n\n“具体。”\n\n“辰时二刻左右。”\n\n“何时封存？”\n\n阮青没答。"
    },
    {
      "change": "唐桥承认自己画的运气图前三折来自副镜反光显示的三段线，后一笔是自己添的。",
      "source_evidence": "唐桥盯着纸面，神色难得认真：“我画的就是这三折。后面那一笔，是我觉得三折不够吉利，添的。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "同乡关系作为岑照泄露路线证据的权重被下调，但薛简仍未排除岑照嫌疑。",
      "source_evidence": "薛简收拢座次牌：“同乡证据权重下调。封签未破、提前调用和图中路线相似，仍需核查。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "照痕辨序在本次监督使用中再次确认只能判断残痕方向和先后，不能认人、定动机或识别传播者。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“能否认出唐桥的灵力？”\n\n“不能。纸上也没有他的灵力可供比照。照痕辨序只认划痕方向和先后，不认人。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照的左眼镜灼仍处于活动状态，观察主镜残痕时出现刺痛加深、银线重影一分为三和距离误判。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "左眼的刺痛忽然加深，主镜边缘那道银线一分为三。岑照立即收回神识，手掌撑住旁边的木栏，却因重影按空了半掌。"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "因镜灼症状未减，安苇禁止岑照追加观察，本次未看完的残痕需留待受控复测。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇记下时长：“不足半刻。镜灼症状未减，不许追加观察。”\n\n岑照缓了两息：“还有一道残痕，方向连向第一处回声节点，没看完。”\n\n“留待受控复测。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "investigating",
      "belief": "安苇确认岑照仍在风险复核中；现有线索不能认定传播者，也不能排除岑照，并且岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动试场，两项已列入程序责任复核清单。",
      "supersedes_fact_ids": [],
      "change": "安苇将岑照两项程序瑕疵正式列入复核清单，并维持对岑照的受限复核安排。",
      "source_evidence": "安苇提笔，字迹一笔一画压在册页上：“岑照漏做候场副镜第二道封镜检查；无正式监考复核，提前启动试场。两项列入程序责任复核清单。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "investigating",
      "belief": "岑照已确认候场副镜反光能形成唐桥运气图的一部分，但镜子只负责反光，唐桥、阮青和岑照各自仍需说明画图、放置副镜和未检查的责任。",
      "supersedes_fact_ids": [],
      "change": "岑照把路线来源调查推进到候场副镜反光、唐桥画出内容、阮青放置副镜和自己漏查并行的方向。",
      "source_evidence": "岑照按着仍在刺痛的左眼：“镜子只负责反光，不负责供词。你负责把看见的画出去，阮青负责解释它为何在这里，我负责解释为何没查。”"
    },
    {
      "character_id": "ruan-qing",
      "fact_id": "unsealed-calibration-mirror",
      "state": "conceals",
      "belief": "阮青已承认校准副镜开考前辰时二刻左右暂放候场廊，但仍回避何时封存以及为何没有上报。",
      "supersedes_fact_ids": [],
      "change": "阮青不再完全隐瞒副镜暂放候场廊的事实，但仍隐瞒或回避未封存、未上报的具体责任与动机。",
      "source_evidence": "安苇转向阮青：“副镜为何未封？”\n\n阮青低声道：“开考催得急。主镜校准差一轮，我要回去补纹，便先放在这里。”\n\n“为何没有上报？”\n\n“我以为只是暂时——”\n\n“暂时的结束时刻。”\n\n阮青沉默。"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "knows",
      "belief": "唐桥知道自己运气图前三折来自候场廊副镜反光，后一笔是自己觉得不够吉利而添上，但仍未承认知道它对应正式试炼路线。",
      "supersedes_fact_ids": [
        "lucky-route-sketch-source"
      ],
      "change": "唐桥从隐瞒运气图来源变为当场承认所画前三折来自副镜反光，旧的隐瞒状态被淘汰。",
      "source_evidence": "唐桥盯着纸面，神色难得认真：“我画的就是这三折。后面那一笔，是我觉得三折不够吉利，添的。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "suspects",
      "belief": "薛简已下调同乡证据权重，但仍依据主镜封签未破、提前调用、图中路线相似和提前试场可能造成纹路外泄，怀疑岑照与路线外泄有关。",
      "supersedes_fact_ids": [
        "cen-leaked-exam-route"
      ],
      "change": "薛简不再坚持单纯同乡泄露链条成立，转为维持对岑照提前试场放出纹路可能性的嫌疑，旧的错误判断被同一事实更新替代。",
      "source_evidence": "薛简重新封住副镜：“现有线索削弱了同乡泄露这一条，却没有排除岑照借提前试场放出纹路的可能。主镜封签未破，调用记录仍成立。判断暂不更改。”"
    }
  ],
  "thread_changes": [
    {
      "change": "调查线从岑照向同乡泄露路线，扩展为座次传播范围、主镜残痕先后、候场副镜反光和程序责任并行。",
      "source_evidence": "安苇把空纸压住：“反光能解释部分图形，不能解释图如何转手，也不能证明你是否知道它对应试炼路线。”"
    },
    {
      "change": "主镜还有一道未看完的残痕连向第一处回声节点，成为下一步低限度试场复测的核心线索。",
      "source_evidence": "他望向封存区内沉暗的主镜。\n\n“先查清楚，回到主镜的那道残痕，为什么还连着第一处回声节点。”"
    },
    {
      "change": "次日将进行低限度试场复测，薛简掌控封签和调用，岑照只能受限辨序，阮青需交代副镜移动准确时间。",
      "source_evidence": "安苇收起复核册：“明日进行低限度试场复测。薛简掌控封签和调用，岑照只做受限辨序。阮青在启阵前交代副镜从维护架移到候场廊的准确时间。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥坚持运气图只负责运气不负责作弊，触发岑照要求复原他画图时的站位、朝向和纸面高度。",
      "source_evidence": "唐桥赶紧道：“复核官，那图只负责运气，不负责作弊。”\n\n岑照看了他一眼：“运气站哪儿？”\n\n唐桥一怔：“什么？”\n\n“你画图时站哪儿，脸朝哪边，纸放多高。”"
    },
    {
      "change": "唐桥用“运气”调侃封签空白，被薛简直接压回实测站位。",
      "source_evidence": "唐桥替他看了看空白的封签位：“从运气上说，似乎一直没封。”\n\n薛简道：“你只负责站回东三位。”"
    },
    {
      "change": "岑照把反光线索归纳成“镜子只负责反光，不负责供词”，将荒谬申诉转化为责任分摊。",
      "source_evidence": "岑照按着仍在刺痛的左眼：“镜子只负责反光，不负责供词。你负责把看见的画出去，阮青负责解释它为何在这里，我负责解释为何没查。”"
    }
  ],
  "new_constraints": [
    {
      "change": "岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动试场，两项进入程序责任复核清单。",
      "source_evidence": "安苇提笔，字迹一笔一画压在册页上：“岑照漏做候场副镜第二道封镜检查；无正式监考复核，提前启动试场。两项列入程序责任复核清单。”"
    },
    {
      "change": "阮青关于校准副镜未上报原因仍待核查。",
      "source_evidence": "安苇在复核册上添了一行：“校准副镜自辰时二刻起留置候场廊，未见封存记录。留置原因已述，未上报原因待核。”"
    },
    {
      "change": "岑照因镜灼症状未减，不许追加观察主镜残痕。",
      "source_evidence": "安苇记下时长：“不足半刻。镜灼症状未减，不许追加观察。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "明日进行低限度试场复测。",
    "薛简掌控封签和调用，岑照只做受限辨序。",
    "阮青必须在启阵前交代校准副镜从维护架移到候场廊的准确时间。",
    "主镜仍有一道残痕未看完，方向连向第一处回声节点。",
    "岑照的左眼镜灼仍在刺痛、重影和距离误判状态，不能追加观察高亮或长时残痕。",
    "岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动试场，已列入程序责任复核清单。",
    "现有线索只削弱同乡泄露链条，未排除岑照借提前试场放出纹路的可能。",
    "候场副镜反光可解释唐桥运气图的前三折，但不能解释图如何转手，也不能证明唐桥是否知道它对应试炼路线。"
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
  "source_sha256": "6a33cd4c333479846beb420d6c7e0f05a45cfcce609ab9d3de94965f65a456cd",
  "entity_changes": [
    {
      "change": "问心镜阵在低限复测中确认主镜与第一回声节点存在错层，安全纹路与陷阱落点短暂错开，镜阵未修复。",
      "source_evidence": "两息之内，淡青光带向右偏了一寸，又缓缓归位。石刺没有归位，反而在原处留下半透明重影。\n\n主镜与节点，已经不在同一层上。"
    },
    {
      "change": "阮青关于校准副镜从维护架移入候场廊的时间出现前后矛盾，只形成时间疑点。",
      "source_evidence": "“我搬的。也可能……下签之后才搬。”\n\n安苇只道：“两种时刻都记。今日不替你选。”"
    },
    {
      "change": "唐桥的运气图仍处于封存和补充申诉材料状态，来源链未被证明。",
      "source_evidence": "唐桥把封存中的运气图申诉又递了上来，纸角新添了一行字：错层既生，图路或为天意所示。\n\n安苇划掉“天意”二字：“改写物件来源、所见角度、作图时刻。其余不收。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "岑照后续只能在安苇与薛简监督下提供辨序协助，每次结论需由正式监考复述确认。",
      "source_evidence": "“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
    },
    {
      "change": "薛简保留岑照涉嫌路线外泄的判断，但同意镜阵安全必须优先处理。",
      "source_evidence": "薛简合上调用簿：“主镜封签未破，提前调用记录仍在。座次线索虽已削弱，现有证据也不能排除岑照借试场放出纹路的可能。我不撤销判断。”\n\n岑照道：“残痕只能证明先后。今日能证明的是主镜与节点错层，不是传播动机。”\n\n“这句我记。”薛简看了一眼已经熄黑的第一节点，“泄露路线另查。但镜阵安全必须先修。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照的 left-eye-mirror-burn 加重，症状明确为重影、神识刺痛、距离误判。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "岑照扶住监考台，左眼视野里，薛简分成了两个。一个在收阵盘，一个站在半步之外。神识中的刺痛没有随着幻象消退，反而顺着眼眶一下下往深处扎。\n\n安苇先验过三名考生，又查主镜灵息，最后才走到他面前。\n\n“看我手。”\n\n她伸出两指。\n\n岑照闭上右眼，左眼里却有四根手指，远近各一层。\n\n“四。”他说完，又停了一息，“不，重影。实际是二。”\n\n“距离？”\n\n“半丈。”\n\n安苇的手距他不过两尺。\n\n她收回手：“左眼镜灼加重。重影、神识刺痛、距离误判，三项俱在。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照临时监考资格被冻结；伤势解除前不得独自进入深层幻境校场，后续只能在安苇与薛简监督下提供辨序协助。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "随后，她取过岑照的临时监考牌，在背面压下一道灰印。\n\n“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照 left-eye-mirror-burn 解除前不得独自进入深层幻境校场的限制继续有效。",
      "state_id": "solo-deep-illusion-ban",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "岑照的照痕辨序继续被限制为只报残痕方向和先后，不认人、不定动机，并由正式监考复述确认。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇又看向岑照：“你只做受限照痕辨序。只报方向、先后，不认人，不定动机。左眼若再出重影，立刻停。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "exam-hall",
      "resource_id": "exam-hall-reset-seal",
      "operation": "consume",
      "amount": 1,
      "unit": "枚",
      "resulting_balance": 1,
      "source_or_destination": "低限试场错层后的全场重置",
      "change": "考场启用并永久消耗 1 枚全场重置印，余额从 2 枚降为 1 枚，不返还。",
      "source_evidence": "临时复核桌被搬到熄灭的主镜旁。安苇当场展开资源簿，在重置印一栏写下：原有二枚，启用一枚，余一枚。用途为低限试场错层后的全场重置，不返还。"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "investigating",
      "belief": "安苇确认岑照误判第一节点距离、left-eye-mirror-burn 加重，并冻结其临时监考资格；岑照漏做副镜第二道封镜检查和无正式监考复核提前启动试场仍在记录中，今日重置不覆盖旧责。",
      "supersedes_fact_ids": [],
      "change": "安苇将岑照资格复核从风险复核推进为资格冻结，并维持既有程序责任记录。",
      "source_evidence": "岑照按住仍在发痛的左眼：“我误判第一节点距离，记我。”\n\n“已记。”安苇道，“你漏做副镜第二道封镜检查，无正式监考复核提前启动试场，也仍在记录中。今日重置不覆盖旧责。”"
    },
    {
      "character_id": "ruan-qing",
      "fact_id": "unsealed-calibration-mirror",
      "state": "conceals",
      "belief": "阮青承认校准副镜由自己搬动，但对副镜移入候场廊是在辰时二刻前还是下签之后说法矛盾，仍未给出可核对的完整说明。",
      "supersedes_fact_ids": [],
      "change": "阮青对副镜移位时间的回避从未封存、未上报扩展为具体时间前后矛盾。",
      "source_evidence": "“辰时二刻前后。”\n\n“前，还是后？”\n\n阮青攥紧量绳：“应当是前。”\n\n薛简翻开维护簿：“辰时二刻，你在第一节点下签，记录为清理回声槽。副镜若在此前移走，是谁搬的？”\n\n“我搬的。也可能……下签之后才搬。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "suspects",
      "belief": "薛简仍依据主镜封签未破、提前调用记录和现有证据，怀疑岑照借试场放出纹路；但承认泄露路线另查，镜阵安全必须先修。",
      "supersedes_fact_ids": [],
      "change": "薛简未撤销对岑照泄露路线的怀疑，只调整处理优先级为先修镜阵安全。",
      "source_evidence": "薛简合上调用簿：“主镜封签未破，提前调用记录仍在。座次线索虽已削弱，现有证据也不能排除岑照借试场放出纹路的可能。我不撤销判断。”\n\n岑照道：“残痕只能证明先后。今日能证明的是主镜与节点错层，不是传播动机。”\n\n“这句我记。”薛简看了一眼已经熄黑的第一节点，“泄露路线另查。但镜阵安全必须先修。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "investigating",
      "belief": "岑照认为今日能证明的是主镜与节点错层，残痕只能证明先后，不能证明传播动机。",
      "supersedes_fact_ids": [],
      "change": "岑照将本章复测结论明确限定为镜阵错层事实，未把残痕解释为传播动机证据。",
      "source_evidence": "岑照道：“残痕只能证明先后。今日能证明的是主镜与节点错层，不是传播动机。”"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "investigating",
      "belief": "唐桥试图以错层解释运气图路线，但被安苇要求改写为物件来源、所见角度、作图时刻，其余不收。",
      "supersedes_fact_ids": [],
      "change": "唐桥的运气图来源仍未被确认，只被要求补充可核对信息。",
      "source_evidence": "唐桥把封存中的运气图申诉又递了上来，纸角新添了一行字：错层既生，图路或为天意所示。\n\n安苇划掉“天意”二字：“改写物件来源、所见角度、作图时刻。其余不收。”"
    }
  ],
  "thread_changes": [
    {
      "change": "低限复测确认试场安全纹路与实际陷阱落点错开，推动调查从单纯泄题动机转向主镜与回声节点错层修复。",
      "source_evidence": "主镜亮起时，一条淡青安全纹路从镜底铺出，越过第一道白线，停在第二道白线左侧。\n\n几乎同时，地面浮出一排浅灰石刺。\n\n石刺本应落在安全纹路之外，最前一根却从淡青光带边缘探了出来，正扎在先前三名考生站过的位置。"
    },
    {
      "change": "错层在实测中扩大，岑照因左眼重影误判第一节点距离，导致封线错误并触发全场重置。",
      "source_evidence": "“不对，是三丈半！”岑照抬手指向节点，眼中的两重边界终于短暂合一，“我报近了一丈！”\n\n神识刺痛随即穿入额角。他脚下明明离阵盘尚有半丈，伸手时却碰翻了旁边的记录架。\n\n薛简一把扶住阵盘：“主镜锁不住。第一节点在反卷！”"
    },
    {
      "change": "后续修复方向确定为停用高亮镜纹，改用低亮度分段检查主镜及第一、第二回声节点。",
      "source_evidence": "安苇封好事故簿：“即刻停用高亮镜纹。明日改用低亮度分段检查，先主镜，再第一、第二回声节点。薛简保管封签与调用记录，岑照只报残痕方向和先后。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "考生将“不得前进三步”的安全指令误解为站位口诀，导致候场线重排和唐桥被排到最后。",
      "source_evidence": "十几名考生齐齐往后退了三步，又有人向左挪半步。唐桥夹在其中，正压低声音指点：“不得前进三步，意思便是前三步有变。第二线后起步，左脚先落，正合我那张图的第二折。”\n\n薛简抬眼：“谁让你们动的？”\n\n唐桥拱手：“安全指令。”\n\n“安全指令是让你们不动。”\n\n“弟子不动之前，先选个稳妥位置。”"
    },
    {
      "change": "唐桥因继续把退三步当成道理，被薛简命令再往后排一丈。",
      "source_evidence": "唐桥远远看了一眼，小声道：“所以退三步确有道理。”\n\n薛简头也不抬：“把他再往后排一丈。”"
    }
  ],
  "new_constraints": [
    {
      "change": "岑照临时监考资格被冻结，伤势解除前不得独自进入深层幻境校场，后续只可在安苇与薛简监督下提供辨序协助。",
      "source_evidence": "“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
    },
    {
      "change": "问心镜阵修清错层前禁止再开完整试场。",
      "source_evidence": "“在修清错层之前，谁也不许再开完整试场。”"
    },
    {
      "change": "即刻停用高亮镜纹，下一步改用低亮度分段检查。",
      "source_evidence": "安苇封好事故簿：“即刻停用高亮镜纹。明日改用低亮度分段检查，先主镜，再第一、第二回声节点。薛简保管封签与调用记录，岑照只报残痕方向和先后。”"
    },
    {
      "change": "阮青明日必须带维护架记录，给出副镜移位时刻与主镜校准缺口的可核对说法。",
      "source_evidence": "安苇转向阮青：“副镜移位时刻，明日带维护架记录来。辰时二刻前，还是辰时二刻后，须有可核对的说法。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "安苇已要求即刻停用高亮镜纹，明日改用低亮度分段检查，顺序为先主镜，再第一、第二回声节点。",
    "薛简继续保管封签与调用记录；岑照只报残痕方向和先后，每次结论需由正式监考复述确认。",
    "岑照 left-eye-mirror-burn 加重，活动症状为左眼重影、神识刺痛和距离误判；临时监考资格已被冻结。",
    "岑照伤势解除前不得独自进入深层幻境校场，只能在安苇与薛简监督下提供辨序协助。",
    "exam-hall-reset-seal 已从 2 枚降为 1 枚，消耗用途为低限试场错层后的全场重置，不返还。",
    "薛简仍怀疑岑照借试场放出纹路，但承认泄露路线另查，镜阵安全必须先修。",
    "阮青明日必须带维护架记录，说明校准副镜移位是在辰时二刻前还是辰时二刻后。",
    "唐桥运气图仍未证明完整来源链，安苇只接受其补写物件来源、所见角度、作图时刻。",
    "问心镜阵主镜与第一回声节点错层已确认；修清错层之前不得再开完整试场。"
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
  "source_sha256": "5371285319227f9f9d464b4f09bb35edd0c290c990f9642527da5a95a82a5634",
  "entity_changes": [
    {
      "change": "问心镜阵主镜完成一处裂纹封补，但不视为全阵修复。",
      "source_evidence": "安苇提笔登记：“镜砂一份，去向：主镜裂纹封补。考场镜砂由六份减至五份。主镜仅完成一处封补，不视为全阵修复。”"
    },
    {
      "change": "第一回声节点完成低亮度临时校准，扣环停在半锁位置，仍需复核。",
      "source_evidence": "第三次转环后，节点的低鸣终于与主镜同拍。\n\n阮青刚要扣死外环，安苇伸手挡住：“临时校准。先留复核扣。”\n\n薛简补道：“还要与第二、第三节点连测。单点同拍，不等于全阵无错。”"
    },
    {
      "change": "校准副镜仍在候场廊封存架，未启封，并被单独列为封存首项。",
      "source_evidence": "封存架被重新打开，灰布、铜笔洗、照面小镜逐件移到桌上。副镜仍未启封，却已被单独列在首项。"
    },
    {
      "change": "执事从书箱夹层里发现三张折成同样大小的反光纸。",
      "source_evidence": "候场廊另一头，执事从一只书箱夹层里抽出三张折成同样大小的反光纸。"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "岑照修复期间只能在薛简读记录、复述确认后辨低亮残痕，并且只报方向与先后。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照的左眼镜灼仍活动，重影和距离误判仍在。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“停了高亮后，刺痛缓了。重影还在，距离仍会错。”\n\n“记为短暂缓和，不是解除。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "recovery",
      "change": "因停用高亮镜纹，岑照的左眼镜灼出现短暂缓和，刺痛减轻，但未解除。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“停了高亮后，刺痛缓了。重影还在，距离仍会错。”\n\n“记为短暂缓和，不是解除。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照不得触碰阵枢、不得单独下令、不得进入深层幻境，临时监考资格冻结下的监督限制继续有效。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照不得进入深层幻境的限制继续有效。",
      "state_id": "solo-deep-illusion-ban",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "exam-hall",
      "resource_id": "mirror-sand",
      "operation": "consume",
      "amount": 1,
      "unit": "份",
      "resulting_balance": 5,
      "source_or_destination": "主镜裂纹封补",
      "change": "考场镜砂消耗一份用于主镜裂纹封补，余额由六份减至五份。",
      "source_evidence": "安苇提笔登记：“镜砂一份，去向：主镜裂纹封补。考场镜砂由六份减至五份。主镜仅完成一处封补，不视为全阵修复。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "investigating",
      "belief": "安苇记录主镜错层起点不在考生入场方向，该事实只削弱主动泄露路线的部分推断，不能排除岑照的调用责任、漏封责任及传播嫌疑；岑照资格冻结和受监督限制仍继续。",
      "supersedes_fact_ids": [],
      "change": "安苇将错层起点不在入场方向及其有限影响写入记录，同时保留岑照程序责任与传播嫌疑。",
      "source_evidence": "安苇提笔，把两人的话拆成两行：“事实：错层起点不在考生入场方向。影响：削弱主动泄露路线的部分推断。不能据此排除岑照的调用责任、漏封责任及传播嫌疑。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "investigating",
      "belief": "岑照知道残痕只能证明灵力运行方向和先后，不能证明谁传图或人的动机；本章残痕只能削弱主动泄题推断。",
      "supersedes_fact_ids": [],
      "change": "岑照再次限定照痕辨序的证明范围，不将残痕当作洗清嫌疑的证据。",
      "source_evidence": "“不能。”岑照答得很快，“残痕只记灵力怎么走、何时走。不记谁想做什么，也不认是谁把图传出去。”\n\n“那只能说明，我原先以为错层由入场路线触发，这一项不成立。”\n\n“只能削弱那一段推断。”"
    },
    {
      "character_id": "ruan-qing",
      "fact_id": "unsealed-calibration-mirror",
      "state": "conceals",
      "belief": "阮青知道校准副镜在开考封存点前已移出维护架，并承认自己为赶开考时间将副镜实际留在候场廊而未按时归架封存。",
      "supersedes_fact_ids": [
        "unsealed-calibration-mirror"
      ],
      "change": "阮青关于副镜移位的矛盾说法被维护架记录固定为辰时一刻移出、早于辰时二刻封存点，并承认曾将副镜留在候场廊。",
      "source_evidence": "薛简抽走记录，先看架号，再看出入刻印：“副镜于辰时一刻移出维护架。开考封存点是辰时二刻。你昨日先说封存后才移，后来又说记不清。”\n\n阮青盯着桌面：“我原本要清完镜边就送回去。”\n\n安苇问：“送回哪里？”\n\n“维护架。”\n\n“实际放在哪里？”\n\n“候场廊。”\n\n“为何？”\n\n阮青沉默片刻：“开考时间快到了。主镜还缺一轮校准，我想着副镜只是暂放，等主镜亮稳再封。”"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "investigating",
      "belief": "唐桥仍试图把修复步骤理解并记录成可避开错层的“新版避坑谱”，其运气图和新增修复笔记被作为传播风险一并封存。",
      "supersedes_fact_ids": [],
      "change": "唐桥新增抄录修复步骤的笔记被发现并封存，扩大了其笔记和候场物件来源链的调查范围。",
      "source_evidence": "唐桥抱着一本窄册，正伏在膝上奋笔疾书。安苇走过去时，他刚写完一行大字——《新版避坑谱》。\n\n下面列着：主镜先补背纹，第一节点三转，低亮时看暗线。"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "suspects",
      "belief": "薛简确认主镜错层最早扰动来自回声节点方向，不是考生入场方向；这使其关于错层由入场路线触发的一项推断不成立，但现有证据仍不足以撤销对岑照的判断。",
      "supersedes_fact_ids": [],
      "change": "薛简把错层起点从考生入场方向修正为回声节点方向，但未撤销对岑照泄露路线的怀疑。",
      "source_evidence": "薛简将维护架记录压在调用簿旁：“镜阵错层查残痕先后，副镜移位查封签时间。两项并行。现有证据仍不足以撤销对岑照的判断，也不足以把两项混作一项。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "side-mirror-time-record",
      "state": "investigating",
      "belief": "薛简掌握维护架记录显示副镜移出维护架早于开考封存点，并将此项与封签时间、阵法调用记录并行核验。",
      "supersedes_fact_ids": [],
      "change": "薛简将副镜移位时间固定为可核验记录项，纳入与封签时间、调用记录的并行核验。",
      "source_evidence": "薛简将“只是暂放”四字原样写入记录：“副镜移出维护架早于开考封存点，且未按时归架封存。此项与封签时间、阵法调用记录并行核验。”"
    }
  ],
  "thread_changes": [
    {
      "change": "修复流程进入低亮分段阶段：先封补主镜一处裂纹，再完成第一回声节点临时校准，后续需主镜与第一节点连测并修第二节点。",
      "source_evidence": "安苇合上记录册：“明日，第一节点与主镜连测，再修第二节点。仍用低亮分段法。”"
    },
    {
      "change": "主镜错层起点被确认不在考生入场方向，只削弱主动泄露路线推断，未洗清岑照嫌疑。",
      "source_evidence": "安苇提笔，把两人的话拆成两行：“事实：错层起点不在考生入场方向。影响：削弱主动泄露路线的部分推断。不能据此排除岑照的调用责任、漏封责任及传播嫌疑。”"
    },
    {
      "change": "副镜移位线索由矛盾口供推进为维护架记录与阮青承认的候场廊暂放事实，需继续与封签时间和调用记录核验。",
      "source_evidence": "薛简将“只是暂放”四字原样写入记录：“副镜移出维护架早于开考封存点，且未按时归架封存。此项与封签时间、阵法调用记录并行核验。”"
    },
    {
      "change": "唐桥新增修复步骤笔记触发考生笔记清点和候场物件再封存。",
      "source_evidence": "她转身点了两名执事：“清点所有考生笔记。运气图、新增修复笔记与候场物件清单一并封存。候场廊的笔、纸、反光器物重新登记，未列册者不得留下。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥把阵法修复步骤命名为《新版避坑谱》，被薛简按规章更正为“未授权修复记录”。",
      "source_evidence": "薛简抽走窄册，按规章念道：“候场考生不得抄录阵法维修步骤、节点位置及监考口令。此纸封存，名称更正为‘未授权修复记录’。”\n\n唐桥争道：“叫避坑谱比较好记。”"
    },
    {
      "change": "安苇因唐桥的笔记“好记”而将其定为传播风险物。",
      "source_evidence": "唐桥争道：“叫避坑谱比较好记。”\n\n安苇把纸折起：“正因为好记，才算传播风险物。”"
    }
  ],
  "new_constraints": [
    {
      "change": "修复期间停用高亮镜纹，岑照不得触碰阵枢、不得单独下令、不得进入深层幻境，所有结论需由薛简复述确认。",
      "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
    },
    {
      "change": "第一回声节点只是临时校准，必须留复核扣，并与第二、第三节点连测后才能判断全阵状态。",
      "source_evidence": "阮青刚要扣死外环，安苇伸手挡住：“临时校准。先留复核扣。”\n\n薛简补道：“还要与第二、第三节点连测。单点同拍，不等于全阵无错。”"
    },
    {
      "change": "候场考生不得抄录阵法维修步骤、节点位置及监考口令；唐桥笔记被封存为未授权修复记录。",
      "source_evidence": "薛简抽走窄册，按规章念道：“候场考生不得抄录阵法维修步骤、节点位置及监考口令。此纸封存，名称更正为‘未授权修复记录’。”"
    },
    {
      "change": "考生笔记、运气图、新增修复笔记和候场物件清单一并封存，候场廊笔、纸、反光器物重新登记，未列册者不得留下。",
      "source_evidence": "她转身点了两名执事：“清点所有考生笔记。运气图、新增修复笔记与候场物件清单一并封存。候场廊的笔、纸、反光器物重新登记，未列册者不得留下。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "明日第一节点与主镜连测，再修第二节点，仍用低亮分段法。",
    "第一回声节点已完成低亮临时校准但只留复核扣，仍需与第二、第三节点连测。",
    "主镜只完成一处裂纹封补，消耗 1 份 mirror-sand，考场镜砂余额为 5 份。",
    "岑照 left-eye-mirror-burn 仅短暂缓和，重影和距离误判仍在，资格冻结与不得独自进入深层幻境的限制继续有效。",
    "薛简确认错层最早扰动来自回声节点方向而非考生入场方向，但现有证据仍不足以撤销对岑照的判断。",
    "阮青维护架记录显示副镜辰时一刻移出，早于辰时二刻开考封存点；她承认曾将副镜暂放候场廊，此项需与封签时间和调用记录并行核验。",
    "唐桥的运气图、新增修复笔记与候场物件清单已一并封存，候场廊笔、纸、反光器物正在重新登记。",
    "候场廊执事从书箱夹层里抽出三张折成同样大小的反光纸。"
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
  "source_sha256": "8bd218662a3507b297395c5077ee4dfda773382a96ece3fcbce7a7996177e578",
  "entity_changes": [
    {
      "change": "主镜与第一回声节点完成一次低亮连测，残痕方向与先后可连上；第一节点仍为可复核临时校准，复核扣待第二节点三点连测后再决定是否锁。",
      "source_evidence": "薛简照原话写下，又补了一行：“第一节点为可复核临时校准，待第二节点三点连测后，再决定是否锁复核扣。”"
    },
    {
      "change": "三张反光纸的持有人、原位置、折法与可成角度已登记并封存。",
      "source_evidence": "她拿过候场清单，在原座次图上划出三道间距线：“丙五座与书箱分开两砖。所有座次与廊柱、窗面、铜器至少隔一砖半。笔、纸、墨碟、玉扣及能反光的器物另列一册。三张纸登记持有人、原位置、折法与可成角度，全部封存。”"
    },
    {
      "change": "第三张反光纸确认为丙五座唐桥相关物件，原放在书箱右侧夹层，折成三叠，唐桥称借来比线。",
      "source_evidence": "执事念道：“丙五座，唐桥。原放在书箱右侧夹层，折成三叠。唐桥称不是他的纸，只是借来比线。”"
    },
    {
      "change": "候场廊复原出第三张反光纸在特定位置、折法和角度下可映出与唐桥运气图前三折相近的第一层安全纹路。",
      "source_evidence": "第二次斜光穿过副镜原位，落上第三张反光纸。纸面顿时亮起三段弯折的淡纹：先向左避开一道窄线，再斜过中央，最后折回右侧。\n\n薛简立刻将唐桥的运气图压在旁边。前三折虽长短略有差别，转向却近乎一致。"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "岑照在低亮连测中继续只能辨认残痕方向与先后，证明范围被正式限定为方向与先后，不证明成因、行为人或动机。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“记。”安苇道，“照痕辨序的证明范围，仅限方向与先后。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照的左眼镜灼未加重但仍存在重影，不能增加观察强度。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "淡青镜纹随即熄灭。岑照左眼的刺痛没有加深，重影却仍停了片刻才散。他退到白线外，没有碰阵枢，也没有要求增加亮度。"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照临时监考资格冻结与监督限制继续有效，仍不得触碰阵枢、不得进入深层幻境，只能报方向、先后和角度。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照不得进入深层幻境的限制继续有效。",
      "state_id": "solo-deep-illusion-ban",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "investigating",
      "belief": "岑照知道残痕和反光复原只能说明位置、折法、角度及相近安全纹路，不能证明唐桥动机、唐桥见过后续考题或岑照自身无责。",
      "supersedes_fact_ids": [],
      "change": "岑照再次限定照痕与反光证据的证明范围。",
      "source_evidence": "岑照盯着纸上渐淡的光：“只能说明这个位置、折法和角度，能映出相近的第一层安全纹路。不能说明唐桥为何画，也不能说明他见过后续考题。”"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "investigating",
      "belief": "唐桥承认自己使用同样宽、折三折的反光纸尺寸给运气图当格尺；该说法被纳入传播风险调查。",
      "supersedes_fact_ids": [],
      "change": "唐桥的运气图来源调查新增同尺寸折纸作格尺的说法。",
      "source_evidence": "唐桥沉默片刻：“给运气图当格尺。”\n\n薛简翻开封存的草图：“格尺？”\n\n“同样宽的纸，折三折，画出来的路才齐整。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "suspects",
      "belief": "薛简仍未撤销对岑照主动泄露路线的嫌疑，并认为主镜封签、提前调用与漏封检查仍在记录中。",
      "supersedes_fact_ids": [],
      "change": "候场反光证据出现后，薛简明确不据此撤销岑照主动泄露路线嫌疑。",
      "source_evidence": "薛简收起草图：“也不能据此撤销你主动泄露路线的嫌疑。主镜封签、提前调用与漏封检查仍在记录中。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "side-mirror-time-record",
      "state": "investigating",
      "belief": "薛简掌握副镜辰时一刻移出、辰时二刻为开考封存点，并认为丙五座书箱、三折反光纸和镜面角度可复原，阮青所谓暂放已跨过封存时限。",
      "supersedes_fact_ids": [],
      "change": "薛简将副镜暂放问题进一步压实为跨过封存时限的程序缺口，并与反光复原证据关联。",
      "source_evidence": "薛简翻到维护架记录：“辰时一刻移出。辰时二刻为开考封存点。现在又有丙五座书箱、三折反光纸和镜面角度可以复原。你所说的‘一阵’，已经跨过封存时限。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "investigating",
      "belief": "安苇继续冻结岑照资格并限制其连测时间与报告范围；同时要求第二节点三点低亮连测、调用记录核查和阮青说明副镜经手与是否使用镜砂或临时封纹。",
      "supersedes_fact_ids": [],
      "change": "安苇维持岑照资格冻结并布置下一步核查。",
      "source_evidence": "安苇合上册子：“次日修第二回声节点。主镜、第一节点、第二节点做三点低亮连测。薛简，调辰时一刻到辰时三刻的调用记录。阮青，说明副镜离架后由谁经手，是否用过镜砂或临时封纹。”\n\n她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
    },
    {
      "character_id": "ruan-qing",
      "fact_id": "unsealed-calibration-mirror",
      "state": "conceals",
      "belief": "阮青知道自己所谓副镜只在廊柱旁暂放一阵的说法已被维护架时间、封存点和反光复原证据压实为程序缺口，但完整责任仍需继续核验。",
      "supersedes_fact_ids": [],
      "change": "阮青不再坚持“只是暂放”的辩解。",
      "source_evidence": "阮青望着被封入袋中的第三张纸，终于没再说“只是暂放”。"
    }
  ],
  "thread_changes": [
    {
      "change": "候场反光链条成为待核证据，需与副镜移出时间、封签时间、阵法调用记录并列核查；现阶段不作动机认定。",
      "source_evidence": "薛简在新清单末尾落下封签：“候场反光链条成立为待核证据，与副镜移出时间、封签时间、阵法调用记录并列核查。现阶段，不作动机认定。”"
    },
    {
      "change": "阮青暂放副镜的程序问题进一步明确：暂放不等于没有程序问题。",
      "source_evidence": "安苇道：“想归架不等于已经归架。暂放也不等于程序不存在。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥把同尺寸折纸解释为运气图格尺，岑照严肃纠正为折痕等距，安苇将其登记为测距用途而非吉相。",
      "source_evidence": "岑照道：“线齐只说明折痕等距。”\n\n“等距也是一种吉相。”\n\n“登记为测距用途。”安苇吩咐执事，“不登记吉相。”"
    },
    {
      "change": "安苇以“哪张纸比较有福气”调侃唐桥的运气说法，同时确认候场廊重排成本。",
      "source_evidence": "候场执事迟疑道：“如此重排，候检至少多半个时辰。”\n\n“记入重排成本。”安苇道，“总好过再用一场考试核验哪张纸比较有福气。”"
    }
  ],
  "new_constraints": [
    {
      "change": "候场廊座次与反光物件重新标注：丙五座与书箱分开两砖，所有座次与廊柱、窗面、铜器至少隔一砖半，笔、纸、墨碟、玉扣及能反光器物另列一册；三张纸全部封存。",
      "source_evidence": "她拿过候场清单，在原座次图上划出三道间距线：“丙五座与书箱分开两砖。所有座次与廊柱、窗面、铜器至少隔一砖半。笔、纸、墨碟、玉扣及能反光的器物另列一册。三张纸登记持有人、原位置、折法与可成角度，全部封存。”"
    },
    {
      "change": "候场廊重排使候检时间至少延长半个时辰，作为重排成本记录。",
      "source_evidence": "候场执事迟疑道：“如此重排，候检至少多半个时辰。”\n\n“记入重排成本。”安苇道，“总好过再用一场考试核验哪张纸比较有福气。”"
    },
    {
      "change": "下一次连测需缩短时间，岑照仍只报方向、先后和角度，资格冻结不变，不得碰阵枢、不得进深层幻境。",
      "source_evidence": "她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "次日修第二回声节点，主镜、第一节点、第二节点做三点低亮连测。",
    "薛简需调辰时一刻到辰时三刻的调用记录。",
    "阮青需说明副镜离架后由谁经手，是否用过镜砂或临时封纹。",
    "候场反光链条作为待核证据，与副镜移出时间、封签时间、阵法调用记录并列核查，现阶段不作动机认定。",
    "唐桥的运气图和三张反光纸继续封存；候场廊按新座次间距和反光物件清单看管。",
    "岑照左眼镜灼未解除，仍有重影；后续连测时间需缩短，仍只报方向、先后和角度，资格冻结不变。"
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
  "source_sha256": "90b5623173c7b0ccaf4acf23a7ebef1b773aebce875f4af8d8dd1a109ac1d6be",
  "entity_changes": [
    {
      "change": "第二回声节点完成低亮补砂修复，低亮试合后旁痕不再回折，先后可辨。",
      "source_evidence": "镜砂入纹，第二节点轻轻一震。岑照没有看震光，只听铜铃三响的间隔。\n\n薛简按规程复述：“低亮试合。西南主线入齿，旁痕不再回折，二者先后可辨。岑照？”"
    },
    {
      "change": "主镜、第一回声节点、第二回声节点完成三点低亮连测；第一节点复核扣扣死，第二节点留待第三节点连测。",
      "source_evidence": "岑照闭左眼听完：“主镜先，第一次之，第二后接。第一节点可扣复核扣。第二节点需等第三节点同线后再扣死。”\n\n薛简没有反驳，取出小铜扣，将第一节点封册上的复核扣压下。咔的一声，清脆得像案上多了一条规矩。\n\n“第一回声节点复核扣扣死。”薛简记录，“第二节点留待第三节点连测。”"
    },
    {
      "change": "考生管理流程新增涉反光图考生告知签收，反光物件清单增加“告知签收”栏。",
      "source_evidence": "候场廊里的队伍因此多绕了一折。执事把涉图考生单独列名，反光物件清单后又添一栏“告知签收”。原本准备重开前只查座次与封签，如今还要查谁把影子当凭据。"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照左眼镜灼仍活动，表现为重影与距离误判风险；本章低亮连测后出现疲乏，但未确认加重或解除。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "岑照站在阵枢线外，袖口压着手背。他左眼仍有薄薄重影，看台上铜尺时，尺尾总像多出一寸。他没有靠近，只把视线落在低亮镜纹的暗边。"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照在三点连测中左眼疲乏，扣影漂移，仍需避免依赖距离判断。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "主镜低亮起，第一节点随之回声。第二节点刚补过砂，光色比第一节点厚半分。岑照左眼一疲，第一节点的扣影像漂到第二节点旁边。他停了一息。"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "岑照继续将照痕辨序限定为听取低亮刻度后只报方向与先后，不报距离或推断。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“停看高亮。”岑照道，“请薛师兄读低亮刻度。只读灰痕起止，不读推断。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照临时监考资格冻结与不得触碰阵枢限制继续有效，连测时站在阵枢线外并有红封纸标识。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "连测廊的灯全部压到低亮，只剩主镜、第一节点、第二节点三处暗纹相接。岑照站在阵枢线外三步，脚尖前有薛简亲手贴的红封纸，写着“冻结资格，不得触枢”。"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "exam-hall",
      "resource_id": "mirror-sand",
      "operation": "consume",
      "amount": 1,
      "unit": "份",
      "resulting_balance": 4,
      "source_or_destination": "第二回声节点补砂修复",
      "change": "第二回声节点补砂消耗考场镜砂 1 份，余额由 5 份降为 4 份。",
      "source_evidence": "阮青取出一小瓶镜砂，倒入量槽。细砂泛起冷白光，正好一格。薛简验过瓶封，报：“消耗镜砂一份。考场镜砂余额五份降为四份。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "ruan-qing",
      "fact_id": "unsealed-calibration-mirror",
      "state": "knows",
      "belief": "阮青承认第二节点临时封纹所需镜砂曾被优先留给主镜裂纹，导致副镜封纹没有及时补做；她同时否认自己改考题或碰主镜封签。",
      "supersedes_fact_ids": [
        "unsealed-calibration-mirror"
      ],
      "change": "阮青不再只是遮掩副镜暂放问题，而是承认镜砂调配导致副镜封纹未及时补做。",
      "source_evidence": "薛简笔尖一顿：“说清楚。第二节点临时封纹所需镜砂，被你优先留给主镜裂纹，所以副镜封纹没有及时补做？”\n\n阮青低头：“是。我没改考题，也没碰主镜封签。我只是赶修主镜和这里，觉得副镜……暂时不进阵。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "investigating",
      "belief": "安苇将阮青优先调镜砂用于主镜裂纹与第二节点临时封纹、副镜封纹未及时补做记为程序与资源责任；不等同修改正式考题，并继续推进资格与程序核查。",
      "supersedes_fact_ids": [
        "temporary-proctor-qualification"
      ],
      "change": "安苇把资源去向和副镜封纹缺口正式记入程序责任范围，同时明确不等同于修改正式考题。",
      "source_evidence": "“又是暂时。”安苇在封册上落笔，“记资源去向。阮青优先调镜砂用于主镜裂纹与第二节点临时封纹，副镜封纹未及时补做。此项为程序与资源责任，不等同修改正式考题。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "side-mirror-time-record",
      "state": "investigating",
      "belief": "薛简掌握阵法调用记录显示副镜辰时一刻移出维护架，辰时二刻为开考封存点，岑照辰时二刻又三分提前启动低限试场，辰时二刻后部分反光纸位置才登记。",
      "supersedes_fact_ids": [
        "side-mirror-time-record"
      ],
      "change": "薛简将副镜移出、封存点、岑照提前调用和反光纸登记位置形成时间放入同一调用记录链。",
      "source_evidence": "薛简调出阵法调用记录。玉简一层层展开，辰时一刻到辰时三刻的刻线浮在案上。\n\n“辰时一刻，校准副镜移出维护架。”薛简念得很慢，“辰时二刻，开考封存点。辰时二刻又三分，岑照以临时监考牌提前启动低限试场。无正式监考复核。辰时二刻后，候场廊丙五、丁二、戊一位置登记反光纸。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "suspects",
      "belief": "薛简不再把路线相似简单归因于考生入场方向泄题，认为回声方向、候场反光、纸位时间要并列核查；但岑照提前调用试场和漏封副镜检查仍成立，现有证据不足以撤销他的判断。",
      "supersedes_fact_ids": [
        "cen-leaked-exam-route"
      ],
      "change": "薛简的旧认知被部分纠正，但他仍未公开撤销对岑照的判断。",
      "source_evidence": "薛简收起玉简，语气比前几日少了些硬刺，却仍稳：“路线相似不能再简单归因于考生入场方向泄题。回声方向、候场反光、纸位时间都要并列核查。但岑照提前调用试场、漏封副镜检查，记录仍成立。现有证据不足以撤销我的判断。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "investigating",
      "belief": "岑照明确反光图与安全纹路相近不等于考题，反光角度只能见第一层安全纹路，随机变化和心境关不能由折痕替代。",
      "supersedes_fact_ids": [
        "shared-route-origin"
      ],
      "change": "岑照进一步限定反光图证据的证明范围，并否定唐桥以运气图免试或免陷阱的理解。",
      "source_evidence": "唐桥把告知单拿近些：“可反光图前三折与安全纹路相近，这是你们登记过的。”\n\n“相近，不等于考题。”岑照短句往下压，“反光角度只见第一层安全纹路。随机变化不在图上。心境关不按折痕开门。你按图冲，仍会撞幻象。”"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "knows",
      "belief": "唐桥已经签收告知，知道反光图不能替代随机幻境心境考验，且自己的三折角不作凭据。",
      "supersedes_fact_ids": [
        "lucky-route-sketch-source"
      ],
      "change": "唐桥从继续围绕运气图来源受查，变为已收到反光图不能作为凭据的正式告知。",
      "source_evidence": "唐桥叹气，写下名字，还在旁边画了个小小的三折角。薛简冷冷看他。\n\n唐桥立刻补字：“此角不作凭据。”"
    }
  ],
  "thread_changes": [
    {
      "change": "调查焦点推进到第三回声节点、候场副镜、封签时间、调用记录和反光纸位置时间线的串联。",
      "source_evidence": "薛简合上调用记录：“明日第三节点。辰时一刻副镜移出、辰时二刻封存点、岑照提前调用、反光纸位置形成时间，我会放在同一条线上。”"
    },
    {
      "change": "下一步要求阮青带副镜封纹工具与剩余镜砂去向清单，并核查副镜边缘残留物。",
      "source_evidence": "安苇看向阮青：“带副镜封纹工具，带剩余镜砂去向清单。若副镜边缘有残留物，一并核。”"
    },
    {
      "change": "完整试场仍不得重开，因为第三节点未修、副镜未封。",
      "source_evidence": "安苇收起第一叠告知单：“今日到此。第三节点未修，副镜未封，完整试场不得重开。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥把三点连测强行理解为自己的三折运气图得到节点背书，被岑照逐句否定。",
      "source_evidence": "他听见“三点连测”四字，眼睛一亮：“三点？我那运气图正好三折。主镜、第一、第二都接上了，是不是说明前三折得了节点背书？重开时开场陷阱我可按图免过？”\n\n岑照正在按眼角，闻言放下手：“不是。”"
    },
    {
      "change": "唐桥签收告知单时仍试图给三折角留凭据，最终被迫注明此角不作凭据。",
      "source_evidence": "唐桥叹气，写下名字，还在旁边画了个小小的三折角。薛简冷冷看他。\n\n唐桥立刻补字：“此角不作凭据。”"
    }
  ],
  "new_constraints": [
    {
      "change": "三点连测规程限定为低亮、分段，岑照只报方向和先后，薛简复述，阮青补砂，越序即停止连测。",
      "source_evidence": "安苇把封册放在台角：“低亮。分段。岑照只报方向和先后。薛简复述，阮青补砂。谁越过这个次序，今日连测停止。”"
    },
    {
      "change": "第二回声节点复核扣必须等第三节点同线连测后再扣死。",
      "source_evidence": "岑照闭左眼听完：“主镜先，第一次之，第二后接。第一节点可扣复核扣。第二节点需等第三节点同线后再扣死。”"
    },
    {
      "change": "凡见过、抄过、传过反光图者必须签收告知单，不能以反光图要求免试、改座或避查，签完并入重开前检查。",
      "source_evidence": "安苇抬笔：“不评聪明。评风险。凡见过、抄过、传过反光图者，签收此单：反光图不能替代随机幻境心境考验，不得以图纸要求免试、改座、避查。签完并入重开前检查。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "第七章从第三回声节点处理与低亮连测推进；第二节点复核扣仍待第三节点同线后再扣死。",
    "岑照左眼镜灼未解除，仍有疲乏、重影和距离误判风险；下一章应继续低亮观测、停看高亮，并只报方向和先后。",
    "岑照临时监考资格仍冻结，不得触碰阵枢；提前调用试场和漏封副镜检查仍在记录中。",
    "薛简将辰时一刻副镜移出、辰时二刻封存点、岑照提前调用、反光纸位置形成时间放在同一条线上核查。",
    "阮青需带副镜封纹工具和剩余镜砂去向清单，并核查副镜边缘残留物。",
    "考场镜砂余额为 4 份。",
    "完整试场仍不得重开；第三节点未修，副镜未封。",
    "涉反光图考生已增加告知签收流程，唐桥已签收且其三折角不作凭据。"
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
  "source_sha256": "d9feaed7409c9f0ca0b5dc3edd41104417917d0e45bb8b0042e6e0cde4c9ee26",
  "entity_changes": [
    {
      "change": "第三回声节点低亮裂缝已用一份镜砂修补，主镜、第一、第二、第三回声节点形成低亮回环连测链路。",
      "source_evidence": "镜砂落入铜扣，细如星屑。阮青以浅层镜纹把它铺开，不敢越过薛简划出的阵枢线。第三节点的抖动慢慢止住，低亮光从主镜绕第一节点、第二节点，再经第三节点回环。"
    },
    {
      "change": "第二回声节点复核扣已扣死。",
      "source_evidence": "薛简把第二回声节点复核扣压下，铜扣“咔”地扣死。阮青眼巴巴看向第三扣。"
    },
    {
      "change": "第三回声节点本体可连测，但第三节点复核扣暂缓，需等候场副镜封纹连测后确认。",
      "source_evidence": "岑照立刻收眼：“第三节点本体可连测。复核扣暂缓。副镜方向残痕未清，需与副镜封纹连测。”\n\n薛简照原话写下：“第三节点复核扣暂待候场副镜封纹连测后确认。”"
    },
    {
      "change": "候场副镜边缘封纹槽内发现疑似残留镜屑，已定位封存，本章未取出。",
      "source_evidence": "安苇把副镜推到封线内侧，让薛简以低亮照边。镜边封纹槽有一道极细的缺口，缺口里卡着一点暗银色碎屑。它不亮，却在角度尺影子移动时闪了一下。\n\n薛简皱眉：“镜屑？”\n\n阮青脸色一白：“封纹刀边缘也沾过细屑。我以为是主镜补砂时带的。”\n\n安苇没有伸手取，只取一枚小封罩扣在副镜边缘：“疑似残留镜屑，定位封存。取出需明日连同封签、角度、残痕同测。今日不取。”"
    },
    {
      "change": "阮青交出副镜封纹工具，副镜未及时归架并未补做封纹被安苇记为维护责任。",
      "source_evidence": "安苇指向阮青：“工具。”\n\n阮青双手奉上封纹刀和细砂匙：“都在。副镜那时只是……还没来得及归架。”\n\n安苇笔尖一顿：“‘未及时归架并未补做封纹’，记为维护责任。不要换词。”"
    },
    {
      "change": "唐桥的站位误认记录与反光纸、运气图一并封存为传播风险材料。",
      "source_evidence": "薛简将唐桥站位另列一栏：“反光纸、运气图、站位误认，一并封存作传播风险材料。唐桥，此线不是考题。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "岑照在监督下继续将照痕辨序限定为低亮残痕的方向与先后，薛简只采信方向与先后，不采信动机判断或程序免责。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“残痕先从候场副镜反射方向入回声链。”岑照改口更短，“再入第三节点。再折主镜。三处节点先后可连。”\n\n安苇看向薛简：“采信范围？”\n\n薛简沉默片刻，道：“采信为方向与先后。不能证明谁有意传播，也不能排除岑照提前调用试场的程序问题。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "injury",
      "change": "岑照左眼镜灼仍未解除，连续低亮观测后出现酸胀、短暂重影，高亮镜纹继续停用，需取镜屑后再安排低强度观想确认伤势流程。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "岑照左眼的酸胀还没退，眼前桌角短短分出两道影。他伸手按了按冷玉纱，却没有再看镜面。\n\n安苇注意到他的动作：“今日到此。高亮镜纹继续停用。取镜屑后，再安排低强度观想，届时我确认伤势流程。现在未解除。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照临时监考资格冻结继续有效，仍不得触阵枢、不得下令调镜，只能在薛简复述后由阮青执行。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "薛简立在阵枢边，手按记录简：“岑照，不得触阵枢，不得下令调镜，只报方向、先后。由我复述，阮青执行。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "exam-hall",
      "resource_id": "mirror-sand",
      "operation": "consume",
      "amount": 1,
      "unit": "份",
      "resulting_balance": 3,
      "source_or_destination": "补第三节点低亮裂缝",
      "change": "考场镜砂消耗一份用于补第三节点低亮裂缝，余额从四份降为三份。",
      "source_evidence": "“一份。”阮青低声道，“补第三节点低亮裂缝。考场镜砂原余四份，用后一三——”\n\n薛简抬眼。\n\n阮青咬字：“余三份。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "suspects",
      "belief": "薛简掌握第三节点残痕显示安全纹路先自候场副镜反射方向入回声链，该证据压缩了原先对岑照主动泄露路线的判断，但不足以撤销；岑照提前调用试场的程序问题仍不排除。",
      "supersedes_fact_ids": [],
      "change": "薛简的旧判断被第三节点残痕进一步压缩，但他未公开撤销对岑照主动泄露路线的判断。",
      "source_evidence": "薛简收起时间线，声音比早晨低了些：“第三节点残痕已写入。它压缩了原先判断，但不足以撤销。明日取屑、连测副镜封纹后再议。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "side-mirror-time-record",
      "state": "investigating",
      "belief": "薛简将副镜辰时一刻移出维护架、辰时二刻应封存、岑照辰时二刻又三分提前调用低限试场、辰时二刻后反光纸位置登记成形、第三节点残痕显示安全纹路先自候场副镜反射方向入回声链纳入同一时间线。",
      "supersedes_fact_ids": [],
      "change": "薛简把副镜移出、封存点、岑照提前调用、反光纸登记时间和第三节点残痕先后排入同一条时间线。",
      "source_evidence": "薛简把时间一条条排开：“辰时一刻，副镜移出维护架。辰时二刻，按规应封存。辰时二刻又三分，岑照提前调用低限试场，无正式监考复核。辰时二刻后，反光纸位置登记成形。第三节点残痕显示，安全纹路先自候场副镜反射方向入回声链。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "investigating",
      "belief": "安苇继续同时记录岑照两项程序责任、阮青未及时归架并未补做副镜封纹的维护责任，以及副镜边缘疑似残留镜屑待取出核验。",
      "supersedes_fact_ids": [],
      "change": "安苇将阮青未及时归架并未补做副镜封纹正式记为维护责任，并将疑似残留镜屑定位封存待核验。",
      "source_evidence": "安苇笔尖一顿：“‘未及时归架并未补做封纹’，记为维护责任。不要换词。”\n\n阮青耳根红了：“是。”\n\n薛简把时间一条条排开：“辰时一刻，副镜移出维护架。辰时二刻，按规应封存。辰时二刻又三分，岑照提前调用低限试场，无正式监考复核。辰时二刻后，反光纸位置登记成形。第三节点残痕显示，安全纹路先自候场副镜反射方向入回声链。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "investigating",
      "belief": "岑照知道反光路径曾成立，残痕只能证明方向和先后，不能证明唐桥动机或传播者，也不能免除自己的两项程序责任。",
      "supersedes_fact_ids": [],
      "change": "岑照进一步限定残痕与反光路径证据的证明范围，并承认两项程序责任不能被洗掉。",
      "source_evidence": "岑照站在封线外，没有靠近副镜。他只看薛简摊开的角度木尺：“反光路径曾成立。残痕能证明方向和先后，不能证明唐桥为何画，也不能证明谁让他画。”\n\n“也不能洗掉你的两项程序责任。”薛简接上。\n\n“不能。”岑照道。"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "knows",
      "belief": "唐桥已被明确告知复原线是证据不是考题，地上画线不可当作自己的避坑路线或前程。",
      "supersedes_fact_ids": [],
      "change": "唐桥因误把复原线当避坑路线而被纠正，知道复原的是证据不是自己的前程。",
      "source_evidence": "唐桥抱着签收牌，小声问：“那若以后地上画了‘不可站’……”\n\n岑照道：“便不可站。”\n\n唐桥思索片刻：“若旁边又画‘复原’？”\n\n安苇把笔放下，看着他。\n\n唐桥立刻退后三步：“弟子明白，复原的是证据，不是弟子的前程。”"
    }
  ],
  "thread_changes": [
    {
      "change": "副镜边缘疑似镜屑、封签、角度、残痕被安排到明日同测，证据链缺口推进到取屑与副镜封纹连测。",
      "source_evidence": "安苇没有伸手取，只取一枚小封罩扣在副镜边缘：“疑似残留镜屑，定位封存。取出需明日连同封签、角度、残痕同测。今日不取。”"
    },
    {
      "change": "薛简将副镜边缘疑似镜屑纳入同一时间线，同时仍突出岑照提前调用记录，但主动泄露判断的压力减弱。",
      "source_evidence": "薛简把“副镜边缘封纹槽疑似镜屑”写进同一张时间线，又在“岑照提前调用”四字下重重加了一点。那一点落得不轻，却没有像早先那样直接压到“主动泄露”上。"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥把取证复原斜线误认为下一轮避坑线并主动站上去，意外触发副镜反光风险。",
      "source_evidence": "唐桥又挪了半步，刚好站到白线交叉处：“弟子只是核对自己没有站错。此处上承副镜，下避红封，左右皆不犯线，看着很顺。”\n\n薛简转头：“唐桥，退回灰绳后。”\n\n唐桥认真道：“若这是复原线，弟子站上去，岂不正好复原当时运气？”\n\n岑照看了他一眼：“你把取证角度当成求签了。”\n\n“不是求签。”唐桥辩解，“是尊重考场线。”\n\n他话音未落，副镜边缘那点暗银碎屑在他所站斜角上轻轻一闪，正把廊柱旁一张空白告知单照出一截浅纹。"
    },
    {
      "change": "唐桥的误站导致候场分区线改为无反光斜角，所有考生改退至廊柱阴面，候场管理流程增加。",
      "source_evidence": "“记录。”安苇道，“唐桥主动移至可再次形成副镜反光的斜角，传播风险增加。候场分区线改为无反光斜角，所有考生退至廊柱阴面。”"
    }
  ],
  "new_constraints": [
    {
      "change": "第三节点复核扣不得立刻扣死，需等待候场副镜封纹连测确认。",
      "source_evidence": "岑照立刻收眼：“第三节点本体可连测。复核扣暂缓。副镜方向残痕未清，需与副镜封纹连测。”\n\n薛简照原话写下：“第三节点复核扣暂待候场副镜封纹连测后确认。”"
    },
    {
      "change": "副镜边缘疑似残留镜屑已封存，必须明日连同封签、角度、残痕同测后取出，本章不得取。",
      "source_evidence": "安苇没有伸手取，只取一枚小封罩扣在副镜边缘：“疑似残留镜屑，定位封存。取出需明日连同封签、角度、残痕同测。今日不取。”"
    },
    {
      "change": "候场分区线改为无反光斜角，所有考生退至廊柱阴面，以避免再次形成副镜反光。",
      "source_evidence": "“记录。”安苇道，“唐桥主动移至可再次形成副镜反光的斜角，传播风险增加。候场分区线改为无反光斜角，所有考生退至廊柱阴面。”"
    },
    {
      "change": "岑照必须继续停用高亮镜纹，等取镜屑后再安排低强度观想并由安苇确认伤势流程。",
      "source_evidence": "安苇注意到他的动作：“今日到此。高亮镜纹继续停用。取镜屑后，再安排低强度观想，届时我确认伤势流程。现在未解除。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "第八章可从副镜封纹槽内疑似残留镜屑的取出开始；该镜屑已被封罩封存，封签上有安苇、薛简两道灵印。",
    "取出镜屑需与封签、角度、残痕同测，并与薛简整理的辰时一刻副镜移出、辰时二刻应封存、辰时二刻又三分岑照提前调用、辰时二刻后反光纸位置登记成形、第三节点残痕先后同线复核。",
    "第三回声节点本体已可连测，但第三节点复核扣仍需等候场副镜封纹连测后确认。",
    "第二回声节点复核扣已扣死；主镜、第一、第二、第三回声节点已形成低亮回环连测链路。",
    "考场镜砂余额为三份；exam-hall-reset-seal 未发生变化。",
    "岑照仍处炼气四层，left-eye-mirror-burn 未解除；高亮镜纹继续停用，取镜屑后再安排低强度观想并由安苇确认伤势流程。",
    "岑照临时监考资格仍冻结，仍不得触阵枢、不得下令调镜，提前调用低限试场和两项程序责任仍在记录中。",
    "薛简尚未撤销岑照主动泄露路线的判断，只认为第三节点残痕压缩了原先判断，需明日取屑、连测副镜封纹后再议。",
    "阮青未及时归架并未补做副镜封纹已被安苇记为维护责任；阮青交出的清单写明剩余镜砂三份，去向待第八章副镜封纹核验后继续登记。",
    "唐桥的反光纸、运气图、站位误认一并封存作传播风险材料；候场分区线已改为无反光斜角，考生退至廊柱阴面。"
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
  "source_sha256": "88c1624a2fc5d58c27727b33a306c6c93d43db7286598d44aad3d46df717f3b2",
  "entity_changes": [
    {
      "change": "候场副镜边缘残留镜屑已被取出、封样，并加两道灵印。",
      "source_evidence": "银色镜屑终于被挑出。阮青将它落入透明封样管，镜屑一面平滑，一面带着极细的斜擦纹。\n\n薛简把角度尺压到副镜边缘：“旧划在东偏南两格。受力痕由外向内。”\n\n“镜屑闪面再转半格。”岑照道。\n\n薛简复述，阮青依令微调封样管。低亮光从镜屑断面掠过，折向封物匣中的反光纸。纸上旧折角亮了一瞬，光线再落到第三回声节点的标尺边。\n\n薛简手中角度尺顿住。\n\n第三节点那道已经封存的入链残痕，正是同一方向。\n\n岑照闭了一下发酸的左眼，才道：“先副镜，后纸面，再入第三节点。只见先后，不见是谁摆的，也不见为何摆。”\n\n“记原话。”安苇道。\n\n薛简亲自落笔：“镜屑断面、封纹刀旧划、槽内受力痕、反光纸折角及第三节点低亮残痕，角度可互证。第一层安全纹路曾由候场副镜特定角度反射，经纸面入回声链。”\n\n镜屑被封样，封口再加两道灵印。"
    },
    {
      "change": "主镜、第一、第二、第三回声节点进入可复核校准完成状态，候场副镜封纹完成。",
      "source_evidence": "这一次，低亮残痕顺着封纹完整归环。第三节点复核扣发出一声清脆轻响，严丝合缝地扣死。\n\n主镜与三处回声节点的低亮回环同时稳定下来。\n\n安苇验过复核扣，又检查副镜封纹，才在校准册上落印：“主镜、第一、第二、第三回声节点，可复核校准完成。候场副镜封纹完成。镜砂余额两份。”"
    },
    {
      "change": "唐桥的运气图被安苇改列为传播风险材料，不再按唐桥自称的运气图定性。",
      "source_evidence": "薛简再翻座次册：“丙五座在候场廊第三柱前。该位置与副镜反光线相交。辰时二刻后，反光纸位置登记成形，唐桥所绘路线与第一层安全纹路相似。”\n\n唐桥小声纠正：“原名运气图。”\n\n安苇看他一眼：“现名传播风险材料。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "薛简公开撤回并更正此前对岑照可能主动泄露试炼路线的判断。",
      "source_evidence": "“我此前依据副镜封签缺失、丙五座位置、岑照提前调用记录，判断岑照可能主动泄露第一层安全路线。该判断有记录依据，但现有镜屑、残痕先后、封签时间与反光角度已组成新的可复核链条。”\n\n他声音清楚，没有含混。\n\n“现有证据不支持岑照主动泄露试炼路线。此前判断，撤回更正。”"
    },
    {
      "change": "安苇将阮青、唐桥、岑照的责任拆分记录，明确岑照主动泄露嫌疑更正不抵消两项程序违规。",
      "source_evidence": "“正该分开。”安苇展开考功堂责任册，逐条念道，“阮青，留置未封校准副镜于候场廊，未及时归架，未补做封纹，记维护责任。”\n\n阮青垂首领记。\n\n“唐桥，将副镜反光形成的第一层安全纹路绘为运气图并传播。该图只能解释开场避障相似，不能作为正式考题证据，更不能证明其可通过后续心境关。记传播风险。”\n\n唐桥看了一眼自己的图：“那它还叫运气图吗？”\n\n“封样名称不按你的愿望写。”\n\n“明白。”\n\n安苇最后看向岑照：“漏做候场副镜第二道封镜检查，记程序违规。无正式监考复核，提前启动低限试场，另记程序违规。主动泄露嫌疑更正，不抵消这两项。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "岑照的照痕辨序继续被限定为只报低亮残痕方向、先后和角度，且须由薛简复述确认，不得触镜或下令调镜。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "薛简立在封线内，持角度尺复述：“阮青拆罩，以封纹针取物。岑照在封线外，只报方向、先后、角度。不得触镜，不得下令调镜。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "recovery",
      "change": "左眼镜灼进入正式处理流程：镜屑已经取出，但高亮镜纹继续停用，下一步需用清神符稳定回声并做低强度观想，由安苇确认是否解除；本章未痊愈。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "岑照退开两步，左眼重影仍在，并未随镜阵稳定而消失。\n\n安苇收起校准册：“高亮镜纹继续停用。镜屑已经取出，下一步用清神符稳定回声，再做低强度观想。由我确认左眼镜灼是否解除。”\n\n“不是今日？”岑照问。\n\n“今日只到取屑与停亮。伤势不因证据齐了便痊愈。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照临时监考资格暂不恢复，需等伤势流程与重开复核完成后再裁定。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“临时监考资格暂不恢复。伤势流程与重开复核完成后再裁定。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照仍不得触阵枢，不得独自进入深层幻境。",
      "state_id": "solo-deep-illusion-ban",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“明日先验候场分区、携物与封纹，再开随机幻境。岑照，你仍不得触阵枢，不得独自入深层幻境。带上清神符。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "exam-hall",
      "resource_id": "mirror-sand",
      "operation": "consume",
      "amount": 1,
      "unit": "份",
      "resulting_balance": 2,
      "source_or_destination": "副镜封纹",
      "change": "阮青使用一份镜砂补完副镜封纹，考场镜砂余额从三份降为两份。",
      "source_evidence": "阮青从资源匣中取出一份镜砂。安苇当面划去清单上的一格：“副镜封纹，耗镜砂一份。余额两份。”\n\n镜砂调成银灰色细浆，沿副镜封纹槽缓缓铺开。阮青这次没再说“暂放”，每补一寸，便报一寸刻度。"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "xue-jian",
      "fact_id": "cen-leaked-exam-route",
      "state": "knows",
      "belief": "薛简已公开确认现有证据不支持岑照主动泄露试炼路线，并撤回更正此前基于副镜封签缺失、丙五座位置和岑照提前调用记录形成的判断。",
      "supersedes_fact_ids": [
        "cen-leaked-exam-route"
      ],
      "change": "薛简旧有的岑照可能主动泄露路线判断被新的镜屑、残痕先后、封签时间与反光角度证据链纠正。",
      "source_evidence": "“我此前依据副镜封签缺失、丙五座位置、岑照提前调用记录，判断岑照可能主动泄露第一层安全路线。该判断有记录依据，但现有镜屑、残痕先后、封签时间与反光角度已组成新的可复核链条。”\n\n他声音清楚，没有含混。\n\n“现有证据不支持岑照主动泄露试炼路线。此前判断，撤回更正。”"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "side-mirror-time-record",
      "state": "knows",
      "belief": "薛简掌握辰时一刻副镜移出、辰时二刻应归架未封、辰时二刻又三分岑照无正式监考复核调用低限试场、辰时二刻后反光纸位置登记成形，并知道第三节点残痕与取屑同测证明候场副镜反射路径能够成立。",
      "supersedes_fact_ids": [
        "side-mirror-time-record"
      ],
      "change": "薛简对副镜时间线与反光链条的调查状态完成为已知事实。",
      "source_evidence": "“辰时一刻，阮青将校准副镜移出维护架。辰时二刻，按规应归架封存，未封。”\n\n阮青低声道：“属实。”\n\n“辰时二刻又三分，岑照调用低限试场。调用簿有其灵印，无正式监考复核。”\n\n岑照道：“属实。”\n\n薛简再翻座次册：“丙五座在候场廊第三柱前。该位置与副镜反光线相交。辰时二刻后，反光纸位置登记成形，唐桥所绘路线与第一层安全纹路相似。”\n\n唐桥小声纠正：“原名运气图。”\n\n安苇看他一眼：“现名传播风险材料。”\n\n薛简将镜屑封样放到时间线中央。\n\n“第三节点残痕显示，安全纹路先自候场副镜方向入回声链。今日取屑同测，证明该反射路径在当时能够成立。也就是说，考生路线相似，不必以监考弟子主动传递为唯一解释。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "temporary-proctor-qualification",
      "state": "knows",
      "belief": "安苇确认岑照主动泄露嫌疑已被更正，但岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动低限试场仍是程序违规，临时监考资格暂不恢复。",
      "supersedes_fact_ids": [
        "temporary-proctor-qualification"
      ],
      "change": "安苇对岑照临时监考资格的调查转为明确裁定：暂不恢复，待伤势流程与重开复核完成后再裁定。",
      "source_evidence": "安苇最后看向岑照：“漏做候场副镜第二道封镜检查，记程序违规。无正式监考复核，提前启动低限试场，另记程序违规。主动泄露嫌疑更正，不抵消这两项。”\n\n岑照道：“认。”\n\n“临时监考资格暂不恢复。伤势流程与重开复核完成后再裁定。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "shared-route-origin",
      "state": "knows",
      "belief": "岑照知道证据链只能证明先副镜、后纸面、再入第三节点的方向和先后，不能证明是谁摆的或为何摆，也不能免除自己的程序责任。",
      "supersedes_fact_ids": [
        "shared-route-origin"
      ],
      "change": "岑照对反光路径证据的认知从调查推进为明确限定证明范围。",
      "source_evidence": "岑照闭了一下发酸的左眼，才道：“先副镜，后纸面，再入第三节点。只见先后，不见是谁摆的，也不见为何摆。”"
    },
    {
      "character_id": "ruan-qing",
      "fact_id": "unsealed-calibration-mirror",
      "state": "knows",
      "belief": "阮青承认辰时一刻将校准副镜移出维护架，辰时二刻按规应归架封存但未封，并领记维护责任。",
      "supersedes_fact_ids": [
        "unsealed-calibration-mirror"
      ],
      "change": "阮青未封校准副镜的维护责任被本人承认并由安苇记录。",
      "source_evidence": "“辰时一刻，阮青将校准副镜移出维护架。辰时二刻，按规应归架封存，未封。”\n\n阮青低声道：“属实。”"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "lucky-route-sketch-source",
      "state": "knows",
      "belief": "唐桥知道自己绘制并传播的运气图被定性为传播风险材料，不能作为正式考题证据，也不能证明可通过后续心境关。",
      "supersedes_fact_ids": [
        "lucky-route-sketch-source"
      ],
      "change": "唐桥对运气图性质的认知被安苇纠正为传播风险材料。",
      "source_evidence": "“唐桥，将副镜反光形成的第一层安全纹路绘为运气图并传播。该图只能解释开场避障相似，不能作为正式考题证据，更不能证明其可通过后续心境关。记传播风险。”\n\n唐桥看了一眼自己的图：“那它还叫运气图吗？”\n\n“封样名称不按你的愿望写。”\n\n“明白。”"
    }
  ],
  "thread_changes": [
    {
      "change": "副镜反光证据链完成：镜屑断面、封纹刀旧划、槽内受力痕、反光纸折角与第三节点低亮残痕角度互证，证明第一层安全纹路曾由候场副镜特定角度反射，经纸面入回声链。",
      "source_evidence": "薛简亲自落笔：“镜屑断面、封纹刀旧划、槽内受力痕、反光纸折角及第三节点低亮残痕，角度可互证。第一层安全纹路曾由候场副镜特定角度反射，经纸面入回声链。”"
    },
    {
      "change": "低亮连测完成，第三节点复核扣扣死，问心镜阵主镜与三处回声节点均可复核校准完成。",
      "source_evidence": "这一次，低亮残痕顺着封纹完整归环。第三节点复核扣发出一声清脆轻响，严丝合缝地扣死。\n\n主镜与三处回声节点的低亮回环同时稳定下来。\n\n安苇验过复核扣，又检查副镜封纹，才在校准册上落印：“主镜、第一、第二、第三回声节点，可复核校准完成。候场副镜封纹完成。镜砂余额两份。”"
    },
    {
      "change": "下一场随机幻境重开前的安全检查流程新增反光物签收项，需重开前逐件验角。",
      "source_evidence": "安苇提笔，在候场检查条目末尾添下一行：“考生携入之纸、金属、釉面器物，另设反光物签收项。重开前逐件验角。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥试图把副镜反光解释成考场给勤快人的运气提示，结果反而促成安苇新增反光物签收项。",
      "source_evidence": "唐桥站在廊柱阴面，踮脚看了两眼：“这光倒像它自己认路。”\n\n安苇头也没抬：“退回阴线。”\n\n唐桥老实退了一步，又忍不住道：“弟子只是申明，那日若也是镜子自己照过来，考生看懂了，是否算考场给勤快人的运气提示？”\n\n岑照的目光仍落在低亮尺上。\n\n“反光不是提示。能被带走，就是传播风险。”\n\n“可弟子没有带镜子。”\n\n“你带了纸。”\n\n唐桥低头看向封物匣里那张三折反光纸，没再出声。\n\n安苇提笔，在候场检查条目末尾添下一行：“考生携入之纸、金属、釉面器物，另设反光物签收项。重开前逐件验角。”\n\n唐桥张了张嘴。\n\n他这一番申诉，没替自己减掉半笔，倒替往后的考生多添了一道签收。"
    },
    {
      "change": "唐桥坚持运气图旧名，被安苇当场改称传播风险材料。",
      "source_evidence": "薛简再翻座次册：“丙五座在候场廊第三柱前。该位置与副镜反光线相交。辰时二刻后，反光纸位置登记成形，唐桥所绘路线与第一层安全纹路相似。”\n\n唐桥小声纠正：“原名运气图。”\n\n安苇看他一眼：“现名传播风险材料。”"
    }
  ],
  "new_constraints": [
    {
      "change": "重开前新增反光物签收项，考生携入之纸、金属、釉面器物需逐件验角。",
      "source_evidence": "安苇提笔，在候场检查条目末尾添下一行：“考生携入之纸、金属、釉面器物，另设反光物签收项。重开前逐件验角。”"
    },
    {
      "change": "唐桥的运气图只能解释开场避障相似，不能作为正式考题证据，也不能证明其可通过后续心境关。",
      "source_evidence": "“唐桥，将副镜反光形成的第一层安全纹路绘为运气图并传播。该图只能解释开场避障相似，不能作为正式考题证据，更不能证明其可通过后续心境关。记传播风险。”"
    },
    {
      "change": "岑照仍需在下一步使用清神符稳定回声并做低强度观想，由安苇确认左眼镜灼是否解除；今日不痊愈。",
      "source_evidence": "安苇收起校准册：“高亮镜纹继续停用。镜屑已经取出，下一步用清神符稳定回声，再做低强度观想。由我确认左眼镜灼是否解除。”\n\n“不是今日？”岑照问。\n\n“今日只到取屑与停亮。伤势不因证据齐了便痊愈。”"
    },
    {
      "change": "明日重开随机幻境前必须先验候场分区、携物与封纹；岑照仍不得触阵枢，不得独自入深层幻境，需带上清神符。",
      "source_evidence": "“明日先验候场分区、携物与封纹，再开随机幻境。岑照，你仍不得触阵枢，不得独自入深层幻境。带上清神符。”"
    }
  ],
  "resolved_constraints": [
    {
      "change": "薛简对岑照主动泄露试炼路线的旧怀疑解除并公开更正。",
      "source_evidence": "“我此前依据副镜封签缺失、丙五座位置、岑照提前调用记录，判断岑照可能主动泄露第一层安全路线。该判断有记录依据，但现有镜屑、残痕先后、封签时间与反光角度已组成新的可复核链条。”\n\n他声音清楚，没有含混。\n\n“现有证据不支持岑照主动泄露试炼路线。此前判断，撤回更正。”"
    },
    {
      "change": "第三回声节点复核扣等待副镜封纹连测后确认的状态解除，复核扣已经扣死。",
      "source_evidence": "这一次，低亮残痕顺着封纹完整归环。第三节点复核扣发出一声清脆轻响，严丝合缝地扣死。"
    }
  ],
  "next_chapter_inputs": [
    "第九章可从安苇安排重开前安全复核开始：明日先验候场分区、携物与封纹，再开随机幻境。",
    "重开前新增反光物签收项：考生携入之纸、金属、釉面器物需逐件验角。",
    "主镜、第一、第二、第三回声节点已可复核校准完成；候场副镜封纹完成；第三节点复核扣已扣死。",
    "考场镜砂余额为2份；exam-hall-reset-seal余额仍沿用上一状态为1枚，本章未变化。",
    "岑照仍处炼气四层，本章未突破，未消耗下品灵石或清神符用于突破。",
    "岑照left-eye-mirror-burn未解除：镜屑已经取出，高亮镜纹继续停用，下一步需用清神符稳定回声，再做低强度观想，由安苇确认是否解除。",
    "岑照临时监考资格暂不恢复；仍不得触阵枢，不得独自入深层幻境。",
    "薛简已公开更正现有证据不支持岑照主动泄露试炼路线，但岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动低限试场两项程序违规仍在。",
    "阮青留置未封校准副镜于候场廊、未及时归架、未补做封纹，已被安苇记维护责任。",
    "唐桥的运气图被记为传播风险材料，只能解释开场避障相似，不能作为正式考题证据，也不能证明其可通过后续心境关。"
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
  "source_sha256": "f3782eb79b10e8885c6664d8d1e1c1a8c8099da74657efa5c92718fa014325dc",
  "entity_changes": [
    {
      "change": "重开前安全复核完成并通过，复核范围包括主镜、三处回声节点、候场副镜封纹、无反光斜角分区和反光物签收项。",
      "source_evidence": "复查结束后，涉反光图考生被拆成三组，座次也与原先反光角度完全错开。安苇重新走过候场廊，确认纸张入袋、金属入盒、釉面器物遮光，才在六项之后落下“通过”二字。"
    },
    {
      "change": "涉反光图考生入场前被追加携物拆包验角、座次复核、分组拆开并调入无反光斜角分区。",
      "source_evidence": "薛简已转向候场执事：“按反射源不明项追加复查。所有涉反光图考生，携物拆包验角，座次与签收条复核。原同组者分开，调入无反光斜角分区后再入场。每次调位记时、记座，不得口头换位。”"
    },
    {
      "change": "监督下的随机幻境考试已经重开，首批考生进入随机心境关。",
      "source_evidence": "第一批考生踏入镜门，廊下山石立刻化作一座雨夜渡口。河上没有唐桥图里的三折安全纹，只有三艘一模一样的旧舟。舟夫分别开口，要考生交出一件最不愿失去之物。"
    }
  ],
  "relationship_changes": [
    {
      "change": "薛简继续作为正式监考复核岑照的操作意见，岑照只能在其复述确认下协助重开。",
      "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "recovery",
      "change": "岑照完成左眼镜灼解除流程，安苇确认残留镜屑已取出、高亮镜纹持续停用、清神符已稳定回声、低强度观想完成，且无重影、无神识刺痛加剧、无距离误判。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "第三轮结束，清神符已化作一小撮灰白符烬。安苇先验左眼灵光，再查神识回声，最后翻到镜屑封样与高亮镜纹停用记录。\n\n“残留镜屑已取出，高亮镜纹持续停用，清神符已稳定回声，低强度观想完成。无重影，无神识刺痛加剧，无距离误判。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "recovery",
      "change": "岑照的 left-eye-mirror-burn 在突破前按流程正式解除，解除与突破无关。",
      "state_id": "left-eye-mirror-burn",
      "state_action": "resolve",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "她在伤势栏落印。\n\n“left-eye-mirror-burn，左眼镜灼，现于突破前按流程正式解除。解除与突破无关。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照伤势解除后仍未恢复独立监考资格，只能在正式监考复核下协助重开，仍不得独自进入深层幻境、触阵枢或单独下令调镜。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照不得独自进入深层幻境、不得触阵枢的限制继续有效，并明确包含不得单独下令调镜。",
      "state_id": "solo-deep-illusion-ban",
      "state_action": "set",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "progress",
      "change": "岑照在随机幻境中启动炼气四层到炼气五层的突破流程，但尚未完成突破，境界仍为炼气四层。",
      "state_id": "",
      "state_action": "",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "随机幻境又一次变化，考生脚下的石阶忽然倒悬。镜中回声随之翻转，岑照的神识回路被猛地拉成一线。两枚灵石迅速黯下去，灵力冲入四层瓶颈，却没有将它撞开，只在临界处不断回荡。\n\n安苇抬眼：“突破已启动，尚未完成。守住完整回路。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "progress",
      "change": "岑照在突破启动时维持主镜与第一节点这一处回声节点，不牵第二、第三节点。",
      "state_id": "",
      "state_action": "",
      "stage_after": "炼气四层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "岑照的回声小周天骤然收紧。主镜的声音如潮涌来，第一节点则在潮后折返。他只维持这一处节点，不去牵第二、第三节点，也不越过浅层监看位。"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "cen-zhao",
      "resource_id": "low-grade-spirit-stone",
      "operation": "consume",
      "amount": 2,
      "unit": "枚",
      "resulting_balance": 2,
      "source_or_destination": "炼气四层到炼气五层突破起始供能槽",
      "change": "岑照消耗2枚下品灵石用于突破起始，余额由4枚降为2枚且不得返还。",
      "source_evidence": "岑照取出两枚下品灵石，放进浅层回环边界的两处供能槽。方才使用的清神符虽已化烬，其清明余力仍留在神识回路中，依规并入此次突破成本，不再另耗一张。\n\n安苇落笔：“下品灵石四减二，余二枚。清神符三减一，余二张。用途：稳定旧伤回声并承接突破起始。不得返还。”"
    },
    {
      "owner_id": "cen-zhao",
      "resource_id": "clarity-talisman",
      "operation": "consume",
      "amount": 1,
      "unit": "张",
      "resulting_balance": 2,
      "source_or_destination": "稳定旧伤回声并承接突破起始",
      "change": "岑照消耗1张清神符用于稳定旧伤回声并并入突破成本，余额由3张降为2张且不得返还。",
      "source_evidence": "岑照取出两枚下品灵石，放进浅层回环边界的两处供能槽。方才使用的清神符虽已化烬，其清明余力仍留在神识回路中，依规并入此次突破成本，不再另耗一张。\n\n安苇落笔：“下品灵石四减二，余二枚。清神符三减一，余二张。用途：稳定旧伤回声并承接突破起始。不得返还。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "tang-qiao",
      "fact_id": "random-heart-test-lucky-route-no-answer",
      "state": "knows",
      "belief": "唐桥知道自己的运气图无法提供随机心境关答案。",
      "supersedes_fact_ids": [],
      "change": "唐桥在随机心境关中发现运气图没有答案，不能帮助他应对心境之问。",
      "source_evidence": "唐桥摸出记熟的运气图，对着河岸比了两次。\n\n“图上这里应当有一道向右的亮纹。”\n\n舟夫问：“你交什么？”\n\n唐桥又看一眼图。\n\n图上没有答案。"
    },
    {
      "character_id": "xue-jian",
      "fact_id": "cen-zhao-assisted-reopen-under-review",
      "state": "knows",
      "belief": "薛简确认岑照只能在正式监考复核下协助随机幻境重开，不能独自进入深层幻境、触阵枢或单独下令调镜。",
      "supersedes_fact_ids": [],
      "change": "薛简明确掌握并执行岑照协助重开的资格边界。",
      "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "left-eye-mirror-burn-resolved-before-breakthrough",
      "state": "knows",
      "belief": "安苇确认岑照左眼镜灼已在突破前按流程正式解除，且解除与突破无关。",
      "supersedes_fact_ids": [],
      "change": "安苇完成并记录岑照伤势解除裁定。",
      "source_evidence": "她在伤势栏落印。\n\n“left-eye-mirror-burn，左眼镜灼，现于突破前按流程正式解除。解除与突破无关。”"
    }
  ],
  "thread_changes": [
    {
      "change": "唐桥和涉反光图考生的运气图材料继续保留为传播风险材料，不能提供随机心境关通关答案。",
      "source_evidence": "他身后的两名考生也因重新分组，站不到原来的角度，更找不到所谓反光路线。运气图只能留在封袋里，继续作为传播风险材料，半点不能替他们应对心境之问。"
    },
    {
      "change": "岑照漏做副镜第二道封镜检查和无正式监考复核提前启动试场两项程序责任仍未取消。",
      "source_evidence": "“漏做副镜第二道封镜检查、无正式监考复核提前启动试场，两项记录不变。”"
    },
    {
      "change": "随机幻境重开过程中出现主镜回声迟半息，处理方式是延后一息入场节拍，不调阵枢。",
      "source_evidence": "第三名考生入场时，主镜回声迟了半息。\n\n岑照没有伸手，只道：“主镜回声迟半息，第一节点尚未跟迟。”\n\n薛简复验后下令：“入场节拍延后一息，阵枢不调。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥把反光物签收项误解为重开考题提示并要求按纸类签收先后排座，反而触发携物复查和座次复核。",
      "source_evidence": "“既然特意写了三类物件，想来这三类之中必有一类与重开后的考题相合。我签收的是纸，应按纸类签收先后排座。若纸为首类，我也不求照顾，只求依规坐前排。”\n\n旁边两名抄过运气图的考生顿时把自己的签收条摸了出来。一人签的是铜扣，一人签的是釉面水囊，三人各执一类，眼看便要从木牌的字序争到座次的吉凶。"
    },
    {
      "change": "岑照用正式监考术语回应荒谬申诉，将唐桥的押题理解转化为实际复查流程。",
      "source_evidence": "岑照隔着封线道：“反射源不明，先复核携物。签收次序不构成考题凭据。”\n\n唐桥认真问：“那木牌为何把纸写在最前？”\n\n“纸最易折成斜角。”\n\n“所以斜角重要？”\n\n“所以你的纸要再查一遍。”"
    },
    {
      "change": "唐桥把签收条当提示，结果该纸条让他多出拆包、验角、调组三道手续。",
      "source_evidence": "唐桥低头看着自己的签收条。那张被他视作重开提示的纸，当场替他添了拆包、验角、调组三道手续。"
    }
  ],
  "new_constraints": [
    {
      "change": "反光物签收项引发申诉后，所有涉反光图考生必须携物拆包验角、座次与签收条复核，原同组者分开并调入无反光斜角分区后再入场。",
      "source_evidence": "薛简已转向候场执事：“按反射源不明项追加复查。所有涉反光图考生，携物拆包验角，座次与签收条复核。原同组者分开，调入无反光斜角分区后再入场。每次调位记时、记座，不得口头换位。”"
    },
    {
      "change": "岑照突破资源投入后不得返还。",
      "source_evidence": "安苇落笔：“下品灵石四减二，余二枚。清神符三减一，余二张。用途：稳定旧伤回声并承接突破起始。不得返还。”"
    },
    {
      "change": "岑照在突破启动中只可维持主镜与第一节点，不得再增加回声节点。",
      "source_evidence": "薛简盯着复核刻度：“主镜与第一节点，闭合。不得再加。”"
    }
  ],
  "resolved_constraints": [
    {
      "change": "岑照 left-eye-mirror-burn 伤势正式解除。",
      "source_evidence": "她在伤势栏落印。\n\n“left-eye-mirror-burn，左眼镜灼，现于突破前按流程正式解除。解除与突破无关。”"
    }
  ],
  "next_chapter_inputs": [
    "岑照仍处炼气四层，炼气四层到炼气五层突破已启动但尚未完成，下一章从两道回声在瓶颈前相撞的临界状态继续。",
    "岑照左眼镜灼 left-eye-mirror-burn 已在突破前按流程正式解除，解除原因来自残留镜屑取出、高亮镜纹停用、清神符稳定回声和低强度观想，不能再作为活动伤势处理。",
    "岑照已消耗2枚下品灵石和1张清神符，余额为2枚下品灵石、2张清神符，突破资源不得返还。",
    "岑照临时监考资格仍未恢复为可独立操作状态；仍不得独自进入深层幻境、不得触阵枢、不得单独下令调镜，每次操作意见需由薛简复述确认。",
    "下一章岑照突破过程中仍只能维持主镜与一处回声节点，不能同时维持超过一处回声节点。",
    "随机幻境考试已在监督下重开，唐桥及涉反光图考生已被拆组并进入后续随机心境关，运气图不能提供通关答案，只能作为传播风险材料。",
    "考场镜砂余额仍为2份；exam-hall-reset-seal余额仍为1枚，已消耗的1枚不返还。",
    "岑照漏做副镜第二道封镜检查、无正式监考复核提前启动试场两项程序责任仍未取消。"
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
  "source_sha256": "49bf276f1877fdf391e2c4dc2524578eb4da1f54fd71ae0b55102dbfcae3dbae",
  "entity_changes": [
    {
      "change": "岑照取得带附加条件的临时监考牌。",
      "source_evidence": "最后，安苇取出一块青灰色木牌。\n\n牌面只有“临时监考”四字，背面却密密刻着数行小字。\n\n她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
    },
    {
      "change": "问心镜阵主镜、三处回声节点及候场副镜完成可复核校准，随机幻境考试可在正式监考监督下继续运行。",
      "source_evidence": "她核对阵图：“主镜、三处回声节点及候场副镜，均完成可复核校准。随机幻境考试可在正式监考监督下继续运行。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "薛简成为岑照后续调镜操作前必须找的正式监考复核人之一。",
      "source_evidence": "薛简合上调用册：“下次调镜，先找我签字。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "cen-zhao",
      "kind": "breakthrough",
      "change": "岑照在随机幻境中完成完整神识回路运转，正式从炼气四层突破至炼气五层。",
      "state_id": "",
      "state_action": "",
      "stage_after": "炼气五层",
      "from_stage": "炼气四层",
      "to_stage": "炼气五层",
      "prerequisites": [
        "完成三处回声节点校准",
        "旧伤在突破前按规则正式解除",
        "在随机幻境中维持完整神识回路"
      ],
      "costs": [
        "2 枚下品灵石",
        "1 张清神符",
        "突破后回声分裂限制"
      ],
      "new_limits": [
        {
          "state_id": "post-breakthrough-echo-splitting",
          "description": "突破后回声分裂，症状为双重回声、深层定位延迟，暂停高强度监考。"
        },
        {
          "state_id": "solo-deep-illusion-ban",
          "description": "三日内不得独自进入深层幻境。"
        },
        {
          "state_id": "temporary-proctor-risk-review",
          "description": "所有镜阵操作须经正式监考复核，每日仅可进行低强度节点复核。"
        }
      ],
      "source_evidence": "瓶颈没有碎响，只有一瞬极静。\n\n紧接着，完整的神识回路穿过主镜，抵达第一节点，再循原路返回。原本需要逐段辨认的残痕同时浮在两处：主镜纹路先转，节点残痕后应，方向与先后清晰分开。\n\n炼气五层。"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "ability",
      "change": "岑照的照痕辨序提升为可同时分辨主镜与第一节点的残痕。",
      "state_id": "residual-mark-reading",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "岑照额角渗出冷汗。他能同时分辨主镜与第一节点的残痕了，却听见两重回声，连神识落点也比念头慢了半拍。"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照新增突破后回声分裂活动限制，表现为双重回声、深层定位延迟，并暂停高强度监考。",
      "state_id": "post-breakthrough-echo-splitting",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "安苇在监督册上记下：“岑照，炼气五层。突破后回声分裂。症状：双重回声、深层定位延迟。暂停高强度监考。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照三日内不得独自进入深层幻境的限制继续有效，并被写入临时监考牌附加条件。",
      "state_id": "solo-deep-illusion-ban",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
    },
    {
      "subject_id": "cen-zhao",
      "kind": "restriction",
      "change": "岑照的临时监考操作限制更新为所有镜阵操作须经正式监考复核，候场反光物检查也须由正式监考复核，每日仅可进行低强度节点复核。",
      "state_id": "temporary-proctor-risk-review",
      "state_action": "set",
      "stage_after": "炼气五层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "xue-jian",
      "fact_id": "cen-zhao-not-supported-as-route-leaker",
      "state": "knows",
      "belief": "现有证据不支持岑照主动泄露试炼路线，薛简原先关于岑照可能主动泄露路线的判断已更正。",
      "supersedes_fact_ids": [
        "cen-leaked-exam-route"
      ],
      "change": "薛简公开更正岑照主动泄露试炼路线的判断不成立。",
      "source_evidence": "薛简上前一步，声音传过整个复核席。\n\n“我先前依据封签缺口、座次重合与试场调用记录，判断岑照可能主动泄露路线。现有副镜角度、镜屑、残痕先后与封签时间已经构成新证据链。现有证据不支持岑照主动泄露试炼路线。原判断更正。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "cen-zhao-procedure-violations-recorded",
      "state": "knows",
      "belief": "岑照漏做候场副镜第二道封镜检查，并在无正式监考复核时提前启动试场，两项程序违规记过，救场与突破均不抵扣。",
      "supersedes_fact_ids": [],
      "change": "安苇记录岑照两项程序违规并记过。",
      "source_evidence": "他停了一息，又道：“但岑照漏做候场副镜第二道封镜检查，并在无正式监考复核时提前启动试场，记录无误。”\n\n安苇提笔：“两项程序违规，记过。救场与突破均不抵扣。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "ruan-qing-side-mirror-maintenance-liability",
      "state": "knows",
      "belief": "阮青留置未封校准副镜于候场廊，维护责任入档。",
      "supersedes_fact_ids": [],
      "change": "安苇将阮青留置未封校准副镜于候场廊记入维护责任。",
      "source_evidence": "“阮青留置未封校准副镜于候场廊，维护责任入档。唐桥传播由反光形成的运气图草图，作为传播风险事实入档，不作正式考题泄露认定，也不作答题凭据。”"
    },
    {
      "character_id": "an-wei",
      "fact_id": "tang-qiao-reflection-sketch-spread-risk",
      "state": "knows",
      "belief": "唐桥传播由反光形成的运气图草图，该事实作为传播风险入档，不作正式考题泄露认定，也不作答题凭据。",
      "supersedes_fact_ids": [],
      "change": "安苇将唐桥传播反光运气图草图作为传播风险事实入档。",
      "source_evidence": "“阮青留置未封校准副镜于候场廊，维护责任入档。唐桥传播由反光形成的运气图草图，作为传播风险事实入档，不作正式考题泄露认定，也不作答题凭据。”"
    },
    {
      "character_id": "tang-qiao",
      "fact_id": "random-heart-test-lucky-route-no-answer",
      "state": "knows",
      "belief": "运气图只押中开场，不包后续，不能作为随机心境关答题依据。",
      "supersedes_fact_ids": [
        "random-heart-test-lucky-route-no-answer"
      ],
      "change": "唐桥确认运气图无法提供随机心境关答案，并申诉将其改记为普通经验但被拒。",
      "source_evidence": "唐桥想了片刻，郑重申诉：“弟子不求把它算答案。能否改记为普通经验？只押中开场，不包后续。”\n\n“不能。”薛简道，“考场没有‘只包开场’的答题依据。”"
    },
    {
      "character_id": "cen-zhao",
      "fact_id": "temporary-proctor-conditions-known",
      "state": "knows",
      "belief": "岑照知道自己只取得附加条件下的临时监考牌，所有镜阵操作须经正式监考复核，三日内不得独自进入深层幻境，每日仅可进行低强度节点复核。",
      "supersedes_fact_ids": [],
      "change": "岑照接收并知晓临时监考牌的附加条件。",
      "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”\n\n岑照接牌时，耳中那道迟来的回声又将“低强度节点复核”重复了一遍。"
    }
  ],
  "thread_changes": [
    {
      "change": "随机心境关继续按随机变化运行，反光草图只能绕过开场陷阱，不能作为后续通关答案。",
      "source_evidence": "其余涉反光图考生依次出关，有人通过，有人失分，结果全按随机心境关中的实际选择登记。那张草图只帮他们绕过了开场陷阱，遇上变换的山路、雨街与取舍问境，便再没有一笔可照着走。"
    },
    {
      "change": "副镜镜屑、座次、残痕先后、封签时间和镜面角度构成证据链，证明现有证据不支持岑照主动泄露试炼路线。",
      "source_evidence": "“候场副镜边缘镜屑已取出。座次与反光纸位置吻合；残痕先后显示安全纹路先由副镜反射方向进入回声链；封签时间晚于副镜移出；镜面角度可形成第一层安全纹路，但不能显示后续随机心境关。”"
    },
    {
      "change": "突破后薛简接管全部调镜口令，阮青关闭第二节点外沿响应，考场未因岑照突破后的回声分裂而错层。",
      "source_evidence": "薛简接过全部调镜口令：“主镜稳位。第一节点由岑照维持，第二、第三节点归我。阮青，关闭第二节点外沿响应。”\n\n阮青当即落下隔纹扣。\n\n主镜中的雨街轻晃了一下，没有错层。独木桥仍在远处，长街也没有与山路重叠。"
    },
    {
      "change": "资源账目最终确认：考场重置印余额一枚、镜砂余额二份、岑照下品灵石余额二枚、清神符余额二张，所有消耗已定账且不返还。",
      "source_evidence": "“考场重置印原有二枚，已消耗一枚，余额一枚，不返还。镜砂原有六份，修补主镜、三处回声节点及副镜封纹后，余额二份。岑照下品灵石原有四枚，余额二枚；清神符原有三张，余额二张。所有消耗已定账。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "唐桥试图把运气图改名为普通经验、避坑心得或运势参照，均被薛简按考试记录否定。",
      "source_evidence": "“不能。”薛简道，“考场没有‘只包开场’的答题依据。”\n\n“那叫避坑心得？”\n\n“警示边界不是心得。”\n\n“运势参照？”\n\n“传播草图。”"
    },
    {
      "change": "唐桥的命名申诉反而促成候场反光物检查新增正式监考复核要求。",
      "source_evidence": "唐桥怔了怔：“弟子只是想给图换个名字。”\n\n薛简收走申诉纸：“你给它添了一道检查。”"
    },
    {
      "change": "临时监考牌本身会反光，因此薛简要求岑照未复核前不得拿去候场照字。",
      "source_evidence": "唐桥探头看了一眼：“这牌也会反光。”\n\n薛简立刻将牌按回岑照掌中：“所以收好。未复核前，不得拿去候场照字。”"
    }
  ],
  "new_constraints": [
    {
      "change": "岑照突破后暂停高强度监考。",
      "source_evidence": "安苇在监督册上记下：“岑照，炼气五层。突破后回声分裂。症状：双重回声、深层定位延迟。暂停高强度监考。”"
    },
    {
      "change": "突破、救场与已耗资源均不抵扣岑照程序违规，已耗灵石与清神符不返还。",
      "source_evidence": "她抬眼：“已耗灵石与清神符不返还。突破不计修阵，不抵违规。”"
    },
    {
      "change": "候场反光物检查以后须由正式监考复核，不得由临时监考单独确认。",
      "source_evidence": "她又指向唐桥的申诉纸：“把‘只押中开场、不包后续’原句抄入传播风险说明。以后候场反光物检查，须由正式监考复核。不得由临时监考单独确认。”"
    },
    {
      "change": "岑照的临时监考牌附加违规记过保留、所有镜阵操作须经正式监考复核、候场反光物检查须由正式监考复核、三日内不得独自进入深层幻境、每日仅可进行低强度节点复核。",
      "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
    },
    {
      "change": "岑照三日后再复核回声分裂，期间不得自行验证。",
      "source_evidence": "安苇看着他：“听见几遍？”\n\n“两遍。”\n\n“三日后再复核。期间不得自行验证。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "岑照已从炼气四层突破至炼气五层，可同时比较主镜与一处回声节点的残痕，但仍不能读取记忆、判断动机或预知随机变化。",
    "post-breakthrough-echo-splitting 仍为活动限制，症状为双重回声、深层定位延迟；岑照暂停高强度监考，三日后再复核，期间不得自行验证。",
    "岑照持有带条件的临时监考牌；违规记过保留，所有镜阵操作须经正式监考复核，候场反光物检查须由正式监考复核，三日内不得独自进入深层幻境，每日仅可进行低强度节点复核。",
    "薛简已公开更正：现有证据不支持岑照主动泄露试炼路线；但岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动试场两项程序违规已记过。",
    "阮青留置未封校准副镜于候场廊的维护责任已入档；唐桥传播由反光形成的运气图草图作为传播风险事实入档，不作正式考题泄露认定，也不作答题凭据。",
    "问心镜阵主镜、三处回声节点及候场副镜均完成可复核校准，随机幻境考试可在正式监考监督下继续运行。",
    "资源账目保持：exam-hall-reset-seal 余额为 1 枚，mirror-sand 余额为 2 份，岑照 low-grade-spirit-stone 余额为 2 枚，clarity-talisman 余额为 2 张；所有已消耗资源均不得回补。",
    "随机心境关继续证明运气图只可绕过开场陷阱，不能提供后续随机问境答案。"
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
        "change": "第一轮试炼中止，所有考生须原地闭目并依座次退出，且不得交谈、交换纸笔或毁弃随身物。",
        "source_evidence": "“第一轮试炼中止。”他声音不高，却盖住了所有争辩，“所有考生原地闭目，依座次退出。不得交谈，不得交换纸笔，不得毁弃随身物。”"
      },
      {
        "change": "二十四块座次牌背面新增每名考生在雾桥上的位置与绕行次序。",
        "source_evidence": "薛简取出封签，先封阵门，又令执役弟子按座次领人。原本只记姓名的二十四块座次牌，被他逐一翻到背面，添上每人在雾桥上的位置与绕行次序。"
      },
      {
        "change": "唐桥的运气图被发现，其路线与第一层泥沼幻象外沿和三处雾坑位置相近。",
        "source_evidence": "那道弯线并不精确，却恰好从第一层泥沼幻象的外沿绕过；三团墨点的位置，也和开场最容易触发的三处雾坑相近。"
      },
      {
        "change": "运气图、警示抄本、座次牌和行动次序被分列封存，第一轮重排时辰被记入，考生后续心境关取消并转送候场廊分区看管。",
        "source_evidence": "封签一张接一张落下。运气图、警示抄本、座次牌和行动次序被分列封存，第一轮重排的时辰也一并记入。考生原定的后续心境关全部取消，转送候场廊分区看管。"
      },
      {
        "change": "候场廊三处分区门合拢，唐桥的运气图被夹入证物册。",
        "source_evidence": "最后一道封签落在主镜铜框上。候场廊三处分区门同时合拢，唐桥的运气图被夹入证物册，露出的那截弯线，正贴着雾桥陷阱的边缘。"
      },
      {
        "change": "座次核对确认绕过开场落藤陷阱的十一名考生中只有两名来自临川郡，绕行人群并非都与岑照同乡。",
        "source_evidence": "一块块座次牌移到封存桌左侧。绕过开场落藤陷阱的十一名考生中，只有唐桥和另外一人来自临川郡，另有三人此前同岑照说过话，却只是进场时问过警示牌能不能抄。"
      },
      {
        "change": "主镜残痕显示安全纹路在第一批考生入场前已有回照，且残痕经过候场副镜方向。",
        "source_evidence": "岑照看向主镜下方的启阵时标。银纹重影晃了一下，他退开半步，重新对准：“早于第一批考生入场。部分第一层安全纹路，在他们进场前已经留下回照残痕。”"
      },
      {
        "change": "候场廊校准副镜在特定复原角度下能把第一层安全纹路的一部分反射到唐桥纸面上。",
        "source_evidence": "一道极淡的银光从副镜边缘斜落下来，在纸上折出三段断续细线。它们拼不成完整路线，却恰好显出落藤区左侧的空隙、石壁转角和第一处安全落脚点。"
      },
      {
        "change": "阮青承认校准副镜在开考前辰时二刻左右暂放候场廊，且未能回答何时封存。",
        "source_evidence": "安苇问：“副镜为何在这里？”\n\n“校准后暂放。”\n\n“何时开始暂放？”\n\n阮青抿了抿唇：“开考前。”\n\n“具体。”\n\n“辰时二刻左右。”\n\n“何时封存？”\n\n阮青没答。"
      },
      {
        "change": "唐桥承认自己画的运气图前三折来自副镜反光显示的三段线，后一笔是自己添的。",
        "source_evidence": "唐桥盯着纸面，神色难得认真：“我画的就是这三折。后面那一笔，是我觉得三折不够吉利，添的。”"
      },
      {
        "change": "问心镜阵在低限复测中确认主镜与第一回声节点存在错层，安全纹路与陷阱落点短暂错开，镜阵未修复。",
        "source_evidence": "两息之内，淡青光带向右偏了一寸，又缓缓归位。石刺没有归位，反而在原处留下半透明重影。\n\n主镜与节点，已经不在同一层上。"
      },
      {
        "change": "阮青关于校准副镜从维护架移入候场廊的时间出现前后矛盾，只形成时间疑点。",
        "source_evidence": "“我搬的。也可能……下签之后才搬。”\n\n安苇只道：“两种时刻都记。今日不替你选。”"
      },
      {
        "change": "唐桥的运气图仍处于封存和补充申诉材料状态，来源链未被证明。",
        "source_evidence": "唐桥把封存中的运气图申诉又递了上来，纸角新添了一行字：错层既生，图路或为天意所示。\n\n安苇划掉“天意”二字：“改写物件来源、所见角度、作图时刻。其余不收。”"
      },
      {
        "change": "问心镜阵主镜完成一处裂纹封补，但不视为全阵修复。",
        "source_evidence": "安苇提笔登记：“镜砂一份，去向：主镜裂纹封补。考场镜砂由六份减至五份。主镜仅完成一处封补，不视为全阵修复。”"
      },
      {
        "change": "第一回声节点完成低亮度临时校准，扣环停在半锁位置，仍需复核。",
        "source_evidence": "第三次转环后，节点的低鸣终于与主镜同拍。\n\n阮青刚要扣死外环，安苇伸手挡住：“临时校准。先留复核扣。”\n\n薛简补道：“还要与第二、第三节点连测。单点同拍，不等于全阵无错。”"
      },
      {
        "change": "校准副镜仍在候场廊封存架，未启封，并被单独列为封存首项。",
        "source_evidence": "封存架被重新打开，灰布、铜笔洗、照面小镜逐件移到桌上。副镜仍未启封，却已被单独列在首项。"
      },
      {
        "change": "执事从书箱夹层里发现三张折成同样大小的反光纸。",
        "source_evidence": "候场廊另一头，执事从一只书箱夹层里抽出三张折成同样大小的反光纸。"
      },
      {
        "change": "主镜与第一回声节点完成一次低亮连测，残痕方向与先后可连上；第一节点仍为可复核临时校准，复核扣待第二节点三点连测后再决定是否锁。",
        "source_evidence": "薛简照原话写下，又补了一行：“第一节点为可复核临时校准，待第二节点三点连测后，再决定是否锁复核扣。”"
      },
      {
        "change": "三张反光纸的持有人、原位置、折法与可成角度已登记并封存。",
        "source_evidence": "她拿过候场清单，在原座次图上划出三道间距线：“丙五座与书箱分开两砖。所有座次与廊柱、窗面、铜器至少隔一砖半。笔、纸、墨碟、玉扣及能反光的器物另列一册。三张纸登记持有人、原位置、折法与可成角度，全部封存。”"
      },
      {
        "change": "第三张反光纸确认为丙五座唐桥相关物件，原放在书箱右侧夹层，折成三叠，唐桥称借来比线。",
        "source_evidence": "执事念道：“丙五座，唐桥。原放在书箱右侧夹层，折成三叠。唐桥称不是他的纸，只是借来比线。”"
      },
      {
        "change": "候场廊复原出第三张反光纸在特定位置、折法和角度下可映出与唐桥运气图前三折相近的第一层安全纹路。",
        "source_evidence": "第二次斜光穿过副镜原位，落上第三张反光纸。纸面顿时亮起三段弯折的淡纹：先向左避开一道窄线，再斜过中央，最后折回右侧。\n\n薛简立刻将唐桥的运气图压在旁边。前三折虽长短略有差别，转向却近乎一致。"
      },
      {
        "change": "第二回声节点完成低亮补砂修复，低亮试合后旁痕不再回折，先后可辨。",
        "source_evidence": "镜砂入纹，第二节点轻轻一震。岑照没有看震光，只听铜铃三响的间隔。\n\n薛简按规程复述：“低亮试合。西南主线入齿，旁痕不再回折，二者先后可辨。岑照？”"
      },
      {
        "change": "主镜、第一回声节点、第二回声节点完成三点低亮连测；第一节点复核扣扣死，第二节点留待第三节点连测。",
        "source_evidence": "岑照闭左眼听完：“主镜先，第一次之，第二后接。第一节点可扣复核扣。第二节点需等第三节点同线后再扣死。”\n\n薛简没有反驳，取出小铜扣，将第一节点封册上的复核扣压下。咔的一声，清脆得像案上多了一条规矩。\n\n“第一回声节点复核扣扣死。”薛简记录，“第二节点留待第三节点连测。”"
      },
      {
        "change": "考生管理流程新增涉反光图考生告知签收，反光物件清单增加“告知签收”栏。",
        "source_evidence": "候场廊里的队伍因此多绕了一折。执事把涉图考生单独列名，反光物件清单后又添一栏“告知签收”。原本准备重开前只查座次与封签，如今还要查谁把影子当凭据。"
      },
      {
        "change": "第三回声节点低亮裂缝已用一份镜砂修补，主镜、第一、第二、第三回声节点形成低亮回环连测链路。",
        "source_evidence": "镜砂落入铜扣，细如星屑。阮青以浅层镜纹把它铺开，不敢越过薛简划出的阵枢线。第三节点的抖动慢慢止住，低亮光从主镜绕第一节点、第二节点，再经第三节点回环。"
      },
      {
        "change": "第二回声节点复核扣已扣死。",
        "source_evidence": "薛简把第二回声节点复核扣压下，铜扣“咔”地扣死。阮青眼巴巴看向第三扣。"
      },
      {
        "change": "第三回声节点本体可连测，但第三节点复核扣暂缓，需等候场副镜封纹连测后确认。",
        "source_evidence": "岑照立刻收眼：“第三节点本体可连测。复核扣暂缓。副镜方向残痕未清，需与副镜封纹连测。”\n\n薛简照原话写下：“第三节点复核扣暂待候场副镜封纹连测后确认。”"
      },
      {
        "change": "候场副镜边缘封纹槽内发现疑似残留镜屑，已定位封存，本章未取出。",
        "source_evidence": "安苇把副镜推到封线内侧，让薛简以低亮照边。镜边封纹槽有一道极细的缺口，缺口里卡着一点暗银色碎屑。它不亮，却在角度尺影子移动时闪了一下。\n\n薛简皱眉：“镜屑？”\n\n阮青脸色一白：“封纹刀边缘也沾过细屑。我以为是主镜补砂时带的。”\n\n安苇没有伸手取，只取一枚小封罩扣在副镜边缘：“疑似残留镜屑，定位封存。取出需明日连同封签、角度、残痕同测。今日不取。”"
      },
      {
        "change": "阮青交出副镜封纹工具，副镜未及时归架并未补做封纹被安苇记为维护责任。",
        "source_evidence": "安苇指向阮青：“工具。”\n\n阮青双手奉上封纹刀和细砂匙：“都在。副镜那时只是……还没来得及归架。”\n\n安苇笔尖一顿：“‘未及时归架并未补做封纹’，记为维护责任。不要换词。”"
      },
      {
        "change": "唐桥的站位误认记录与反光纸、运气图一并封存为传播风险材料。",
        "source_evidence": "薛简将唐桥站位另列一栏：“反光纸、运气图、站位误认，一并封存作传播风险材料。唐桥，此线不是考题。”"
      },
      {
        "change": "候场副镜边缘残留镜屑已被取出、封样，并加两道灵印。",
        "source_evidence": "银色镜屑终于被挑出。阮青将它落入透明封样管，镜屑一面平滑，一面带着极细的斜擦纹。\n\n薛简把角度尺压到副镜边缘：“旧划在东偏南两格。受力痕由外向内。”\n\n“镜屑闪面再转半格。”岑照道。\n\n薛简复述，阮青依令微调封样管。低亮光从镜屑断面掠过，折向封物匣中的反光纸。纸上旧折角亮了一瞬，光线再落到第三回声节点的标尺边。\n\n薛简手中角度尺顿住。\n\n第三节点那道已经封存的入链残痕，正是同一方向。\n\n岑照闭了一下发酸的左眼，才道：“先副镜，后纸面，再入第三节点。只见先后，不见是谁摆的，也不见为何摆。”\n\n“记原话。”安苇道。\n\n薛简亲自落笔：“镜屑断面、封纹刀旧划、槽内受力痕、反光纸折角及第三节点低亮残痕，角度可互证。第一层安全纹路曾由候场副镜特定角度反射，经纸面入回声链。”\n\n镜屑被封样，封口再加两道灵印。"
      },
      {
        "change": "主镜、第一、第二、第三回声节点进入可复核校准完成状态，候场副镜封纹完成。",
        "source_evidence": "这一次，低亮残痕顺着封纹完整归环。第三节点复核扣发出一声清脆轻响，严丝合缝地扣死。\n\n主镜与三处回声节点的低亮回环同时稳定下来。\n\n安苇验过复核扣，又检查副镜封纹，才在校准册上落印：“主镜、第一、第二、第三回声节点，可复核校准完成。候场副镜封纹完成。镜砂余额两份。”"
      },
      {
        "change": "唐桥的运气图被安苇改列为传播风险材料，不再按唐桥自称的运气图定性。",
        "source_evidence": "薛简再翻座次册：“丙五座在候场廊第三柱前。该位置与副镜反光线相交。辰时二刻后，反光纸位置登记成形，唐桥所绘路线与第一层安全纹路相似。”\n\n唐桥小声纠正：“原名运气图。”\n\n安苇看他一眼：“现名传播风险材料。”"
      },
      {
        "change": "重开前安全复核完成并通过，复核范围包括主镜、三处回声节点、候场副镜封纹、无反光斜角分区和反光物签收项。",
        "source_evidence": "复查结束后，涉反光图考生被拆成三组，座次也与原先反光角度完全错开。安苇重新走过候场廊，确认纸张入袋、金属入盒、釉面器物遮光，才在六项之后落下“通过”二字。"
      },
      {
        "change": "涉反光图考生入场前被追加携物拆包验角、座次复核、分组拆开并调入无反光斜角分区。",
        "source_evidence": "薛简已转向候场执事：“按反射源不明项追加复查。所有涉反光图考生，携物拆包验角，座次与签收条复核。原同组者分开，调入无反光斜角分区后再入场。每次调位记时、记座，不得口头换位。”"
      },
      {
        "change": "监督下的随机幻境考试已经重开，首批考生进入随机心境关。",
        "source_evidence": "第一批考生踏入镜门，廊下山石立刻化作一座雨夜渡口。河上没有唐桥图里的三折安全纹，只有三艘一模一样的旧舟。舟夫分别开口，要考生交出一件最不愿失去之物。"
      },
      {
        "change": "岑照取得带附加条件的临时监考牌。",
        "source_evidence": "最后，安苇取出一块青灰色木牌。\n\n牌面只有“临时监考”四字，背面却密密刻着数行小字。\n\n她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
      },
      {
        "change": "问心镜阵主镜、三处回声节点及候场副镜完成可复核校准，随机幻境考试可在正式监考监督下继续运行。",
        "source_evidence": "她核对阵图：“主镜、三处回声节点及候场副镜，均完成可复核校准。随机幻境考试可在正式监考监督下继续运行。”"
      }
    ],
    "relationship_changes": [
      {
        "change": "薛简公开判断岑照涉嫌向同乡考生泄露第一层路线。",
        "source_evidence": "“流程要求先核名册，再由正式监考复签。你提前启阵，没有复核签；随后与安全路线相似的图出现在候场考生手里。主镜封签未破，外人无法直接接触阵图。依现有记录，我有理由判断，你涉嫌向同乡考生泄露第一层路线。”"
      },
      {
        "change": "薛简将岑照视为涉事监考，允许查残痕但不许岑照独查。",
        "source_evidence": "“可以查，但不是现在由你独查。”薛简把调用册合上，“你已是涉事监考。”"
      },
      {
        "change": "安苇介入后要求先封存证据，不先裁定动机。",
        "source_evidence": "安苇点头：“先封存，不先定动机。主镜、座次牌、调用册、考生纸片，分别加双签。候场廊内与反光有关的器物原位封住，任何人不得挪动。”"
      },
      {
        "change": "同乡关系作为岑照泄露路线证据的权重被下调，但薛简仍未排除岑照嫌疑。",
        "source_evidence": "薛简收拢座次牌：“同乡证据权重下调。封签未破、提前调用和图中路线相似，仍需核查。”"
      },
      {
        "change": "岑照后续只能在安苇与薛简监督下提供辨序协助，每次结论需由正式监考复述确认。",
        "source_evidence": "“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
      },
      {
        "change": "薛简保留岑照涉嫌路线外泄的判断，但同意镜阵安全必须优先处理。",
        "source_evidence": "薛简合上调用簿：“主镜封签未破，提前调用记录仍在。座次线索虽已削弱，现有证据也不能排除岑照借试场放出纹路的可能。我不撤销判断。”\n\n岑照道：“残痕只能证明先后。今日能证明的是主镜与节点错层，不是传播动机。”\n\n“这句我记。”薛简看了一眼已经熄黑的第一节点，“泄露路线另查。但镜阵安全必须先修。”"
      },
      {
        "change": "薛简公开撤回并更正此前对岑照可能主动泄露试炼路线的判断。",
        "source_evidence": "“我此前依据副镜封签缺失、丙五座位置、岑照提前调用记录，判断岑照可能主动泄露第一层安全路线。该判断有记录依据，但现有镜屑、残痕先后、封签时间与反光角度已组成新的可复核链条。”\n\n他声音清楚，没有含混。\n\n“现有证据不支持岑照主动泄露试炼路线。此前判断，撤回更正。”"
      },
      {
        "change": "安苇将阮青、唐桥、岑照的责任拆分记录，明确岑照主动泄露嫌疑更正不抵消两项程序违规。",
        "source_evidence": "“正该分开。”安苇展开考功堂责任册，逐条念道，“阮青，留置未封校准副镜于候场廊，未及时归架，未补做封纹，记维护责任。”\n\n阮青垂首领记。\n\n“唐桥，将副镜反光形成的第一层安全纹路绘为运气图并传播。该图只能解释开场避障相似，不能作为正式考题证据，更不能证明其可通过后续心境关。记传播风险。”\n\n唐桥看了一眼自己的图：“那它还叫运气图吗？”\n\n“封样名称不按你的愿望写。”\n\n“明白。”\n\n安苇最后看向岑照：“漏做候场副镜第二道封镜检查，记程序违规。无正式监考复核，提前启动低限试场，另记程序违规。主动泄露嫌疑更正，不抵消这两项。”"
      },
      {
        "change": "薛简继续作为正式监考复核岑照的操作意见，岑照只能在其复述确认下协助重开。",
        "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
      },
      {
        "change": "薛简成为岑照后续调镜操作前必须找的正式监考复核人之一。",
        "source_evidence": "薛简合上调用册：“下次调镜，先找我签字。”"
      }
    ],
    "cultivation_changes": [
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照的左眼镜灼复发，出现刺痛、重影、神识刺痛和距离误判，并导致他不能保证下一次不误触阵枢。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇问：“旧伤？”\n\n“左眼镜灼。”\n\n“方才发生距离误判？”\n\n“是。”\n\n“能否保证下一次不误触阵枢？”\n\n岑照没有辩解：“不能保证。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照临时监考资格尚未冻结但进入风险复核；结果出来前不得单独操作镜阵，不得独自进入深层幻境；辨残痕须有正式监考在场并记录角度与时长。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇又看向岑照：“你的临时监考资格尚未冻结，但已进入风险复核。在结果出来前，不得单独操作镜阵，不得独自进入深层幻境。需要辨残痕，须由正式监考在场，并记录你所看角度与时长。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "照痕辨序在本次监督使用中再次确认只能判断残痕方向和先后，不能认人、定动机或识别传播者。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“能否认出唐桥的灵力？”\n\n“不能。纸上也没有他的灵力可供比照。照痕辨序只认划痕方向和先后，不认人。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照的左眼镜灼仍处于活动状态，观察主镜残痕时出现刺痛加深、银线重影一分为三和距离误判。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "左眼的刺痛忽然加深，主镜边缘那道银线一分为三。岑照立即收回神识，手掌撑住旁边的木栏，却因重影按空了半掌。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "因镜灼症状未减，安苇禁止岑照追加观察，本次未看完的残痕需留待受控复测。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇记下时长：“不足半刻。镜灼症状未减，不许追加观察。”\n\n岑照缓了两息：“还有一道残痕，方向连向第一处回声节点，没看完。”\n\n“留待受控复测。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照的 left-eye-mirror-burn 加重，症状明确为重影、神识刺痛、距离误判。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "岑照扶住监考台，左眼视野里，薛简分成了两个。一个在收阵盘，一个站在半步之外。神识中的刺痛没有随着幻象消退，反而顺着眼眶一下下往深处扎。\n\n安苇先验过三名考生，又查主镜灵息，最后才走到他面前。\n\n“看我手。”\n\n她伸出两指。\n\n岑照闭上右眼，左眼里却有四根手指，远近各一层。\n\n“四。”他说完，又停了一息，“不，重影。实际是二。”\n\n“距离？”\n\n“半丈。”\n\n安苇的手距他不过两尺。\n\n她收回手：“左眼镜灼加重。重影、神识刺痛、距离误判，三项俱在。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照临时监考资格被冻结；伤势解除前不得独自进入深层幻境校场，后续只能在安苇与薛简监督下提供辨序协助。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "随后，她取过岑照的临时监考牌，在背面压下一道灰印。\n\n“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照 left-eye-mirror-burn 解除前不得独自进入深层幻境校场的限制继续有效。",
        "state_id": "solo-deep-illusion-ban",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "岑照的照痕辨序继续被限制为只报残痕方向和先后，不认人、不定动机，并由正式监考复述确认。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇又看向岑照：“你只做受限照痕辨序。只报方向、先后，不认人，不定动机。左眼若再出重影，立刻停。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "岑照修复期间只能在薛简读记录、复述确认后辨低亮残痕，并且只报方向与先后。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照的左眼镜灼仍活动，重影和距离误判仍在。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“停了高亮后，刺痛缓了。重影还在，距离仍会错。”\n\n“记为短暂缓和，不是解除。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "recovery",
        "change": "因停用高亮镜纹，岑照的左眼镜灼出现短暂缓和，刺痛减轻，但未解除。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“停了高亮后，刺痛缓了。重影还在，距离仍会错。”\n\n“记为短暂缓和，不是解除。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照不得触碰阵枢、不得单独下令、不得进入深层幻境，临时监考资格冻结下的监督限制继续有效。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照不得进入深层幻境的限制继续有效。",
        "state_id": "solo-deep-illusion-ban",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "岑照在低亮连测中继续只能辨认残痕方向与先后，证明范围被正式限定为方向与先后，不证明成因、行为人或动机。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“记。”安苇道，“照痕辨序的证明范围，仅限方向与先后。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照的左眼镜灼未加重但仍存在重影，不能增加观察强度。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "淡青镜纹随即熄灭。岑照左眼的刺痛没有加深，重影却仍停了片刻才散。他退到白线外，没有碰阵枢，也没有要求增加亮度。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照临时监考资格冻结与监督限制继续有效，仍不得触碰阵枢、不得进入深层幻境，只能报方向、先后和角度。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照不得进入深层幻境的限制继续有效。",
        "state_id": "solo-deep-illusion-ban",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照左眼镜灼仍活动，表现为重影与距离误判风险；本章低亮连测后出现疲乏，但未确认加重或解除。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "岑照站在阵枢线外，袖口压着手背。他左眼仍有薄薄重影，看台上铜尺时，尺尾总像多出一寸。他没有靠近，只把视线落在低亮镜纹的暗边。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照在三点连测中左眼疲乏，扣影漂移，仍需避免依赖距离判断。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "主镜低亮起，第一节点随之回声。第二节点刚补过砂，光色比第一节点厚半分。岑照左眼一疲，第一节点的扣影像漂到第二节点旁边。他停了一息。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "岑照继续将照痕辨序限定为听取低亮刻度后只报方向与先后，不报距离或推断。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“停看高亮。”岑照道，“请薛师兄读低亮刻度。只读灰痕起止，不读推断。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照临时监考资格冻结与不得触碰阵枢限制继续有效，连测时站在阵枢线外并有红封纸标识。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "连测廊的灯全部压到低亮，只剩主镜、第一节点、第二节点三处暗纹相接。岑照站在阵枢线外三步，脚尖前有薛简亲手贴的红封纸，写着“冻结资格，不得触枢”。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "岑照在监督下继续将照痕辨序限定为低亮残痕的方向与先后，薛简只采信方向与先后，不采信动机判断或程序免责。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“残痕先从候场副镜反射方向入回声链。”岑照改口更短，“再入第三节点。再折主镜。三处节点先后可连。”\n\n安苇看向薛简：“采信范围？”\n\n薛简沉默片刻，道：“采信为方向与先后。不能证明谁有意传播，也不能排除岑照提前调用试场的程序问题。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "injury",
        "change": "岑照左眼镜灼仍未解除，连续低亮观测后出现酸胀、短暂重影，高亮镜纹继续停用，需取镜屑后再安排低强度观想确认伤势流程。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "岑照左眼的酸胀还没退，眼前桌角短短分出两道影。他伸手按了按冷玉纱，却没有再看镜面。\n\n安苇注意到他的动作：“今日到此。高亮镜纹继续停用。取镜屑后，再安排低强度观想，届时我确认伤势流程。现在未解除。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照临时监考资格冻结继续有效，仍不得触阵枢、不得下令调镜，只能在薛简复述后由阮青执行。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "薛简立在阵枢边，手按记录简：“岑照，不得触阵枢，不得下令调镜，只报方向、先后。由我复述，阮青执行。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "岑照的照痕辨序继续被限定为只报低亮残痕方向、先后和角度，且须由薛简复述确认，不得触镜或下令调镜。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "薛简立在封线内，持角度尺复述：“阮青拆罩，以封纹针取物。岑照在封线外，只报方向、先后、角度。不得触镜，不得下令调镜。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "recovery",
        "change": "左眼镜灼进入正式处理流程：镜屑已经取出，但高亮镜纹继续停用，下一步需用清神符稳定回声并做低强度观想，由安苇确认是否解除；本章未痊愈。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "岑照退开两步，左眼重影仍在，并未随镜阵稳定而消失。\n\n安苇收起校准册：“高亮镜纹继续停用。镜屑已经取出，下一步用清神符稳定回声，再做低强度观想。由我确认左眼镜灼是否解除。”\n\n“不是今日？”岑照问。\n\n“今日只到取屑与停亮。伤势不因证据齐了便痊愈。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照临时监考资格暂不恢复，需等伤势流程与重开复核完成后再裁定。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“临时监考资格暂不恢复。伤势流程与重开复核完成后再裁定。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照仍不得触阵枢，不得独自进入深层幻境。",
        "state_id": "solo-deep-illusion-ban",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“明日先验候场分区、携物与封纹，再开随机幻境。岑照，你仍不得触阵枢，不得独自入深层幻境。带上清神符。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "recovery",
        "change": "岑照完成左眼镜灼解除流程，安苇确认残留镜屑已取出、高亮镜纹持续停用、清神符已稳定回声、低强度观想完成，且无重影、无神识刺痛加剧、无距离误判。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "第三轮结束，清神符已化作一小撮灰白符烬。安苇先验左眼灵光，再查神识回声，最后翻到镜屑封样与高亮镜纹停用记录。\n\n“残留镜屑已取出，高亮镜纹持续停用，清神符已稳定回声，低强度观想完成。无重影，无神识刺痛加剧，无距离误判。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "recovery",
        "change": "岑照的 left-eye-mirror-burn 在突破前按流程正式解除，解除与突破无关。",
        "state_id": "left-eye-mirror-burn",
        "state_action": "resolve",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "她在伤势栏落印。\n\n“left-eye-mirror-burn，左眼镜灼，现于突破前按流程正式解除。解除与突破无关。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照伤势解除后仍未恢复独立监考资格，只能在正式监考复核下协助重开，仍不得独自进入深层幻境、触阵枢或单独下令调镜。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照不得独自进入深层幻境、不得触阵枢的限制继续有效，并明确包含不得单独下令调镜。",
        "state_id": "solo-deep-illusion-ban",
        "state_action": "set",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "progress",
        "change": "岑照在随机幻境中启动炼气四层到炼气五层的突破流程，但尚未完成突破，境界仍为炼气四层。",
        "state_id": "",
        "state_action": "",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "随机幻境又一次变化，考生脚下的石阶忽然倒悬。镜中回声随之翻转，岑照的神识回路被猛地拉成一线。两枚灵石迅速黯下去，灵力冲入四层瓶颈，却没有将它撞开，只在临界处不断回荡。\n\n安苇抬眼：“突破已启动，尚未完成。守住完整回路。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "progress",
        "change": "岑照在突破启动时维持主镜与第一节点这一处回声节点，不牵第二、第三节点。",
        "state_id": "",
        "state_action": "",
        "stage_after": "炼气四层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "岑照的回声小周天骤然收紧。主镜的声音如潮涌来，第一节点则在潮后折返。他只维持这一处节点，不去牵第二、第三节点，也不越过浅层监看位。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "breakthrough",
        "change": "岑照在随机幻境中完成完整神识回路运转，正式从炼气四层突破至炼气五层。",
        "state_id": "",
        "state_action": "",
        "stage_after": "炼气五层",
        "from_stage": "炼气四层",
        "to_stage": "炼气五层",
        "prerequisites": [
          "完成三处回声节点校准",
          "旧伤在突破前按规则正式解除",
          "在随机幻境中维持完整神识回路"
        ],
        "costs": [
          "2 枚下品灵石",
          "1 张清神符",
          "突破后回声分裂限制"
        ],
        "new_limits": [
          {
            "state_id": "post-breakthrough-echo-splitting",
            "description": "突破后回声分裂，症状为双重回声、深层定位延迟，暂停高强度监考。"
          },
          {
            "state_id": "solo-deep-illusion-ban",
            "description": "三日内不得独自进入深层幻境。"
          },
          {
            "state_id": "temporary-proctor-risk-review",
            "description": "所有镜阵操作须经正式监考复核，每日仅可进行低强度节点复核。"
          }
        ],
        "source_evidence": "瓶颈没有碎响，只有一瞬极静。\n\n紧接着，完整的神识回路穿过主镜，抵达第一节点，再循原路返回。原本需要逐段辨认的残痕同时浮在两处：主镜纹路先转，节点残痕后应，方向与先后清晰分开。\n\n炼气五层。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "ability",
        "change": "岑照的照痕辨序提升为可同时分辨主镜与第一节点的残痕。",
        "state_id": "residual-mark-reading",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "岑照额角渗出冷汗。他能同时分辨主镜与第一节点的残痕了，却听见两重回声，连神识落点也比念头慢了半拍。"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照新增突破后回声分裂活动限制，表现为双重回声、深层定位延迟，并暂停高强度监考。",
        "state_id": "post-breakthrough-echo-splitting",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "安苇在监督册上记下：“岑照，炼气五层。突破后回声分裂。症状：双重回声、深层定位延迟。暂停高强度监考。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照三日内不得独自进入深层幻境的限制继续有效，并被写入临时监考牌附加条件。",
        "state_id": "solo-deep-illusion-ban",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
      },
      {
        "subject_id": "cen-zhao",
        "kind": "restriction",
        "change": "岑照的临时监考操作限制更新为所有镜阵操作须经正式监考复核，候场反光物检查也须由正式监考复核，每日仅可进行低强度节点复核。",
        "state_id": "temporary-proctor-risk-review",
        "state_action": "set",
        "stage_after": "炼气五层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
      }
    ],
    "resource_changes": [
      {
        "owner_id": "exam-hall",
        "resource_id": "exam-hall-reset-seal",
        "operation": "consume",
        "amount": 1,
        "unit": "枚",
        "resulting_balance": 1,
        "source_or_destination": "低限试场错层后的全场重置",
        "change": "考场启用并永久消耗 1 枚全场重置印，余额从 2 枚降为 1 枚，不返还。",
        "source_evidence": "临时复核桌被搬到熄灭的主镜旁。安苇当场展开资源簿，在重置印一栏写下：原有二枚，启用一枚，余一枚。用途为低限试场错层后的全场重置，不返还。"
      },
      {
        "owner_id": "exam-hall",
        "resource_id": "mirror-sand",
        "operation": "consume",
        "amount": 1,
        "unit": "份",
        "resulting_balance": 5,
        "source_or_destination": "主镜裂纹封补",
        "change": "考场镜砂消耗一份用于主镜裂纹封补，余额由六份减至五份。",
        "source_evidence": "安苇提笔登记：“镜砂一份，去向：主镜裂纹封补。考场镜砂由六份减至五份。主镜仅完成一处封补，不视为全阵修复。”"
      },
      {
        "owner_id": "exam-hall",
        "resource_id": "mirror-sand",
        "operation": "consume",
        "amount": 1,
        "unit": "份",
        "resulting_balance": 4,
        "source_or_destination": "第二回声节点补砂修复",
        "change": "第二回声节点补砂消耗考场镜砂 1 份，余额由 5 份降为 4 份。",
        "source_evidence": "阮青取出一小瓶镜砂，倒入量槽。细砂泛起冷白光，正好一格。薛简验过瓶封，报：“消耗镜砂一份。考场镜砂余额五份降为四份。”"
      },
      {
        "owner_id": "exam-hall",
        "resource_id": "mirror-sand",
        "operation": "consume",
        "amount": 1,
        "unit": "份",
        "resulting_balance": 3,
        "source_or_destination": "补第三节点低亮裂缝",
        "change": "考场镜砂消耗一份用于补第三节点低亮裂缝，余额从四份降为三份。",
        "source_evidence": "“一份。”阮青低声道，“补第三节点低亮裂缝。考场镜砂原余四份，用后一三——”\n\n薛简抬眼。\n\n阮青咬字：“余三份。”"
      },
      {
        "owner_id": "exam-hall",
        "resource_id": "mirror-sand",
        "operation": "consume",
        "amount": 1,
        "unit": "份",
        "resulting_balance": 2,
        "source_or_destination": "副镜封纹",
        "change": "阮青使用一份镜砂补完副镜封纹，考场镜砂余额从三份降为两份。",
        "source_evidence": "阮青从资源匣中取出一份镜砂。安苇当面划去清单上的一格：“副镜封纹，耗镜砂一份。余额两份。”\n\n镜砂调成银灰色细浆，沿副镜封纹槽缓缓铺开。阮青这次没再说“暂放”，每补一寸，便报一寸刻度。"
      },
      {
        "owner_id": "cen-zhao",
        "resource_id": "low-grade-spirit-stone",
        "operation": "consume",
        "amount": 2,
        "unit": "枚",
        "resulting_balance": 2,
        "source_or_destination": "炼气四层到炼气五层突破起始供能槽",
        "change": "岑照消耗2枚下品灵石用于突破起始，余额由4枚降为2枚且不得返还。",
        "source_evidence": "岑照取出两枚下品灵石，放进浅层回环边界的两处供能槽。方才使用的清神符虽已化烬，其清明余力仍留在神识回路中，依规并入此次突破成本，不再另耗一张。\n\n安苇落笔：“下品灵石四减二，余二枚。清神符三减一，余二张。用途：稳定旧伤回声并承接突破起始。不得返还。”"
      },
      {
        "owner_id": "cen-zhao",
        "resource_id": "clarity-talisman",
        "operation": "consume",
        "amount": 1,
        "unit": "张",
        "resulting_balance": 2,
        "source_or_destination": "稳定旧伤回声并承接突破起始",
        "change": "岑照消耗1张清神符用于稳定旧伤回声并并入突破成本，余额由3张降为2张且不得返还。",
        "source_evidence": "岑照取出两枚下品灵石，放进浅层回环边界的两处供能槽。方才使用的清神符虽已化烬，其清明余力仍留在神识回路中，依规并入此次突破成本，不再另耗一张。\n\n安苇落笔：“下品灵石四减二，余二枚。清神符三减一，余二张。用途：稳定旧伤回声并承接突破起始。不得返还。”"
      }
    ],
    "knowledge_changes": [
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "believes_false",
        "belief": "薛简依据岑照提前启阵且无正式监考复核、唐桥等同乡关系、主镜封签未破以及相似路线图出现在候场考生手里，判断岑照涉嫌向同乡考生泄露第一层路线。",
        "supersedes_fact_ids": [],
        "change": "薛简公开提出岑照涉嫌向同乡考生泄露第一层路线的判断。",
        "source_evidence": "“流程要求先核名册，再由正式监考复签。你提前启阵，没有复核签；随后与安全路线相似的图出现在候场考生手里。主镜封签未破，外人无法直接接触阵图。依现有记录，我有理由判断，你涉嫌向同乡考生泄露第一层路线。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "investigating",
        "belief": "岑照认为调用记录只能证明自己启过阵，不能证明路线从自己这里出去；主镜、节点和廊下器物留下的残痕方向与先后可用于追查路线来源。",
        "supersedes_fact_ids": [],
        "change": "岑照提出应查主镜、节点和廊下器物残痕的方向与先后。",
        "source_evidence": "岑照没有看考生，只看调用册：“记录能证明我启过阵，不能证明路线从我这里出去。先查残痕。灵力经过主镜、节点和廊下器物，方向与先后会留下。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "investigating",
        "belief": "安苇认定岑照临时监考资格尚未冻结但已进入风险复核，后续不得单独操作镜阵或独自进入深层幻境，辨残痕必须由正式监考在场并记录角度与时长。",
        "supersedes_fact_ids": [],
        "change": "安苇明确岑照临时监考资格进入风险复核。",
        "source_evidence": "安苇又看向岑照：“你的临时监考资格尚未冻结，但已进入风险复核。在结果出来前，不得单独操作镜阵，不得独自进入深层幻境。需要辨残痕，须由正式监考在场，并记录你所看角度与时长。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "conceals",
        "belief": "唐桥承认运气图是照着候场廊下反光所画，并承认同组都看过、邻组有人借去看，但未承认接触正式考题。",
        "supersedes_fact_ids": [],
        "change": "唐桥声称运气图来源于候场廊下反光，并承认图被同组和邻组考生看过。",
        "source_evidence": "“同组的都看过。邻组有人借去，说只看铜钱，不看路线。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "investigating",
        "belief": "安苇确认岑照仍在风险复核中；现有线索不能认定传播者，也不能排除岑照，并且岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动试场，两项已列入程序责任复核清单。",
        "supersedes_fact_ids": [],
        "change": "安苇将岑照两项程序瑕疵正式列入复核清单，并维持对岑照的受限复核安排。",
        "source_evidence": "安苇提笔，字迹一笔一画压在册页上：“岑照漏做候场副镜第二道封镜检查；无正式监考复核，提前启动试场。两项列入程序责任复核清单。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "investigating",
        "belief": "岑照已确认候场副镜反光能形成唐桥运气图的一部分，但镜子只负责反光，唐桥、阮青和岑照各自仍需说明画图、放置副镜和未检查的责任。",
        "supersedes_fact_ids": [],
        "change": "岑照把路线来源调查推进到候场副镜反光、唐桥画出内容、阮青放置副镜和自己漏查并行的方向。",
        "source_evidence": "岑照按着仍在刺痛的左眼：“镜子只负责反光，不负责供词。你负责把看见的画出去，阮青负责解释它为何在这里，我负责解释为何没查。”"
      },
      {
        "character_id": "ruan-qing",
        "fact_id": "unsealed-calibration-mirror",
        "state": "conceals",
        "belief": "阮青已承认校准副镜开考前辰时二刻左右暂放候场廊，但仍回避何时封存以及为何没有上报。",
        "supersedes_fact_ids": [],
        "change": "阮青不再完全隐瞒副镜暂放候场廊的事实，但仍隐瞒或回避未封存、未上报的具体责任与动机。",
        "source_evidence": "安苇转向阮青：“副镜为何未封？”\n\n阮青低声道：“开考催得急。主镜校准差一轮，我要回去补纹，便先放在这里。”\n\n“为何没有上报？”\n\n“我以为只是暂时——”\n\n“暂时的结束时刻。”\n\n阮青沉默。"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "knows",
        "belief": "唐桥知道自己运气图前三折来自候场廊副镜反光，后一笔是自己觉得不够吉利而添上，但仍未承认知道它对应正式试炼路线。",
        "supersedes_fact_ids": [
          "lucky-route-sketch-source"
        ],
        "change": "唐桥从隐瞒运气图来源变为当场承认所画前三折来自副镜反光，旧的隐瞒状态被淘汰。",
        "source_evidence": "唐桥盯着纸面，神色难得认真：“我画的就是这三折。后面那一笔，是我觉得三折不够吉利，添的。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "suspects",
        "belief": "薛简已下调同乡证据权重，但仍依据主镜封签未破、提前调用、图中路线相似和提前试场可能造成纹路外泄，怀疑岑照与路线外泄有关。",
        "supersedes_fact_ids": [
          "cen-leaked-exam-route"
        ],
        "change": "薛简不再坚持单纯同乡泄露链条成立，转为维持对岑照提前试场放出纹路可能性的嫌疑，旧的错误判断被同一事实更新替代。",
        "source_evidence": "薛简重新封住副镜：“现有线索削弱了同乡泄露这一条，却没有排除岑照借提前试场放出纹路的可能。主镜封签未破，调用记录仍成立。判断暂不更改。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "investigating",
        "belief": "安苇确认岑照误判第一节点距离、left-eye-mirror-burn 加重，并冻结其临时监考资格；岑照漏做副镜第二道封镜检查和无正式监考复核提前启动试场仍在记录中，今日重置不覆盖旧责。",
        "supersedes_fact_ids": [],
        "change": "安苇将岑照资格复核从风险复核推进为资格冻结，并维持既有程序责任记录。",
        "source_evidence": "岑照按住仍在发痛的左眼：“我误判第一节点距离，记我。”\n\n“已记。”安苇道，“你漏做副镜第二道封镜检查，无正式监考复核提前启动试场，也仍在记录中。今日重置不覆盖旧责。”"
      },
      {
        "character_id": "ruan-qing",
        "fact_id": "unsealed-calibration-mirror",
        "state": "conceals",
        "belief": "阮青承认校准副镜由自己搬动，但对副镜移入候场廊是在辰时二刻前还是下签之后说法矛盾，仍未给出可核对的完整说明。",
        "supersedes_fact_ids": [],
        "change": "阮青对副镜移位时间的回避从未封存、未上报扩展为具体时间前后矛盾。",
        "source_evidence": "“辰时二刻前后。”\n\n“前，还是后？”\n\n阮青攥紧量绳：“应当是前。”\n\n薛简翻开维护簿：“辰时二刻，你在第一节点下签，记录为清理回声槽。副镜若在此前移走，是谁搬的？”\n\n“我搬的。也可能……下签之后才搬。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "suspects",
        "belief": "薛简仍依据主镜封签未破、提前调用记录和现有证据，怀疑岑照借试场放出纹路；但承认泄露路线另查，镜阵安全必须先修。",
        "supersedes_fact_ids": [],
        "change": "薛简未撤销对岑照泄露路线的怀疑，只调整处理优先级为先修镜阵安全。",
        "source_evidence": "薛简合上调用簿：“主镜封签未破，提前调用记录仍在。座次线索虽已削弱，现有证据也不能排除岑照借试场放出纹路的可能。我不撤销判断。”\n\n岑照道：“残痕只能证明先后。今日能证明的是主镜与节点错层，不是传播动机。”\n\n“这句我记。”薛简看了一眼已经熄黑的第一节点，“泄露路线另查。但镜阵安全必须先修。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "investigating",
        "belief": "岑照认为今日能证明的是主镜与节点错层，残痕只能证明先后，不能证明传播动机。",
        "supersedes_fact_ids": [],
        "change": "岑照将本章复测结论明确限定为镜阵错层事实，未把残痕解释为传播动机证据。",
        "source_evidence": "岑照道：“残痕只能证明先后。今日能证明的是主镜与节点错层，不是传播动机。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "investigating",
        "belief": "唐桥试图以错层解释运气图路线，但被安苇要求改写为物件来源、所见角度、作图时刻，其余不收。",
        "supersedes_fact_ids": [],
        "change": "唐桥的运气图来源仍未被确认，只被要求补充可核对信息。",
        "source_evidence": "唐桥把封存中的运气图申诉又递了上来，纸角新添了一行字：错层既生，图路或为天意所示。\n\n安苇划掉“天意”二字：“改写物件来源、所见角度、作图时刻。其余不收。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "investigating",
        "belief": "安苇记录主镜错层起点不在考生入场方向，该事实只削弱主动泄露路线的部分推断，不能排除岑照的调用责任、漏封责任及传播嫌疑；岑照资格冻结和受监督限制仍继续。",
        "supersedes_fact_ids": [],
        "change": "安苇将错层起点不在入场方向及其有限影响写入记录，同时保留岑照程序责任与传播嫌疑。",
        "source_evidence": "安苇提笔，把两人的话拆成两行：“事实：错层起点不在考生入场方向。影响：削弱主动泄露路线的部分推断。不能据此排除岑照的调用责任、漏封责任及传播嫌疑。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "investigating",
        "belief": "岑照知道残痕只能证明灵力运行方向和先后，不能证明谁传图或人的动机；本章残痕只能削弱主动泄题推断。",
        "supersedes_fact_ids": [],
        "change": "岑照再次限定照痕辨序的证明范围，不将残痕当作洗清嫌疑的证据。",
        "source_evidence": "“不能。”岑照答得很快，“残痕只记灵力怎么走、何时走。不记谁想做什么，也不认是谁把图传出去。”\n\n“那只能说明，我原先以为错层由入场路线触发，这一项不成立。”\n\n“只能削弱那一段推断。”"
      },
      {
        "character_id": "ruan-qing",
        "fact_id": "unsealed-calibration-mirror",
        "state": "conceals",
        "belief": "阮青知道校准副镜在开考封存点前已移出维护架，并承认自己为赶开考时间将副镜实际留在候场廊而未按时归架封存。",
        "supersedes_fact_ids": [
          "unsealed-calibration-mirror"
        ],
        "change": "阮青关于副镜移位的矛盾说法被维护架记录固定为辰时一刻移出、早于辰时二刻封存点，并承认曾将副镜留在候场廊。",
        "source_evidence": "薛简抽走记录，先看架号，再看出入刻印：“副镜于辰时一刻移出维护架。开考封存点是辰时二刻。你昨日先说封存后才移，后来又说记不清。”\n\n阮青盯着桌面：“我原本要清完镜边就送回去。”\n\n安苇问：“送回哪里？”\n\n“维护架。”\n\n“实际放在哪里？”\n\n“候场廊。”\n\n“为何？”\n\n阮青沉默片刻：“开考时间快到了。主镜还缺一轮校准，我想着副镜只是暂放，等主镜亮稳再封。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "investigating",
        "belief": "唐桥仍试图把修复步骤理解并记录成可避开错层的“新版避坑谱”，其运气图和新增修复笔记被作为传播风险一并封存。",
        "supersedes_fact_ids": [],
        "change": "唐桥新增抄录修复步骤的笔记被发现并封存，扩大了其笔记和候场物件来源链的调查范围。",
        "source_evidence": "唐桥抱着一本窄册，正伏在膝上奋笔疾书。安苇走过去时，他刚写完一行大字——《新版避坑谱》。\n\n下面列着：主镜先补背纹，第一节点三转，低亮时看暗线。"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "suspects",
        "belief": "薛简确认主镜错层最早扰动来自回声节点方向，不是考生入场方向；这使其关于错层由入场路线触发的一项推断不成立，但现有证据仍不足以撤销对岑照的判断。",
        "supersedes_fact_ids": [],
        "change": "薛简把错层起点从考生入场方向修正为回声节点方向，但未撤销对岑照泄露路线的怀疑。",
        "source_evidence": "薛简将维护架记录压在调用簿旁：“镜阵错层查残痕先后，副镜移位查封签时间。两项并行。现有证据仍不足以撤销对岑照的判断，也不足以把两项混作一项。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "side-mirror-time-record",
        "state": "investigating",
        "belief": "薛简掌握维护架记录显示副镜移出维护架早于开考封存点，并将此项与封签时间、阵法调用记录并行核验。",
        "supersedes_fact_ids": [],
        "change": "薛简将副镜移位时间固定为可核验记录项，纳入与封签时间、调用记录的并行核验。",
        "source_evidence": "薛简将“只是暂放”四字原样写入记录：“副镜移出维护架早于开考封存点，且未按时归架封存。此项与封签时间、阵法调用记录并行核验。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "investigating",
        "belief": "岑照知道残痕和反光复原只能说明位置、折法、角度及相近安全纹路，不能证明唐桥动机、唐桥见过后续考题或岑照自身无责。",
        "supersedes_fact_ids": [],
        "change": "岑照再次限定照痕与反光证据的证明范围。",
        "source_evidence": "岑照盯着纸上渐淡的光：“只能说明这个位置、折法和角度，能映出相近的第一层安全纹路。不能说明唐桥为何画，也不能说明他见过后续考题。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "investigating",
        "belief": "唐桥承认自己使用同样宽、折三折的反光纸尺寸给运气图当格尺；该说法被纳入传播风险调查。",
        "supersedes_fact_ids": [],
        "change": "唐桥的运气图来源调查新增同尺寸折纸作格尺的说法。",
        "source_evidence": "唐桥沉默片刻：“给运气图当格尺。”\n\n薛简翻开封存的草图：“格尺？”\n\n“同样宽的纸，折三折，画出来的路才齐整。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "suspects",
        "belief": "薛简仍未撤销对岑照主动泄露路线的嫌疑，并认为主镜封签、提前调用与漏封检查仍在记录中。",
        "supersedes_fact_ids": [],
        "change": "候场反光证据出现后，薛简明确不据此撤销岑照主动泄露路线嫌疑。",
        "source_evidence": "薛简收起草图：“也不能据此撤销你主动泄露路线的嫌疑。主镜封签、提前调用与漏封检查仍在记录中。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "side-mirror-time-record",
        "state": "investigating",
        "belief": "薛简掌握副镜辰时一刻移出、辰时二刻为开考封存点，并认为丙五座书箱、三折反光纸和镜面角度可复原，阮青所谓暂放已跨过封存时限。",
        "supersedes_fact_ids": [],
        "change": "薛简将副镜暂放问题进一步压实为跨过封存时限的程序缺口，并与反光复原证据关联。",
        "source_evidence": "薛简翻到维护架记录：“辰时一刻移出。辰时二刻为开考封存点。现在又有丙五座书箱、三折反光纸和镜面角度可以复原。你所说的‘一阵’，已经跨过封存时限。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "investigating",
        "belief": "安苇继续冻结岑照资格并限制其连测时间与报告范围；同时要求第二节点三点低亮连测、调用记录核查和阮青说明副镜经手与是否使用镜砂或临时封纹。",
        "supersedes_fact_ids": [],
        "change": "安苇维持岑照资格冻结并布置下一步核查。",
        "source_evidence": "安苇合上册子：“次日修第二回声节点。主镜、第一节点、第二节点做三点低亮连测。薛简，调辰时一刻到辰时三刻的调用记录。阮青，说明副镜离架后由谁经手，是否用过镜砂或临时封纹。”\n\n她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
      },
      {
        "character_id": "ruan-qing",
        "fact_id": "unsealed-calibration-mirror",
        "state": "conceals",
        "belief": "阮青知道自己所谓副镜只在廊柱旁暂放一阵的说法已被维护架时间、封存点和反光复原证据压实为程序缺口，但完整责任仍需继续核验。",
        "supersedes_fact_ids": [],
        "change": "阮青不再坚持“只是暂放”的辩解。",
        "source_evidence": "阮青望着被封入袋中的第三张纸，终于没再说“只是暂放”。"
      },
      {
        "character_id": "ruan-qing",
        "fact_id": "unsealed-calibration-mirror",
        "state": "knows",
        "belief": "阮青承认第二节点临时封纹所需镜砂曾被优先留给主镜裂纹，导致副镜封纹没有及时补做；她同时否认自己改考题或碰主镜封签。",
        "supersedes_fact_ids": [
          "unsealed-calibration-mirror"
        ],
        "change": "阮青不再只是遮掩副镜暂放问题，而是承认镜砂调配导致副镜封纹未及时补做。",
        "source_evidence": "薛简笔尖一顿：“说清楚。第二节点临时封纹所需镜砂，被你优先留给主镜裂纹，所以副镜封纹没有及时补做？”\n\n阮青低头：“是。我没改考题，也没碰主镜封签。我只是赶修主镜和这里，觉得副镜……暂时不进阵。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "investigating",
        "belief": "安苇将阮青优先调镜砂用于主镜裂纹与第二节点临时封纹、副镜封纹未及时补做记为程序与资源责任；不等同修改正式考题，并继续推进资格与程序核查。",
        "supersedes_fact_ids": [
          "temporary-proctor-qualification"
        ],
        "change": "安苇把资源去向和副镜封纹缺口正式记入程序责任范围，同时明确不等同于修改正式考题。",
        "source_evidence": "“又是暂时。”安苇在封册上落笔，“记资源去向。阮青优先调镜砂用于主镜裂纹与第二节点临时封纹，副镜封纹未及时补做。此项为程序与资源责任，不等同修改正式考题。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "side-mirror-time-record",
        "state": "investigating",
        "belief": "薛简掌握阵法调用记录显示副镜辰时一刻移出维护架，辰时二刻为开考封存点，岑照辰时二刻又三分提前启动低限试场，辰时二刻后部分反光纸位置才登记。",
        "supersedes_fact_ids": [
          "side-mirror-time-record"
        ],
        "change": "薛简将副镜移出、封存点、岑照提前调用和反光纸登记位置形成时间放入同一调用记录链。",
        "source_evidence": "薛简调出阵法调用记录。玉简一层层展开，辰时一刻到辰时三刻的刻线浮在案上。\n\n“辰时一刻，校准副镜移出维护架。”薛简念得很慢，“辰时二刻，开考封存点。辰时二刻又三分，岑照以临时监考牌提前启动低限试场。无正式监考复核。辰时二刻后，候场廊丙五、丁二、戊一位置登记反光纸。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "suspects",
        "belief": "薛简不再把路线相似简单归因于考生入场方向泄题，认为回声方向、候场反光、纸位时间要并列核查；但岑照提前调用试场和漏封副镜检查仍成立，现有证据不足以撤销他的判断。",
        "supersedes_fact_ids": [
          "cen-leaked-exam-route"
        ],
        "change": "薛简的旧认知被部分纠正，但他仍未公开撤销对岑照的判断。",
        "source_evidence": "薛简收起玉简，语气比前几日少了些硬刺，却仍稳：“路线相似不能再简单归因于考生入场方向泄题。回声方向、候场反光、纸位时间都要并列核查。但岑照提前调用试场、漏封副镜检查，记录仍成立。现有证据不足以撤销我的判断。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "investigating",
        "belief": "岑照明确反光图与安全纹路相近不等于考题，反光角度只能见第一层安全纹路，随机变化和心境关不能由折痕替代。",
        "supersedes_fact_ids": [
          "shared-route-origin"
        ],
        "change": "岑照进一步限定反光图证据的证明范围，并否定唐桥以运气图免试或免陷阱的理解。",
        "source_evidence": "唐桥把告知单拿近些：“可反光图前三折与安全纹路相近，这是你们登记过的。”\n\n“相近，不等于考题。”岑照短句往下压，“反光角度只见第一层安全纹路。随机变化不在图上。心境关不按折痕开门。你按图冲，仍会撞幻象。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "knows",
        "belief": "唐桥已经签收告知，知道反光图不能替代随机幻境心境考验，且自己的三折角不作凭据。",
        "supersedes_fact_ids": [
          "lucky-route-sketch-source"
        ],
        "change": "唐桥从继续围绕运气图来源受查，变为已收到反光图不能作为凭据的正式告知。",
        "source_evidence": "唐桥叹气，写下名字，还在旁边画了个小小的三折角。薛简冷冷看他。\n\n唐桥立刻补字：“此角不作凭据。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "suspects",
        "belief": "薛简掌握第三节点残痕显示安全纹路先自候场副镜反射方向入回声链，该证据压缩了原先对岑照主动泄露路线的判断，但不足以撤销；岑照提前调用试场的程序问题仍不排除。",
        "supersedes_fact_ids": [],
        "change": "薛简的旧判断被第三节点残痕进一步压缩，但他未公开撤销对岑照主动泄露路线的判断。",
        "source_evidence": "薛简收起时间线，声音比早晨低了些：“第三节点残痕已写入。它压缩了原先判断，但不足以撤销。明日取屑、连测副镜封纹后再议。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "side-mirror-time-record",
        "state": "investigating",
        "belief": "薛简将副镜辰时一刻移出维护架、辰时二刻应封存、岑照辰时二刻又三分提前调用低限试场、辰时二刻后反光纸位置登记成形、第三节点残痕显示安全纹路先自候场副镜反射方向入回声链纳入同一时间线。",
        "supersedes_fact_ids": [],
        "change": "薛简把副镜移出、封存点、岑照提前调用、反光纸登记时间和第三节点残痕先后排入同一条时间线。",
        "source_evidence": "薛简把时间一条条排开：“辰时一刻，副镜移出维护架。辰时二刻，按规应封存。辰时二刻又三分，岑照提前调用低限试场，无正式监考复核。辰时二刻后，反光纸位置登记成形。第三节点残痕显示，安全纹路先自候场副镜反射方向入回声链。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "investigating",
        "belief": "安苇继续同时记录岑照两项程序责任、阮青未及时归架并未补做副镜封纹的维护责任，以及副镜边缘疑似残留镜屑待取出核验。",
        "supersedes_fact_ids": [],
        "change": "安苇将阮青未及时归架并未补做副镜封纹正式记为维护责任，并将疑似残留镜屑定位封存待核验。",
        "source_evidence": "安苇笔尖一顿：“‘未及时归架并未补做封纹’，记为维护责任。不要换词。”\n\n阮青耳根红了：“是。”\n\n薛简把时间一条条排开：“辰时一刻，副镜移出维护架。辰时二刻，按规应封存。辰时二刻又三分，岑照提前调用低限试场，无正式监考复核。辰时二刻后，反光纸位置登记成形。第三节点残痕显示，安全纹路先自候场副镜反射方向入回声链。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "investigating",
        "belief": "岑照知道反光路径曾成立，残痕只能证明方向和先后，不能证明唐桥动机或传播者，也不能免除自己的两项程序责任。",
        "supersedes_fact_ids": [],
        "change": "岑照进一步限定残痕与反光路径证据的证明范围，并承认两项程序责任不能被洗掉。",
        "source_evidence": "岑照站在封线外，没有靠近副镜。他只看薛简摊开的角度木尺：“反光路径曾成立。残痕能证明方向和先后，不能证明唐桥为何画，也不能证明谁让他画。”\n\n“也不能洗掉你的两项程序责任。”薛简接上。\n\n“不能。”岑照道。"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "knows",
        "belief": "唐桥已被明确告知复原线是证据不是考题，地上画线不可当作自己的避坑路线或前程。",
        "supersedes_fact_ids": [],
        "change": "唐桥因误把复原线当避坑路线而被纠正，知道复原的是证据不是自己的前程。",
        "source_evidence": "唐桥抱着签收牌，小声问：“那若以后地上画了‘不可站’……”\n\n岑照道：“便不可站。”\n\n唐桥思索片刻：“若旁边又画‘复原’？”\n\n安苇把笔放下，看着他。\n\n唐桥立刻退后三步：“弟子明白，复原的是证据，不是弟子的前程。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-leaked-exam-route",
        "state": "knows",
        "belief": "薛简已公开确认现有证据不支持岑照主动泄露试炼路线，并撤回更正此前基于副镜封签缺失、丙五座位置和岑照提前调用记录形成的判断。",
        "supersedes_fact_ids": [
          "cen-leaked-exam-route"
        ],
        "change": "薛简旧有的岑照可能主动泄露路线判断被新的镜屑、残痕先后、封签时间与反光角度证据链纠正。",
        "source_evidence": "“我此前依据副镜封签缺失、丙五座位置、岑照提前调用记录，判断岑照可能主动泄露第一层安全路线。该判断有记录依据，但现有镜屑、残痕先后、封签时间与反光角度已组成新的可复核链条。”\n\n他声音清楚，没有含混。\n\n“现有证据不支持岑照主动泄露试炼路线。此前判断，撤回更正。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "side-mirror-time-record",
        "state": "knows",
        "belief": "薛简掌握辰时一刻副镜移出、辰时二刻应归架未封、辰时二刻又三分岑照无正式监考复核调用低限试场、辰时二刻后反光纸位置登记成形，并知道第三节点残痕与取屑同测证明候场副镜反射路径能够成立。",
        "supersedes_fact_ids": [
          "side-mirror-time-record"
        ],
        "change": "薛简对副镜时间线与反光链条的调查状态完成为已知事实。",
        "source_evidence": "“辰时一刻，阮青将校准副镜移出维护架。辰时二刻，按规应归架封存，未封。”\n\n阮青低声道：“属实。”\n\n“辰时二刻又三分，岑照调用低限试场。调用簿有其灵印，无正式监考复核。”\n\n岑照道：“属实。”\n\n薛简再翻座次册：“丙五座在候场廊第三柱前。该位置与副镜反光线相交。辰时二刻后，反光纸位置登记成形，唐桥所绘路线与第一层安全纹路相似。”\n\n唐桥小声纠正：“原名运气图。”\n\n安苇看他一眼：“现名传播风险材料。”\n\n薛简将镜屑封样放到时间线中央。\n\n“第三节点残痕显示，安全纹路先自候场副镜方向入回声链。今日取屑同测，证明该反射路径在当时能够成立。也就是说，考生路线相似，不必以监考弟子主动传递为唯一解释。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "knows",
        "belief": "安苇确认岑照主动泄露嫌疑已被更正，但岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动低限试场仍是程序违规，临时监考资格暂不恢复。",
        "supersedes_fact_ids": [
          "temporary-proctor-qualification"
        ],
        "change": "安苇对岑照临时监考资格的调查转为明确裁定：暂不恢复，待伤势流程与重开复核完成后再裁定。",
        "source_evidence": "安苇最后看向岑照：“漏做候场副镜第二道封镜检查，记程序违规。无正式监考复核，提前启动低限试场，另记程序违规。主动泄露嫌疑更正，不抵消这两项。”\n\n岑照道：“认。”\n\n“临时监考资格暂不恢复。伤势流程与重开复核完成后再裁定。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "knows",
        "belief": "岑照知道证据链只能证明先副镜、后纸面、再入第三节点的方向和先后，不能证明是谁摆的或为何摆，也不能免除自己的程序责任。",
        "supersedes_fact_ids": [
          "shared-route-origin"
        ],
        "change": "岑照对反光路径证据的认知从调查推进为明确限定证明范围。",
        "source_evidence": "岑照闭了一下发酸的左眼，才道：“先副镜，后纸面，再入第三节点。只见先后，不见是谁摆的，也不见为何摆。”"
      },
      {
        "character_id": "ruan-qing",
        "fact_id": "unsealed-calibration-mirror",
        "state": "knows",
        "belief": "阮青承认辰时一刻将校准副镜移出维护架，辰时二刻按规应归架封存但未封，并领记维护责任。",
        "supersedes_fact_ids": [
          "unsealed-calibration-mirror"
        ],
        "change": "阮青未封校准副镜的维护责任被本人承认并由安苇记录。",
        "source_evidence": "“辰时一刻，阮青将校准副镜移出维护架。辰时二刻，按规应归架封存，未封。”\n\n阮青低声道：“属实。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "knows",
        "belief": "唐桥知道自己绘制并传播的运气图被定性为传播风险材料，不能作为正式考题证据，也不能证明可通过后续心境关。",
        "supersedes_fact_ids": [
          "lucky-route-sketch-source"
        ],
        "change": "唐桥对运气图性质的认知被安苇纠正为传播风险材料。",
        "source_evidence": "“唐桥，将副镜反光形成的第一层安全纹路绘为运气图并传播。该图只能解释开场避障相似，不能作为正式考题证据，更不能证明其可通过后续心境关。记传播风险。”\n\n唐桥看了一眼自己的图：“那它还叫运气图吗？”\n\n“封样名称不按你的愿望写。”\n\n“明白。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "random-heart-test-lucky-route-no-answer",
        "state": "knows",
        "belief": "唐桥知道自己的运气图无法提供随机心境关答案。",
        "supersedes_fact_ids": [],
        "change": "唐桥在随机心境关中发现运气图没有答案，不能帮助他应对心境之问。",
        "source_evidence": "唐桥摸出记熟的运气图，对着河岸比了两次。\n\n“图上这里应当有一道向右的亮纹。”\n\n舟夫问：“你交什么？”\n\n唐桥又看一眼图。\n\n图上没有答案。"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-zhao-assisted-reopen-under-review",
        "state": "knows",
        "belief": "薛简确认岑照只能在正式监考复核下协助随机幻境重开，不能独自进入深层幻境、触阵枢或单独下令调镜。",
        "supersedes_fact_ids": [],
        "change": "薛简明确掌握并执行岑照协助重开的资格边界。",
        "source_evidence": "“伤势解除，不等于资格恢复。你可在正式监考复核下协助随机幻境重开；仍不得独自进入深层幻境，不得触阵枢，不得单独下令调镜。每次操作意见，由我复述确认。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "left-eye-mirror-burn-resolved-before-breakthrough",
        "state": "knows",
        "belief": "安苇确认岑照左眼镜灼已在突破前按流程正式解除，且解除与突破无关。",
        "supersedes_fact_ids": [],
        "change": "安苇完成并记录岑照伤势解除裁定。",
        "source_evidence": "她在伤势栏落印。\n\n“left-eye-mirror-burn，左眼镜灼，现于突破前按流程正式解除。解除与突破无关。”"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-zhao-not-supported-as-route-leaker",
        "state": "knows",
        "belief": "现有证据不支持岑照主动泄露试炼路线，薛简原先关于岑照可能主动泄露路线的判断已更正。",
        "supersedes_fact_ids": [
          "cen-leaked-exam-route"
        ],
        "change": "薛简公开更正岑照主动泄露试炼路线的判断不成立。",
        "source_evidence": "薛简上前一步，声音传过整个复核席。\n\n“我先前依据封签缺口、座次重合与试场调用记录，判断岑照可能主动泄露路线。现有副镜角度、镜屑、残痕先后与封签时间已经构成新证据链。现有证据不支持岑照主动泄露试炼路线。原判断更正。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "cen-zhao-procedure-violations-recorded",
        "state": "knows",
        "belief": "岑照漏做候场副镜第二道封镜检查，并在无正式监考复核时提前启动试场，两项程序违规记过，救场与突破均不抵扣。",
        "supersedes_fact_ids": [],
        "change": "安苇记录岑照两项程序违规并记过。",
        "source_evidence": "他停了一息，又道：“但岑照漏做候场副镜第二道封镜检查，并在无正式监考复核时提前启动试场，记录无误。”\n\n安苇提笔：“两项程序违规，记过。救场与突破均不抵扣。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "ruan-qing-side-mirror-maintenance-liability",
        "state": "knows",
        "belief": "阮青留置未封校准副镜于候场廊，维护责任入档。",
        "supersedes_fact_ids": [],
        "change": "安苇将阮青留置未封校准副镜于候场廊记入维护责任。",
        "source_evidence": "“阮青留置未封校准副镜于候场廊，维护责任入档。唐桥传播由反光形成的运气图草图，作为传播风险事实入档，不作正式考题泄露认定，也不作答题凭据。”"
      },
      {
        "character_id": "an-wei",
        "fact_id": "tang-qiao-reflection-sketch-spread-risk",
        "state": "knows",
        "belief": "唐桥传播由反光形成的运气图草图，该事实作为传播风险入档，不作正式考题泄露认定，也不作答题凭据。",
        "supersedes_fact_ids": [],
        "change": "安苇将唐桥传播反光运气图草图作为传播风险事实入档。",
        "source_evidence": "“阮青留置未封校准副镜于候场廊，维护责任入档。唐桥传播由反光形成的运气图草图，作为传播风险事实入档，不作正式考题泄露认定，也不作答题凭据。”"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "random-heart-test-lucky-route-no-answer",
        "state": "knows",
        "belief": "运气图只押中开场，不包后续，不能作为随机心境关答题依据。",
        "supersedes_fact_ids": [
          "random-heart-test-lucky-route-no-answer"
        ],
        "change": "唐桥确认运气图无法提供随机心境关答案，并申诉将其改记为普通经验但被拒。",
        "source_evidence": "唐桥想了片刻，郑重申诉：“弟子不求把它算答案。能否改记为普通经验？只押中开场，不包后续。”\n\n“不能。”薛简道，“考场没有‘只包开场’的答题依据。”"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "temporary-proctor-conditions-known",
        "state": "knows",
        "belief": "岑照知道自己只取得附加条件下的临时监考牌，所有镜阵操作须经正式监考复核，三日内不得独自进入深层幻境，每日仅可进行低强度节点复核。",
        "supersedes_fact_ids": [],
        "change": "岑照接收并知晓临时监考牌的附加条件。",
        "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”\n\n岑照接牌时，耳中那道迟来的回声又将“低强度节点复核”重复了一遍。"
      }
    ],
    "thread_changes": [
      {
        "change": "第一轮试炼因二十四名考生集体绕开同一路线而中止，并转入依座次退出和封存核查流程。",
        "source_evidence": "“第一轮试炼中止。”他声音不高，却盖住了所有争辩，“所有考生原地闭目，依座次退出。不得交谈，不得交换纸笔，不得毁弃随身物。”"
      },
      {
        "change": "考场异常升级为岑照涉嫌泄露第一层路线的正式核查。",
        "source_evidence": "“流程要求先核名册，再由正式监考复签。你提前启阵，没有复核签；随后与安全路线相似的图出现在候场考生手里。主镜封签未破，外人无法直接接触阵图。依现有记录，我有理由判断，你涉嫌向同乡考生泄露第一层路线。”"
      },
      {
        "change": "岑照申请从座次、封签和调用记录开始核验，再在监督下查看主镜残痕。",
        "source_evidence": "岑照睁开右眼：“我申请从座次、封签和调用记录开始核验，再在监督下查看主镜残痕。”"
      },
      {
        "change": "安苇暂未准许岑照立即动手，要求先把现场封完整。",
        "source_evidence": "“准许提出，不等于准许立即动手。”安苇道，“先把现场封完整。”"
      },
      {
        "change": "调查线从岑照向同乡泄露路线，扩展为座次传播范围、主镜残痕先后、候场副镜反光和程序责任并行。",
        "source_evidence": "安苇把空纸压住：“反光能解释部分图形，不能解释图如何转手，也不能证明你是否知道它对应试炼路线。”"
      },
      {
        "change": "主镜还有一道未看完的残痕连向第一处回声节点，成为下一步低限度试场复测的核心线索。",
        "source_evidence": "他望向封存区内沉暗的主镜。\n\n“先查清楚，回到主镜的那道残痕，为什么还连着第一处回声节点。”"
      },
      {
        "change": "次日将进行低限度试场复测，薛简掌控封签和调用，岑照只能受限辨序，阮青需交代副镜移动准确时间。",
        "source_evidence": "安苇收起复核册：“明日进行低限度试场复测。薛简掌控封签和调用，岑照只做受限辨序。阮青在启阵前交代副镜从维护架移到候场廊的准确时间。”"
      },
      {
        "change": "低限复测确认试场安全纹路与实际陷阱落点错开，推动调查从单纯泄题动机转向主镜与回声节点错层修复。",
        "source_evidence": "主镜亮起时，一条淡青安全纹路从镜底铺出，越过第一道白线，停在第二道白线左侧。\n\n几乎同时，地面浮出一排浅灰石刺。\n\n石刺本应落在安全纹路之外，最前一根却从淡青光带边缘探了出来，正扎在先前三名考生站过的位置。"
      },
      {
        "change": "错层在实测中扩大，岑照因左眼重影误判第一节点距离，导致封线错误并触发全场重置。",
        "source_evidence": "“不对，是三丈半！”岑照抬手指向节点，眼中的两重边界终于短暂合一，“我报近了一丈！”\n\n神识刺痛随即穿入额角。他脚下明明离阵盘尚有半丈，伸手时却碰翻了旁边的记录架。\n\n薛简一把扶住阵盘：“主镜锁不住。第一节点在反卷！”"
      },
      {
        "change": "后续修复方向确定为停用高亮镜纹，改用低亮度分段检查主镜及第一、第二回声节点。",
        "source_evidence": "安苇封好事故簿：“即刻停用高亮镜纹。明日改用低亮度分段检查，先主镜，再第一、第二回声节点。薛简保管封签与调用记录，岑照只报残痕方向和先后。”"
      },
      {
        "change": "修复流程进入低亮分段阶段：先封补主镜一处裂纹，再完成第一回声节点临时校准，后续需主镜与第一节点连测并修第二节点。",
        "source_evidence": "安苇合上记录册：“明日，第一节点与主镜连测，再修第二节点。仍用低亮分段法。”"
      },
      {
        "change": "主镜错层起点被确认不在考生入场方向，只削弱主动泄露路线推断，未洗清岑照嫌疑。",
        "source_evidence": "安苇提笔，把两人的话拆成两行：“事实：错层起点不在考生入场方向。影响：削弱主动泄露路线的部分推断。不能据此排除岑照的调用责任、漏封责任及传播嫌疑。”"
      },
      {
        "change": "副镜移位线索由矛盾口供推进为维护架记录与阮青承认的候场廊暂放事实，需继续与封签时间和调用记录核验。",
        "source_evidence": "薛简将“只是暂放”四字原样写入记录：“副镜移出维护架早于开考封存点，且未按时归架封存。此项与封签时间、阵法调用记录并行核验。”"
      },
      {
        "change": "唐桥新增修复步骤笔记触发考生笔记清点和候场物件再封存。",
        "source_evidence": "她转身点了两名执事：“清点所有考生笔记。运气图、新增修复笔记与候场物件清单一并封存。候场廊的笔、纸、反光器物重新登记，未列册者不得留下。”"
      },
      {
        "change": "候场反光链条成为待核证据，需与副镜移出时间、封签时间、阵法调用记录并列核查；现阶段不作动机认定。",
        "source_evidence": "薛简在新清单末尾落下封签：“候场反光链条成立为待核证据，与副镜移出时间、封签时间、阵法调用记录并列核查。现阶段，不作动机认定。”"
      },
      {
        "change": "阮青暂放副镜的程序问题进一步明确：暂放不等于没有程序问题。",
        "source_evidence": "安苇道：“想归架不等于已经归架。暂放也不等于程序不存在。”"
      },
      {
        "change": "调查焦点推进到第三回声节点、候场副镜、封签时间、调用记录和反光纸位置时间线的串联。",
        "source_evidence": "薛简合上调用记录：“明日第三节点。辰时一刻副镜移出、辰时二刻封存点、岑照提前调用、反光纸位置形成时间，我会放在同一条线上。”"
      },
      {
        "change": "下一步要求阮青带副镜封纹工具与剩余镜砂去向清单，并核查副镜边缘残留物。",
        "source_evidence": "安苇看向阮青：“带副镜封纹工具，带剩余镜砂去向清单。若副镜边缘有残留物，一并核。”"
      },
      {
        "change": "完整试场仍不得重开，因为第三节点未修、副镜未封。",
        "source_evidence": "安苇收起第一叠告知单：“今日到此。第三节点未修，副镜未封，完整试场不得重开。”"
      },
      {
        "change": "副镜边缘疑似镜屑、封签、角度、残痕被安排到明日同测，证据链缺口推进到取屑与副镜封纹连测。",
        "source_evidence": "安苇没有伸手取，只取一枚小封罩扣在副镜边缘：“疑似残留镜屑，定位封存。取出需明日连同封签、角度、残痕同测。今日不取。”"
      },
      {
        "change": "薛简将副镜边缘疑似镜屑纳入同一时间线，同时仍突出岑照提前调用记录，但主动泄露判断的压力减弱。",
        "source_evidence": "薛简把“副镜边缘封纹槽疑似镜屑”写进同一张时间线，又在“岑照提前调用”四字下重重加了一点。那一点落得不轻，却没有像早先那样直接压到“主动泄露”上。"
      },
      {
        "change": "副镜反光证据链完成：镜屑断面、封纹刀旧划、槽内受力痕、反光纸折角与第三节点低亮残痕角度互证，证明第一层安全纹路曾由候场副镜特定角度反射，经纸面入回声链。",
        "source_evidence": "薛简亲自落笔：“镜屑断面、封纹刀旧划、槽内受力痕、反光纸折角及第三节点低亮残痕，角度可互证。第一层安全纹路曾由候场副镜特定角度反射，经纸面入回声链。”"
      },
      {
        "change": "低亮连测完成，第三节点复核扣扣死，问心镜阵主镜与三处回声节点均可复核校准完成。",
        "source_evidence": "这一次，低亮残痕顺着封纹完整归环。第三节点复核扣发出一声清脆轻响，严丝合缝地扣死。\n\n主镜与三处回声节点的低亮回环同时稳定下来。\n\n安苇验过复核扣，又检查副镜封纹，才在校准册上落印：“主镜、第一、第二、第三回声节点，可复核校准完成。候场副镜封纹完成。镜砂余额两份。”"
      },
      {
        "change": "下一场随机幻境重开前的安全检查流程新增反光物签收项，需重开前逐件验角。",
        "source_evidence": "安苇提笔，在候场检查条目末尾添下一行：“考生携入之纸、金属、釉面器物，另设反光物签收项。重开前逐件验角。”"
      },
      {
        "change": "唐桥和涉反光图考生的运气图材料继续保留为传播风险材料，不能提供随机心境关通关答案。",
        "source_evidence": "他身后的两名考生也因重新分组，站不到原来的角度，更找不到所谓反光路线。运气图只能留在封袋里，继续作为传播风险材料，半点不能替他们应对心境之问。"
      },
      {
        "change": "岑照漏做副镜第二道封镜检查和无正式监考复核提前启动试场两项程序责任仍未取消。",
        "source_evidence": "“漏做副镜第二道封镜检查、无正式监考复核提前启动试场，两项记录不变。”"
      },
      {
        "change": "随机幻境重开过程中出现主镜回声迟半息，处理方式是延后一息入场节拍，不调阵枢。",
        "source_evidence": "第三名考生入场时，主镜回声迟了半息。\n\n岑照没有伸手，只道：“主镜回声迟半息，第一节点尚未跟迟。”\n\n薛简复验后下令：“入场节拍延后一息，阵枢不调。”"
      },
      {
        "change": "随机心境关继续按随机变化运行，反光草图只能绕过开场陷阱，不能作为后续通关答案。",
        "source_evidence": "其余涉反光图考生依次出关，有人通过，有人失分，结果全按随机心境关中的实际选择登记。那张草图只帮他们绕过了开场陷阱，遇上变换的山路、雨街与取舍问境，便再没有一笔可照着走。"
      },
      {
        "change": "副镜镜屑、座次、残痕先后、封签时间和镜面角度构成证据链，证明现有证据不支持岑照主动泄露试炼路线。",
        "source_evidence": "“候场副镜边缘镜屑已取出。座次与反光纸位置吻合；残痕先后显示安全纹路先由副镜反射方向进入回声链；封签时间晚于副镜移出；镜面角度可形成第一层安全纹路，但不能显示后续随机心境关。”"
      },
      {
        "change": "突破后薛简接管全部调镜口令，阮青关闭第二节点外沿响应，考场未因岑照突破后的回声分裂而错层。",
        "source_evidence": "薛简接过全部调镜口令：“主镜稳位。第一节点由岑照维持，第二、第三节点归我。阮青，关闭第二节点外沿响应。”\n\n阮青当即落下隔纹扣。\n\n主镜中的雨街轻晃了一下，没有错层。独木桥仍在远处，长街也没有与山路重叠。"
      },
      {
        "change": "资源账目最终确认：考场重置印余额一枚、镜砂余额二份、岑照下品灵石余额二枚、清神符余额二张，所有消耗已定账且不返还。",
        "source_evidence": "“考场重置印原有二枚，已消耗一枚，余额一枚，不返还。镜砂原有六份，修补主镜、三处回声节点及副镜封纹后，余额二份。岑照下品灵石原有四枚，余额二枚；清神符原有三张，余额二张。所有消耗已定账。”"
      }
    ],
    "comedy_changes": [
      {
        "change": "唐桥把“不得触碰左侧雾桥”的安全警示理解为押题提示，推导出左侧必有题眼、安全处在右。",
        "source_evidence": "唐桥谨慎地指向那块警示牌：“不得触碰左侧雾桥。字面上是不许碰，深意自然是左侧必有题眼。既然题眼在左，安全处便在右。如今又叫我们别动，可见动者有失。”"
      },
      {
        "change": "唐桥把考生贴右侧遇险后被监考救回，也解释成右侧是生路。",
        "source_evidence": "这一弹牵动整队。前后六人撞成一串，唐桥被挤得抱住桥柱，仍不忘高声提醒：“看见没有，右侧虽险，却有监考相救，果然是生路！”"
      },
      {
        "change": "有考生抄下警示牌并加注“左侧必有题眼，右行三步”，与二十四人在桥上的动作一致。",
        "source_evidence": "薛简把他的纸也收走。纸上端端正正写着“不得触碰左侧雾桥”，下面另加一行小字：左侧必有题眼，右行三步。\n\n这行小字与二十四人在桥上的动作分毫不差。"
      },
      {
        "change": "唐桥坚持运气图只负责运气不负责作弊，触发岑照要求复原他画图时的站位、朝向和纸面高度。",
        "source_evidence": "唐桥赶紧道：“复核官，那图只负责运气，不负责作弊。”\n\n岑照看了他一眼：“运气站哪儿？”\n\n唐桥一怔：“什么？”\n\n“你画图时站哪儿，脸朝哪边，纸放多高。”"
      },
      {
        "change": "唐桥用“运气”调侃封签空白，被薛简直接压回实测站位。",
        "source_evidence": "唐桥替他看了看空白的封签位：“从运气上说，似乎一直没封。”\n\n薛简道：“你只负责站回东三位。”"
      },
      {
        "change": "岑照把反光线索归纳成“镜子只负责反光，不负责供词”，将荒谬申诉转化为责任分摊。",
        "source_evidence": "岑照按着仍在刺痛的左眼：“镜子只负责反光，不负责供词。你负责把看见的画出去，阮青负责解释它为何在这里，我负责解释为何没查。”"
      },
      {
        "change": "考生将“不得前进三步”的安全指令误解为站位口诀，导致候场线重排和唐桥被排到最后。",
        "source_evidence": "十几名考生齐齐往后退了三步，又有人向左挪半步。唐桥夹在其中，正压低声音指点：“不得前进三步，意思便是前三步有变。第二线后起步，左脚先落，正合我那张图的第二折。”\n\n薛简抬眼：“谁让你们动的？”\n\n唐桥拱手：“安全指令。”\n\n“安全指令是让你们不动。”\n\n“弟子不动之前，先选个稳妥位置。”"
      },
      {
        "change": "唐桥因继续把退三步当成道理，被薛简命令再往后排一丈。",
        "source_evidence": "唐桥远远看了一眼，小声道：“所以退三步确有道理。”\n\n薛简头也不抬：“把他再往后排一丈。”"
      },
      {
        "change": "唐桥把阵法修复步骤命名为《新版避坑谱》，被薛简按规章更正为“未授权修复记录”。",
        "source_evidence": "薛简抽走窄册，按规章念道：“候场考生不得抄录阵法维修步骤、节点位置及监考口令。此纸封存，名称更正为‘未授权修复记录’。”\n\n唐桥争道：“叫避坑谱比较好记。”"
      },
      {
        "change": "安苇因唐桥的笔记“好记”而将其定为传播风险物。",
        "source_evidence": "唐桥争道：“叫避坑谱比较好记。”\n\n安苇把纸折起：“正因为好记，才算传播风险物。”"
      },
      {
        "change": "唐桥把同尺寸折纸解释为运气图格尺，岑照严肃纠正为折痕等距，安苇将其登记为测距用途而非吉相。",
        "source_evidence": "岑照道：“线齐只说明折痕等距。”\n\n“等距也是一种吉相。”\n\n“登记为测距用途。”安苇吩咐执事，“不登记吉相。”"
      },
      {
        "change": "安苇以“哪张纸比较有福气”调侃唐桥的运气说法，同时确认候场廊重排成本。",
        "source_evidence": "候场执事迟疑道：“如此重排，候检至少多半个时辰。”\n\n“记入重排成本。”安苇道，“总好过再用一场考试核验哪张纸比较有福气。”"
      },
      {
        "change": "唐桥把三点连测强行理解为自己的三折运气图得到节点背书，被岑照逐句否定。",
        "source_evidence": "他听见“三点连测”四字，眼睛一亮：“三点？我那运气图正好三折。主镜、第一、第二都接上了，是不是说明前三折得了节点背书？重开时开场陷阱我可按图免过？”\n\n岑照正在按眼角，闻言放下手：“不是。”"
      },
      {
        "change": "唐桥签收告知单时仍试图给三折角留凭据，最终被迫注明此角不作凭据。",
        "source_evidence": "唐桥叹气，写下名字，还在旁边画了个小小的三折角。薛简冷冷看他。\n\n唐桥立刻补字：“此角不作凭据。”"
      },
      {
        "change": "唐桥把取证复原斜线误认为下一轮避坑线并主动站上去，意外触发副镜反光风险。",
        "source_evidence": "唐桥又挪了半步，刚好站到白线交叉处：“弟子只是核对自己没有站错。此处上承副镜，下避红封，左右皆不犯线，看着很顺。”\n\n薛简转头：“唐桥，退回灰绳后。”\n\n唐桥认真道：“若这是复原线，弟子站上去，岂不正好复原当时运气？”\n\n岑照看了他一眼：“你把取证角度当成求签了。”\n\n“不是求签。”唐桥辩解，“是尊重考场线。”\n\n他话音未落，副镜边缘那点暗银碎屑在他所站斜角上轻轻一闪，正把廊柱旁一张空白告知单照出一截浅纹。"
      },
      {
        "change": "唐桥的误站导致候场分区线改为无反光斜角，所有考生改退至廊柱阴面，候场管理流程增加。",
        "source_evidence": "“记录。”安苇道，“唐桥主动移至可再次形成副镜反光的斜角，传播风险增加。候场分区线改为无反光斜角，所有考生退至廊柱阴面。”"
      },
      {
        "change": "唐桥试图把副镜反光解释成考场给勤快人的运气提示，结果反而促成安苇新增反光物签收项。",
        "source_evidence": "唐桥站在廊柱阴面，踮脚看了两眼：“这光倒像它自己认路。”\n\n安苇头也没抬：“退回阴线。”\n\n唐桥老实退了一步，又忍不住道：“弟子只是申明，那日若也是镜子自己照过来，考生看懂了，是否算考场给勤快人的运气提示？”\n\n岑照的目光仍落在低亮尺上。\n\n“反光不是提示。能被带走，就是传播风险。”\n\n“可弟子没有带镜子。”\n\n“你带了纸。”\n\n唐桥低头看向封物匣里那张三折反光纸，没再出声。\n\n安苇提笔，在候场检查条目末尾添下一行：“考生携入之纸、金属、釉面器物，另设反光物签收项。重开前逐件验角。”\n\n唐桥张了张嘴。\n\n他这一番申诉，没替自己减掉半笔，倒替往后的考生多添了一道签收。"
      },
      {
        "change": "唐桥坚持运气图旧名，被安苇当场改称传播风险材料。",
        "source_evidence": "薛简再翻座次册：“丙五座在候场廊第三柱前。该位置与副镜反光线相交。辰时二刻后，反光纸位置登记成形，唐桥所绘路线与第一层安全纹路相似。”\n\n唐桥小声纠正：“原名运气图。”\n\n安苇看他一眼：“现名传播风险材料。”"
      },
      {
        "change": "唐桥把反光物签收项误解为重开考题提示并要求按纸类签收先后排座，反而触发携物复查和座次复核。",
        "source_evidence": "“既然特意写了三类物件，想来这三类之中必有一类与重开后的考题相合。我签收的是纸，应按纸类签收先后排座。若纸为首类，我也不求照顾，只求依规坐前排。”\n\n旁边两名抄过运气图的考生顿时把自己的签收条摸了出来。一人签的是铜扣，一人签的是釉面水囊，三人各执一类，眼看便要从木牌的字序争到座次的吉凶。"
      },
      {
        "change": "岑照用正式监考术语回应荒谬申诉，将唐桥的押题理解转化为实际复查流程。",
        "source_evidence": "岑照隔着封线道：“反射源不明，先复核携物。签收次序不构成考题凭据。”\n\n唐桥认真问：“那木牌为何把纸写在最前？”\n\n“纸最易折成斜角。”\n\n“所以斜角重要？”\n\n“所以你的纸要再查一遍。”"
      },
      {
        "change": "唐桥把签收条当提示，结果该纸条让他多出拆包、验角、调组三道手续。",
        "source_evidence": "唐桥低头看着自己的签收条。那张被他视作重开提示的纸，当场替他添了拆包、验角、调组三道手续。"
      },
      {
        "change": "唐桥试图把运气图改名为普通经验、避坑心得或运势参照，均被薛简按考试记录否定。",
        "source_evidence": "“不能。”薛简道，“考场没有‘只包开场’的答题依据。”\n\n“那叫避坑心得？”\n\n“警示边界不是心得。”\n\n“运势参照？”\n\n“传播草图。”"
      },
      {
        "change": "唐桥的命名申诉反而促成候场反光物检查新增正式监考复核要求。",
        "source_evidence": "唐桥怔了怔：“弟子只是想给图换个名字。”\n\n薛简收走申诉纸：“你给它添了一道检查。”"
      },
      {
        "change": "临时监考牌本身会反光，因此薛简要求岑照未复核前不得拿去候场照字。",
        "source_evidence": "唐桥探头看了一眼：“这牌也会反光。”\n\n薛简立刻将牌按回岑照掌中：“所以收好。未复核前，不得拿去候场照字。”"
      }
    ],
    "new_constraints": [
      {
        "change": "岑照不得再动主镜。",
        "source_evidence": "“所以才停。”薛简看向他，“你不得再动主镜。”"
      },
      {
        "change": "主镜、座次牌、调用册、考生纸片须分别加双签；候场廊内与反光有关的器物须原位封住，任何人不得挪动。",
        "source_evidence": "安苇点头：“先封存，不先定动机。主镜、座次牌、调用册、考生纸片，分别加双签。候场廊内与反光有关的器物原位封住，任何人不得挪动。”"
      },
      {
        "change": "岑照临时监考资格尚未冻结但进入风险复核；结果出来前不得单独操作镜阵，不得独自进入深层幻境；辨残痕须由正式监考在场并记录角度与时长。",
        "source_evidence": "安苇又看向岑照：“你的临时监考资格尚未冻结，但已进入风险复核。在结果出来前，不得单独操作镜阵，不得独自进入深层幻境。需要辨残痕，须由正式监考在场，并记录你所看角度与时长。”"
      },
      {
        "change": "岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动试场，两项进入程序责任复核清单。",
        "source_evidence": "安苇提笔，字迹一笔一画压在册页上：“岑照漏做候场副镜第二道封镜检查；无正式监考复核，提前启动试场。两项列入程序责任复核清单。”"
      },
      {
        "change": "阮青关于校准副镜未上报原因仍待核查。",
        "source_evidence": "安苇在复核册上添了一行：“校准副镜自辰时二刻起留置候场廊，未见封存记录。留置原因已述，未上报原因待核。”"
      },
      {
        "change": "岑照因镜灼症状未减，不许追加观察主镜残痕。",
        "source_evidence": "安苇记下时长：“不足半刻。镜灼症状未减，不许追加观察。”"
      },
      {
        "change": "岑照临时监考资格被冻结，伤势解除前不得独自进入深层幻境校场，后续只可在安苇与薛简监督下提供辨序协助。",
        "source_evidence": "“自此刻起，冻结临时监考资格。伤势解除前，不得独自进入深层幻境校场。后续只可在我与薛简监督下提供辨序协助，每次结论由正式监考复述确认。”"
      },
      {
        "change": "问心镜阵修清错层前禁止再开完整试场。",
        "source_evidence": "“在修清错层之前，谁也不许再开完整试场。”"
      },
      {
        "change": "即刻停用高亮镜纹，下一步改用低亮度分段检查。",
        "source_evidence": "安苇封好事故簿：“即刻停用高亮镜纹。明日改用低亮度分段检查，先主镜，再第一、第二回声节点。薛简保管封签与调用记录，岑照只报残痕方向和先后。”"
      },
      {
        "change": "阮青明日必须带维护架记录，给出副镜移位时刻与主镜校准缺口的可核对说法。",
        "source_evidence": "安苇转向阮青：“副镜移位时刻，明日带维护架记录来。辰时二刻前，还是辰时二刻后，须有可核对的说法。”"
      },
      {
        "change": "修复期间停用高亮镜纹，岑照不得触碰阵枢、不得单独下令、不得进入深层幻境，所有结论需由薛简复述确认。",
        "source_evidence": "安苇将禁用牌扣在阵枢上，声音平直：“修复期间，停用高亮镜纹。岑照不得触碰阵枢，不得单独下令，不得进入深层幻境。薛简先读封签与调用记录，岑照再辨残痕，所有结论由薛简复述确认。”"
      },
      {
        "change": "第一回声节点只是临时校准，必须留复核扣，并与第二、第三节点连测后才能判断全阵状态。",
        "source_evidence": "阮青刚要扣死外环，安苇伸手挡住：“临时校准。先留复核扣。”\n\n薛简补道：“还要与第二、第三节点连测。单点同拍，不等于全阵无错。”"
      },
      {
        "change": "候场考生不得抄录阵法维修步骤、节点位置及监考口令；唐桥笔记被封存为未授权修复记录。",
        "source_evidence": "薛简抽走窄册，按规章念道：“候场考生不得抄录阵法维修步骤、节点位置及监考口令。此纸封存，名称更正为‘未授权修复记录’。”"
      },
      {
        "change": "考生笔记、运气图、新增修复笔记和候场物件清单一并封存，候场廊笔、纸、反光器物重新登记，未列册者不得留下。",
        "source_evidence": "她转身点了两名执事：“清点所有考生笔记。运气图、新增修复笔记与候场物件清单一并封存。候场廊的笔、纸、反光器物重新登记，未列册者不得留下。”"
      },
      {
        "change": "候场廊座次与反光物件重新标注：丙五座与书箱分开两砖，所有座次与廊柱、窗面、铜器至少隔一砖半，笔、纸、墨碟、玉扣及能反光器物另列一册；三张纸全部封存。",
        "source_evidence": "她拿过候场清单，在原座次图上划出三道间距线：“丙五座与书箱分开两砖。所有座次与廊柱、窗面、铜器至少隔一砖半。笔、纸、墨碟、玉扣及能反光的器物另列一册。三张纸登记持有人、原位置、折法与可成角度，全部封存。”"
      },
      {
        "change": "候场廊重排使候检时间至少延长半个时辰，作为重排成本记录。",
        "source_evidence": "候场执事迟疑道：“如此重排，候检至少多半个时辰。”\n\n“记入重排成本。”安苇道，“总好过再用一场考试核验哪张纸比较有福气。”"
      },
      {
        "change": "下一次连测需缩短时间，岑照仍只报方向、先后和角度，资格冻结不变，不得碰阵枢、不得进深层幻境。",
        "source_evidence": "她又看向岑照：“连测时间缩短。你仍只报方向、先后和角度。资格冻结不变，阵枢不许碰，深层幻境不许进。”"
      },
      {
        "change": "三点连测规程限定为低亮、分段，岑照只报方向和先后，薛简复述，阮青补砂，越序即停止连测。",
        "source_evidence": "安苇把封册放在台角：“低亮。分段。岑照只报方向和先后。薛简复述，阮青补砂。谁越过这个次序，今日连测停止。”"
      },
      {
        "change": "第二回声节点复核扣必须等第三节点同线连测后再扣死。",
        "source_evidence": "岑照闭左眼听完：“主镜先，第一次之，第二后接。第一节点可扣复核扣。第二节点需等第三节点同线后再扣死。”"
      },
      {
        "change": "凡见过、抄过、传过反光图者必须签收告知单，不能以反光图要求免试、改座或避查，签完并入重开前检查。",
        "source_evidence": "安苇抬笔：“不评聪明。评风险。凡见过、抄过、传过反光图者，签收此单：反光图不能替代随机幻境心境考验，不得以图纸要求免试、改座、避查。签完并入重开前检查。”"
      },
      {
        "change": "第三节点复核扣不得立刻扣死，需等待候场副镜封纹连测确认。",
        "source_evidence": "岑照立刻收眼：“第三节点本体可连测。复核扣暂缓。副镜方向残痕未清，需与副镜封纹连测。”\n\n薛简照原话写下：“第三节点复核扣暂待候场副镜封纹连测后确认。”"
      },
      {
        "change": "副镜边缘疑似残留镜屑已封存，必须明日连同封签、角度、残痕同测后取出，本章不得取。",
        "source_evidence": "安苇没有伸手取，只取一枚小封罩扣在副镜边缘：“疑似残留镜屑，定位封存。取出需明日连同封签、角度、残痕同测。今日不取。”"
      },
      {
        "change": "候场分区线改为无反光斜角，所有考生退至廊柱阴面，以避免再次形成副镜反光。",
        "source_evidence": "“记录。”安苇道，“唐桥主动移至可再次形成副镜反光的斜角，传播风险增加。候场分区线改为无反光斜角，所有考生退至廊柱阴面。”"
      },
      {
        "change": "岑照必须继续停用高亮镜纹，等取镜屑后再安排低强度观想并由安苇确认伤势流程。",
        "source_evidence": "安苇注意到他的动作：“今日到此。高亮镜纹继续停用。取镜屑后，再安排低强度观想，届时我确认伤势流程。现在未解除。”"
      },
      {
        "change": "重开前新增反光物签收项，考生携入之纸、金属、釉面器物需逐件验角。",
        "source_evidence": "安苇提笔，在候场检查条目末尾添下一行：“考生携入之纸、金属、釉面器物，另设反光物签收项。重开前逐件验角。”"
      },
      {
        "change": "唐桥的运气图只能解释开场避障相似，不能作为正式考题证据，也不能证明其可通过后续心境关。",
        "source_evidence": "“唐桥，将副镜反光形成的第一层安全纹路绘为运气图并传播。该图只能解释开场避障相似，不能作为正式考题证据，更不能证明其可通过后续心境关。记传播风险。”"
      },
      {
        "change": "岑照仍需在下一步使用清神符稳定回声并做低强度观想，由安苇确认左眼镜灼是否解除；今日不痊愈。",
        "source_evidence": "安苇收起校准册：“高亮镜纹继续停用。镜屑已经取出，下一步用清神符稳定回声，再做低强度观想。由我确认左眼镜灼是否解除。”\n\n“不是今日？”岑照问。\n\n“今日只到取屑与停亮。伤势不因证据齐了便痊愈。”"
      },
      {
        "change": "明日重开随机幻境前必须先验候场分区、携物与封纹；岑照仍不得触阵枢，不得独自入深层幻境，需带上清神符。",
        "source_evidence": "“明日先验候场分区、携物与封纹，再开随机幻境。岑照，你仍不得触阵枢，不得独自入深层幻境。带上清神符。”"
      },
      {
        "change": "反光物签收项引发申诉后，所有涉反光图考生必须携物拆包验角、座次与签收条复核，原同组者分开并调入无反光斜角分区后再入场。",
        "source_evidence": "薛简已转向候场执事：“按反射源不明项追加复查。所有涉反光图考生，携物拆包验角，座次与签收条复核。原同组者分开，调入无反光斜角分区后再入场。每次调位记时、记座，不得口头换位。”"
      },
      {
        "change": "岑照突破资源投入后不得返还。",
        "source_evidence": "安苇落笔：“下品灵石四减二，余二枚。清神符三减一，余二张。用途：稳定旧伤回声并承接突破起始。不得返还。”"
      },
      {
        "change": "岑照在突破启动中只可维持主镜与第一节点，不得再增加回声节点。",
        "source_evidence": "薛简盯着复核刻度：“主镜与第一节点，闭合。不得再加。”"
      },
      {
        "change": "岑照突破后暂停高强度监考。",
        "source_evidence": "安苇在监督册上记下：“岑照，炼气五层。突破后回声分裂。症状：双重回声、深层定位延迟。暂停高强度监考。”"
      },
      {
        "change": "突破、救场与已耗资源均不抵扣岑照程序违规，已耗灵石与清神符不返还。",
        "source_evidence": "她抬眼：“已耗灵石与清神符不返还。突破不计修阵，不抵违规。”"
      },
      {
        "change": "候场反光物检查以后须由正式监考复核，不得由临时监考单独确认。",
        "source_evidence": "她又指向唐桥的申诉纸：“把‘只押中开场、不包后续’原句抄入传播风险说明。以后候场反光物检查，须由正式监考复核。不得由临时监考单独确认。”"
      },
      {
        "change": "岑照的临时监考牌附加违规记过保留、所有镜阵操作须经正式监考复核、候场反光物检查须由正式监考复核、三日内不得独自进入深层幻境、每日仅可进行低强度节点复核。",
        "source_evidence": "她递给岑照：“临时监考牌。附加条件：违规记过保留；所有镜阵操作须经正式监考复核；候场反光物检查须由正式监考复核；三日内不得独自进入深层幻境；每日仅可进行低强度节点复核。”"
      },
      {
        "change": "岑照三日后再复核回声分裂，期间不得自行验证。",
        "source_evidence": "安苇看着他：“听见几遍？”\n\n“两遍。”\n\n“三日后再复核。期间不得自行验证。”"
      }
    ],
    "resolved_constraints": [
      {
        "change": "薛简对岑照主动泄露试炼路线的旧怀疑解除并公开更正。",
        "source_evidence": "“我此前依据副镜封签缺失、丙五座位置、岑照提前调用记录，判断岑照可能主动泄露第一层安全路线。该判断有记录依据，但现有镜屑、残痕先后、封签时间与反光角度已组成新的可复核链条。”\n\n他声音清楚，没有含混。\n\n“现有证据不支持岑照主动泄露试炼路线。此前判断，撤回更正。”"
      },
      {
        "change": "第三回声节点复核扣等待副镜封纹连测后确认的状态解除，复核扣已经扣死。",
        "source_evidence": "这一次，低亮残痕顺着封纹完整归环。第三节点复核扣发出一声清脆轻响，严丝合缝地扣死。"
      },
      {
        "change": "岑照 left-eye-mirror-burn 伤势正式解除。",
        "source_evidence": "她在伤势栏落印。\n\n“left-eye-mirror-burn，左眼镜灼，现于突破前按流程正式解除。解除与突破无关。”"
      }
    ]
  },
  "structured_state": {
    "cultivation": [
      {
        "subject_id": "an-wei",
        "stage": "炼气六层",
        "abilities": [
          "考功堂复核",
          "深层幻境安全裁定"
        ],
        "injuries": [],
        "limits": [
          "不能因救场表现免除已确认的程序违规"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "cen-zhao",
        "stage": "炼气五层",
        "abilities": [
          "回声小周天",
          "基础问心镜阵操作",
          "岑照的照痕辨序提升为可同时分辨主镜与第一节点的残痕。"
        ],
        "injuries": [],
        "limits": [
          "临时监考操作必须由正式监考复核",
          "岑照新增突破后回声分裂活动限制，表现为双重回声、深层定位延迟，并暂停高强度监考。",
          "岑照三日内不得独自进入深层幻境的限制继续有效，并被写入临时监考牌附加条件。",
          "岑照的临时监考操作限制更新为所有镜阵操作须经正式监考复核，候场反光物检查也须由正式监考复核，每日仅可进行低强度节点复核。"
        ],
        "tracked_states": [
          {
            "state_id": "post-breakthrough-echo-splitting",
            "kind": "restriction",
            "description": "岑照新增突破后回声分裂活动限制，表现为双重回声、深层定位延迟，并暂停高强度监考。"
          },
          {
            "state_id": "residual-mark-reading",
            "kind": "ability",
            "description": "岑照的照痕辨序提升为可同时分辨主镜与第一节点的残痕。"
          },
          {
            "state_id": "solo-deep-illusion-ban",
            "kind": "restriction",
            "description": "岑照三日内不得独自进入深层幻境的限制继续有效，并被写入临时监考牌附加条件。"
          },
          {
            "state_id": "temporary-proctor-risk-review",
            "kind": "restriction",
            "description": "岑照的临时监考操作限制更新为所有镜阵操作须经正式监考复核，候场反光物检查也须由正式监考复核，每日仅可进行低强度节点复核。"
          }
        ],
        "last_kind": "restriction",
        "last_change": "岑照的临时监考操作限制更新为所有镜阵操作须经正式监考复核，候场反光物检查也须由正式监考复核，每日仅可进行低强度节点复核。"
      },
      {
        "subject_id": "ruan-qing",
        "stage": "炼气三层",
        "abilities": [
          "副镜清洁",
          "浅层镜纹维护"
        ],
        "injuries": [],
        "limits": [
          "无权修改正式考题、座次或监考记录"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "tang-qiao",
        "stage": "炼气三层",
        "abilities": [
          "基础观想",
          "路径速记"
        ],
        "injuries": [],
        "limits": [
          "不得接触监考封签或镜阵控制区"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "xue-jian",
        "stage": "炼气五层",
        "abilities": [
          "正式幻境监考",
          "封签复核",
          "镜阵调用日志审查"
        ],
        "injuries": [],
        "limits": [
          "必须依据正式记录和可复核证据更正裁定"
        ],
        "tracked_states": []
      }
    ],
    "resources": [
      {
        "owner_id": "cen-zhao",
        "resource_id": "clarity-talisman",
        "amount": 2.0,
        "unit": "张",
        "last_operation": "consume",
        "last_source_or_destination": "稳定旧伤回声并承接突破起始"
      },
      {
        "owner_id": "cen-zhao",
        "resource_id": "low-grade-spirit-stone",
        "amount": 2.0,
        "unit": "枚",
        "last_operation": "consume",
        "last_source_or_destination": "炼气四层到炼气五层突破起始供能槽"
      },
      {
        "owner_id": "exam-hall",
        "resource_id": "exam-hall-reset-seal",
        "amount": 1.0,
        "unit": "枚",
        "last_operation": "consume",
        "last_source_or_destination": "低限试场错层后的全场重置"
      },
      {
        "owner_id": "exam-hall",
        "resource_id": "mirror-sand",
        "amount": 2.0,
        "unit": "份",
        "last_operation": "consume",
        "last_source_or_destination": "副镜封纹"
      }
    ],
    "knowledge": [
      {
        "character_id": "an-wei",
        "fact_id": "cen-zhao-procedure-violations-recorded",
        "state": "knows",
        "belief": "岑照漏做候场副镜第二道封镜检查，并在无正式监考复核时提前启动试场，两项程序违规记过，救场与突破均不抵扣。",
        "last_change": "安苇记录岑照两项程序违规并记过。"
      },
      {
        "character_id": "an-wei",
        "fact_id": "left-eye-mirror-burn-resolved-before-breakthrough",
        "state": "knows",
        "belief": "安苇确认岑照左眼镜灼已在突破前按流程正式解除，且解除与突破无关。",
        "last_change": "安苇完成并记录岑照伤势解除裁定。"
      },
      {
        "character_id": "an-wei",
        "fact_id": "ruan-qing-side-mirror-maintenance-liability",
        "state": "knows",
        "belief": "阮青留置未封校准副镜于候场廊，维护责任入档。",
        "last_change": "安苇将阮青留置未封校准副镜于候场廊记入维护责任。"
      },
      {
        "character_id": "an-wei",
        "fact_id": "tang-qiao-reflection-sketch-spread-risk",
        "state": "knows",
        "belief": "唐桥传播由反光形成的运气图草图，该事实作为传播风险入档，不作正式考题泄露认定，也不作答题凭据。",
        "last_change": "安苇将唐桥传播反光运气图草图作为传播风险事实入档。"
      },
      {
        "character_id": "an-wei",
        "fact_id": "temporary-proctor-qualification",
        "state": "knows",
        "belief": "安苇确认岑照主动泄露嫌疑已被更正，但岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动低限试场仍是程序违规，临时监考资格暂不恢复。",
        "last_change": "安苇对岑照临时监考资格的调查转为明确裁定：暂不恢复，待伤势流程与重开复核完成后再裁定。"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "shared-route-origin",
        "state": "knows",
        "belief": "岑照知道证据链只能证明先副镜、后纸面、再入第三节点的方向和先后，不能证明是谁摆的或为何摆，也不能免除自己的程序责任。",
        "last_change": "岑照对反光路径证据的认知从调查推进为明确限定证明范围。"
      },
      {
        "character_id": "cen-zhao",
        "fact_id": "temporary-proctor-conditions-known",
        "state": "knows",
        "belief": "岑照知道自己只取得附加条件下的临时监考牌，所有镜阵操作须经正式监考复核，三日内不得独自进入深层幻境，每日仅可进行低强度节点复核。",
        "last_change": "岑照接收并知晓临时监考牌的附加条件。"
      },
      {
        "character_id": "ruan-qing",
        "fact_id": "unsealed-calibration-mirror",
        "state": "knows",
        "belief": "阮青承认辰时一刻将校准副镜移出维护架，辰时二刻按规应归架封存但未封，并领记维护责任。",
        "last_change": "阮青未封校准副镜的维护责任被本人承认并由安苇记录。"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "lucky-route-sketch-source",
        "state": "knows",
        "belief": "唐桥知道自己绘制并传播的运气图被定性为传播风险材料，不能作为正式考题证据，也不能证明可通过后续心境关。",
        "last_change": "唐桥对运气图性质的认知被安苇纠正为传播风险材料。"
      },
      {
        "character_id": "tang-qiao",
        "fact_id": "random-heart-test-lucky-route-no-answer",
        "state": "knows",
        "belief": "运气图只押中开场，不包后续，不能作为随机心境关答题依据。",
        "last_change": "唐桥确认运气图无法提供随机心境关答案，并申诉将其改记为普通经验但被拒。"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-zhao-assisted-reopen-under-review",
        "state": "knows",
        "belief": "薛简确认岑照只能在正式监考复核下协助随机幻境重开，不能独自进入深层幻境、触阵枢或单独下令调镜。",
        "last_change": "薛简明确掌握并执行岑照协助重开的资格边界。"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "cen-zhao-not-supported-as-route-leaker",
        "state": "knows",
        "belief": "现有证据不支持岑照主动泄露试炼路线，薛简原先关于岑照可能主动泄露路线的判断已更正。",
        "last_change": "薛简公开更正岑照主动泄露试炼路线的判断不成立。"
      },
      {
        "character_id": "xue-jian",
        "fact_id": "side-mirror-time-record",
        "state": "knows",
        "belief": "薛简掌握辰时一刻副镜移出、辰时二刻应归架未封、辰时二刻又三分岑照无正式监考复核调用低限试场、辰时二刻后反光纸位置登记成形，并知道第三节点残痕与取屑同测证明候场副镜反射路径能够成立。",
        "last_change": "薛简对副镜时间线与反光链条的调查状态完成为已知事实。"
      }
    ]
  },
  "next_chapter_inputs": [
    "岑照已从炼气四层突破至炼气五层，可同时比较主镜与一处回声节点的残痕，但仍不能读取记忆、判断动机或预知随机变化。",
    "post-breakthrough-echo-splitting 仍为活动限制，症状为双重回声、深层定位延迟；岑照暂停高强度监考，三日后再复核，期间不得自行验证。",
    "岑照持有带条件的临时监考牌；违规记过保留，所有镜阵操作须经正式监考复核，候场反光物检查须由正式监考复核，三日内不得独自进入深层幻境，每日仅可进行低强度节点复核。",
    "薛简已公开更正：现有证据不支持岑照主动泄露试炼路线；但岑照漏做候场副镜第二道封镜检查、无正式监考复核提前启动试场两项程序违规已记过。",
    "阮青留置未封校准副镜于候场廊的维护责任已入档；唐桥传播由反光形成的运气图草图作为传播风险事实入档，不作正式考题泄露认定，也不作答题凭据。",
    "问心镜阵主镜、三处回声节点及候场副镜均完成可复核校准，随机幻境考试可在正式监考监督下继续运行。",
    "资源账目保持：exam-hall-reset-seal 余额为 1 枚，mirror-sand 余额为 2 份，岑照 low-grade-spirit-stone 余额为 2 枚，clarity-talisman 余额为 2 张；所有已消耗资源均不得回补。",
    "随机心境关继续证明运气图只可绕过开场陷阱，不能提供后续随机问境答案。"
  ],
  "deviations": [],
  "last_source_draft": "chapters/0010/draft.final.md",
  "last_source_sha256": "49bf276f1877fdf391e2c4dc2524578eb4da1f54fd71ae0b55102dbfcae3dbae",
  "source": "chapters/0010/state-event.json"
}
```
