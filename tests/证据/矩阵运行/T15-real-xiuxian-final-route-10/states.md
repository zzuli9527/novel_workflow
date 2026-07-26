# 逐章正式状态事件

## 第 1 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0001",
  "chapter": 1,
  "source_draft": "chapters/0001/draft.final.md",
  "source_sha256": "2386be7103c3d17634cbab4af421b90ed3c44241008c4de7d8133063d3df4c58",
  "entity_changes": [
    {
      "change": "云蹄鹿栏发生拒食，白绒避开中槽，两只幼鹿随行，成鹿闻槽未食。",
      "source_evidence": "陆宁答：“第三声开食后。白绒先避中槽，两只幼鹿随行，成鹿闻槽未食。”"
    },
    {
      "change": "中槽残留被封存，初步辨出有燥阳谷气味，但投放者未被证明。",
      "source_evidence": "陆宁神色微沉：“像燥阳谷。”\n\n“初闻是。”许苛将残留装瓶，封纸压印，“只说明燥阳谷到过这只槽，不说明谁放的。封存，核份量。”"
    },
    {
      "change": "饲铃牌显示今晨除正常三声铃序外，另有一次三声触发，且紧挨陆宁值守时段。",
      "source_evidence": "“一声，聚栏。二声，冷料分左槽。三声，开食。”许苛念到末尾，手指停住，“这里还有一次三声触发。”\n\n陆宁看见那道细痕紧挨着自己的值守时段，间隔不过半刻。"
    },
    {
      "change": "乔穗已开始把白绒行为转化为可查记录，包括气味、踏痕、进食结果、空桶无暖味和白绒主动嗅闻。",
      "source_evidence": "陆宁把桶翻过来给她看：“它只是闻到桶洗过，没有那股暖味。记空桶无异味，白绒愿意靠近。”\n\n乔穗只得把“证物清白”划去，改成“空桶无暖味，白绒主动嗅闻”。"
    },
    {
      "change": "许苛把异常铃序拓印留存，作为后续复核材料。",
      "source_evidence": "许苛收起封存瓶，将饲铃牌上的异常亮痕拓印下来：“鹿群今日拒食未解。入夜前核完青穗草与燥阳谷出库份量，晚间重走三声铃。谁少报一次动作，便从头复述。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "陆宁被许苛列入重点复核对象，但未被正式定责。",
      "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”"
    },
    {
      "change": "乔穗因坚持把白绒当证人，被许苛安排清点中槽周围全部蹄印。",
      "source_evidence": "许苛却把她的册子抽来看了一遍，又指向栏边：“把中槽周围蹄印全部清点，分出避槽、近槽和后来踩乱的。既称它是证人，你便先把证人的脚印认全。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "injury",
      "change": "陆宁低强度使用听息诀后仍出现耳鸣和轻微方向错觉，breath-echo-vertigo 仍处于活动状态。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "耳中仍“嗡”地一响，食槽边缘像轻轻向左滑了半寸。陆宁闭眼定了定，脚下没有移动。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "insight",
      "change": "陆宁确认听息诀本次只能判断鹿群呼吸发紧、节奏乱和不适，不能判断投料者。",
      "state_id": "",
      "state_action": "",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "乔穗凑近：“它们说什么？”\n\n“呼吸发紧，节奏乱。是不适。”\n\n“谁害的？”\n\n“听不出来。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "solo-night-listening-ban 被许苛重申：伤势确认解除前，陆宁不得独自在夜间对整群云蹄鹿用听息诀，低强度复核也须有人在场。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“禁令再记一次。伤势确认解除前，不得独自在夜间对整群云蹄鹿用听息诀。低强度复核也须有人在场。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "lu-ning",
      "fact_id": "wrong-feed-route",
      "state": "investigating",
      "belief": "燥阳谷到过中槽且异常三声铃紧挨自己的值守时段，但饲铃牌不能证明敲铃者，仍需从铃序、份量和槽路复核。",
      "supersedes_fact_ids": [],
      "change": "陆宁掌握中槽疑似燥阳谷残留与相邻异常铃序的调查焦点，但没有获得投料者结论。",
      "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”\n\n“我没有私加燥阳谷。”陆宁道。\n\n“那就拿铃序、份量和槽路说话。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "investigating",
      "belief": "异常三声铃与陆宁值守相邻，需要复核，但饲铃牌不记敲铃者，不能据此定责陆宁私加燥阳谷。",
      "supersedes_fact_ids": [
        "lu-ning-secret-yang-feed"
      ],
      "change": "许苛不再按既有误信直接认定陆宁私加燥阳谷，而把异常铃序列为复核项。",
      "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trial-qualification-result",
      "state": "investigating",
      "belief": "陆宁试用表现需按铃序、饲料份量和兽栏后果继续复核，灵兽亲近或避开不算证据。",
      "supersedes_fact_ids": [],
      "change": "许苛明确后续裁定标准为铃序、饲料份量和兽栏后果。",
      "source_evidence": "许苛封好瓷瓶：“亲近不抵一粒谷，避开也不抵一声铃。后续我只看铃序、饲料份量和兽栏后果。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-record-format",
      "state": "knows",
      "belief": "白绒避槽不能直接记成证词，必须写成气味、踏痕和进食结果等可复查记录。",
      "supersedes_fact_ids": [],
      "change": "乔穗被陆宁和许苛纠正记录方式。",
      "source_evidence": "乔穗张了张嘴。\n\n“写气味、踏痕、进食结果。”许苛取出封料纸和细口瓷瓶，“灵兽不是值房执事，它不签押。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-hoofprint-count",
      "state": "investigating",
      "belief": "需要清点中槽周围蹄印，分出避槽、近槽和后来踩乱的痕迹。",
      "supersedes_fact_ids": [],
      "change": "乔穗开始调查并记录白绒及鹿群在中槽周围的蹄印。",
      "source_evidence": "许苛却把她的册子抽来看了一遍，又指向栏边：“把中槽周围蹄印全部清点，分出避槽、近槽和后来踩乱的。既称它是证人，你便先把证人的脚印认全。”"
    }
  ],
  "thread_changes": [
    {
      "change": "燥阳谷残留调查正式启动，下一步要核青穗草与燥阳谷出库份量并复走三声铃。",
      "source_evidence": "许苛收起封存瓶，将饲铃牌上的异常亮痕拓印下来：“鹿群今日拒食未解。入夜前核完青穗草与燥阳谷出库份量，晚间重走三声铃。谁少报一次动作，便从头复述。”"
    },
    {
      "change": "陆宁今夜将在监督下复核封存残留、铃序和鹿栏安抚流程。",
      "source_evidence": "许苛转向陆宁：“今夜在我或指定弟子监督下，复核封存残留、铃序和鹿栏安抚流程。你的听息回声眩晕尚在，方才只听数息，耳鸣也没避过。”"
    },
    {
      "change": "鹿群拒食仍未解决，成为晚间复核和安抚流程的紧迫问题。",
      "source_evidence": "许苛收起封存瓶，将饲铃牌上的异常亮痕拓印下来：“鹿群今日拒食未解。入夜前核完青穗草与燥阳谷出库份量，晚间重走三声铃。谁少报一次动作，便从头复述。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗把白绒避槽称为指认，被陆宁纠正为不能给鹿安身份。",
      "source_evidence": "乔穗立刻放下空桶：“白绒指认中槽。”\n\n“先别给它安身份。”"
    },
    {
      "change": "乔穗把白绒嗅空桶解读为证物清白，被陆宁改成空桶无暖味、白绒主动嗅闻的记录。",
      "source_evidence": "乔穗抬头：“它选了证物。”\n\n“桶里什么都没有。”\n\n“所以清白。”\n\n陆宁把桶翻过来给她看：“它只是闻到桶洗过，没有那股暖味。记空桶无异味，白绒愿意靠近。”"
    },
    {
      "change": "许苛把乔穗的拟人化证词说法转化成清点全部蹄印的苦差。",
      "source_evidence": "乔穗望着满地交叠的鹿蹄印，抱紧册子：“它的证词略显繁复。”\n\n“所以让你清点。”"
    }
  ],
  "new_constraints": [
    {
      "change": "饲铃牌异常只可作为复核项，不能单独证明敲铃者或定责。",
      "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”"
    },
    {
      "change": "中槽燥阳谷残留只证明燥阳谷到过该槽，不证明投放者。",
      "source_evidence": "“初闻是。”许苛将残留装瓶，封纸压印，“只说明燥阳谷到过这只槽，不说明谁放的。封存，核份量。”"
    },
    {
      "change": "灵兽亲近或避开某人不作为免责或定责证据，后续裁定只看铃序、饲料份量和兽栏后果。",
      "source_evidence": "许苛封好瓷瓶：“亲近不抵一粒谷，避开也不抵一声铃。后续我只看铃序、饲料份量和兽栏后果。”"
    },
    {
      "change": "陆宁晚间复核听息与鹿栏流程必须在许苛或指定弟子监督下进行。",
      "source_evidence": "许苛转向陆宁：“今夜在我或指定弟子监督下，复核封存残留、铃序和鹿栏安抚流程。你的听息回声眩晕尚在，方才只听数息，耳鸣也没避过。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "陆宁、乔穗今夜将在许苛或指定弟子监督下复核封存残留、铃序和鹿栏安抚流程。",
    "中槽残留已封存，初闻像燥阳谷，只能证明燥阳谷到过中槽，不能证明投放者。",
    "饲铃牌显示有一次紧挨陆宁值守时段的异常三声触发，但饲铃牌不记敲铃者。",
    "鹿群今日拒食未解，入夜前需核完青穗草与燥阳谷出库份量，晚间重走三声铃。",
    "乔穗负责清点中槽周围蹄印，分出避槽、近槽和后来踩乱的痕迹。",
    "陆宁的 breath-echo-vertigo 仍在，低强度听息后仍耳鸣；solo-night-listening-ban 仍有效。"
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
  "source_sha256": "7898059cc6e31de82747f085d01e917a2da660847f7203bb7343795e3b7b26a5",
  "entity_changes": [
    {
      "change": "云蹄鹿栏门铰裂损，栏门歪斜，只能临时加固，不能当场恢复，需后续报修。",
      "source_evidence": "许苛蹲下检查门铰。裂口贯过铰片，固定钉也被扯松。他没有伸手硬掰，只取出损坏签压在门柱上，又命乔穗搬来横木，从外侧抵住歪斜栏门。\n\n“铰片裂损，当场不能恢复。今夜只能临时加固，明日起报修。修料、工时与赔偿，你参与核算。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "injury",
      "change": "陆宁超限对整群使用听息诀后，breath-echo-vertigo 加重，出现更严重耳鸣与方向错判。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "陆宁眼前的栏木陡然倾斜。他分明朝左迈步，身体却撞上右侧门柱。方向在耳鸣里整个翻了过来。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "许苛确认陆宁听息回声加重、方向错判，solo-night-listening-ban 仍持续有效，并另记其超限施术。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛看了他一眼：“听息回声加重，方向错判。禁令仍在，另记超限施术。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格被冻结，复核前不得独立值栏。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "lu-ning",
      "resource_id": "contribution-point",
      "operation": "consume",
      "amount": 2,
      "unit": "点",
      "resulting_balance": 4,
      "source_or_destination": "御兽苑考核处罚",
      "change": "陆宁因宵禁入栏、擅改铃序和处置不当致栏门铰损坏，被扣除贡献二点，余额由六点变为四点。",
      "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "lu-ning",
      "fact_id": "wrong-feed-route",
      "state": "investigating",
      "belief": "陆宁知道自己没有加燥阳谷，并继续把燥阳谷残留与饲料路线作为需要查明的问题。",
      "supersedes_fact_ids": [],
      "change": "陆宁明确否认自己加过燥阳谷，但正文没有证明其否认已被他人采信或最终定案。",
      "source_evidence": "陆宁听见“冻结”二字，指尖慢慢收紧，却没有辩解前面三项。\n\n“燥阳谷不是我加的。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "suspects",
      "belief": "许苛当前按陆宁可能私加暖料的方向核查，但承认这不是定案，燥阳谷残留只能证明暖性饲料到过鹿栏，不能单独证明投放者。",
      "supersedes_fact_ids": [
        "lu-ning-secret-yang-feed-review"
      ],
      "change": "许苛将核查方向更新为怀疑陆宁可能私加暖料，同时保留饲料路线核查空间。",
      "source_evidence": "许苛合上半边册页：“中槽有燥阳谷残留，错铃发生在你值守相邻时段，今夜你又私自改铃。我当前先按你可能私加暖料核查。”\n\n“饲铃牌不记敲铃者。”\n\n“所以我说核查，不是定案。”许苛指向封住的中槽，“残留只能证明暖性饲料到过鹿栏，不能单独证明谁投放。你的违规与投料责任分开记。铃序、份量、饲料路线，一项都不会少。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trial-qualification-result",
      "state": "knows",
      "belief": "许苛已按宵禁入栏、擅改安抚铃序、处置不当致栏门铰损坏，裁定陆宁扣贡献二点、试用资格冻结、复核前不得独立值栏。",
      "supersedes_fact_ids": [
        "trial-qualification-result"
      ],
      "change": "许苛对陆宁试用表现的复核从调查状态推进为当场处罚裁定。",
      "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-hoofprint-count",
      "state": "investigating",
      "belief": "乔穗在清点白绒与鹿群踏痕时发现一串非鹿蹄的圆钝压痕，压痕通向食槽阵压力石旁，来源尚未确认。",
      "supersedes_fact_ids": [
        "white-tuft-hoofprint-count"
      ],
      "change": "乔穗的蹄印清点从单纯分辨鹿蹄痕，推进到发现压力石旁的非鹿压痕线索。",
      "source_evidence": "泥里有一串圆钝压痕，边缘宽厚，没有分瓣，不是云蹄鹿留下的。压痕从中槽后方斜穿清理道，一直没入食槽阵的石廊。\n\n乔穗挪过灯盏，顺着最后两枚压痕照去。\n\n它们正停在那块压力石旁。"
    }
  ],
  "thread_changes": [
    {
      "change": "陆宁在宵禁后违规入栏查看鹿群拒食变化。",
      "source_evidence": "监督复核已经结束，许苛临走前封了中槽，也重申过禁令。按规矩，此刻陆宁该回试舍。\n\n白绒忽然晃了一下，前膝几乎碰到地面。\n\n陆宁推门入栏。"
    },
    {
      "change": "陆宁为避开白绒惊跳而擅自改变安抚铃顺序，饲铃牌留下右、左、中错铃记录。",
      "source_evidence": "他抬手先敲了右铃。\n\n清响荡过栏顶。\n\n饲铃牌上，一道银纹随即亮起，右侧槽位下方也闪过一线微光。\n\n乔穗脸色变了：“顺序错了。”"
    },
    {
      "change": "暖性残留与错位铃声共同刺激鹿群，拒食升级为冲栏，柔缰引导无法压制整群。",
      "source_evidence": "白绒从中槽边横窜，鹿群被它带得挤向栏门。暖性残留令几只鹿呼吸发急，错位的铃声又把它们引向相反方向。前鹿想退，后鹿仍在向前，鹿角与栏木接连擦响。\n\n陆宁甩出柔缰。\n\n两缕低强度灵气绕上最前方两只鹿的肩颈，将它们往侧道牵。它们偏开半步，后方鹿群一拥，两缕柔缰当即绷直。陆宁手腕一沉，鞋底被拖过湿草，掌中灵气也被冲势震得断续。\n\n炼气二层的柔缰能改小兽方向，压不住整群冲势。"
    },
    {
      "change": "乔穗发现通向食槽阵压力石旁的非鹿圆钝压痕，为后续追查压力石受压留下入口。",
      "source_evidence": "尺端忽然停住。\n\n泥里有一串圆钝压痕，边缘宽厚，没有分瓣，不是云蹄鹿留下的。压痕从中槽后方斜穿清理道，一直没入食槽阵的石廊。\n\n乔穗挪过灯盏，顺着最后两枚压痕照去。\n\n它们正停在那块压力石旁。"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗把安抚铃戏称为“白绒同意铃”，但鹿群实际躁动使这个说法失效。",
      "source_evidence": "乔穗盯着那三道纹：“这不是白日的安抚铃。”\n\n“我知道。”\n\n“我原先还想叫它‘白绒同意铃’。”\n\n“它现在不同意。”"
    },
    {
      "change": "乔穗把白绒受惊后的走法比作证人改口，被许苛压回量尺记录。",
      "source_evidence": "“它方才受惊，前后走法不一样，像是证人改了口。”\n\n“闭嘴，量尺。”"
    }
  ],
  "new_constraints": [
    {
      "change": "鹿栏门铰裂损不可当场恢复，今夜只能临时加固，明日起报修，陆宁要参与修料、工时与赔偿核算。",
      "source_evidence": "“铰片裂损，当场不能恢复。今夜只能临时加固，明日起报修。修料、工时与赔偿，你参与核算。”"
    },
    {
      "change": "陆宁试用资格冻结，复核前不得独立值栏。",
      "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
    },
    {
      "change": "陆宁被另记超限施术，solo-night-listening-ban 继续有效。",
      "source_evidence": "许苛看了他一眼：“听息回声加重，方向错判。禁令仍在，另记超限施术。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "陆宁处于试用资格冻结状态，复核前不得独立值栏。",
    "陆宁贡献点余额为四点，扣除的二点未退还。",
    "陆宁 breath-echo-vertigo 加重，仍有耳鸣与方向错判，solo-night-listening-ban 继续有效。",
    "鹿栏门铰裂损未修复，今夜仅临时加固，明日起报修；陆宁需参与修料、工时与赔偿核算。",
    "许苛当前按陆宁可能私加暖料核查，但承认燥阳谷残留只能证明暖性饲料到过鹿栏，不能单独证明投放者，仍要查铃序、份量和饲料路线。",
    "乔穗已发现一串非鹿蹄的圆钝压痕，从中槽后方通向食槽阵压力石旁，来源未确认。"
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
  "source_sha256": "93784466165aef33b0c2c44dbc1166aa5be29ff2ca8a5d527301858fdac07041",
  "entity_changes": [
    {
      "change": "鹿栏门铰仍裂损，已加临时横撑但未修复，后续仍需报修、工时和赔偿核算。",
      "source_evidence": "他又指了指栏门：“复查前，先加一道横撑。昨夜的麻绳只够撑到今日。门铰裂了就是裂了，不会因为查出别的路径便自己长好。报修、工时、赔偿，后续照算。”"
    },
    {
      "change": "食槽阵压力石被确认只响应重量和持续时间，不能识别压石对象或引导者。",
      "source_evidence": "“压力石认重量和持续时间，不认蹄子，更不认引导者。”他说，“压痕与贪食豚栏常见蹄垫痕相似，只能记相似。不得定哪只豚，也不得定谁带来的。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "许苛准许陆宁进行有限复查，但复查必须在白日、有许苛或同组弟子在场，并禁止陆宁听整群兽息或独立触动食槽阵。",
      "source_evidence": "许苛合上簿册，“复查准许。只限白日，须我或同组弟子在场，不得听整群兽息，不得独立触动食槽阵。夜间禁令照旧。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "injury",
      "change": "陆宁的 breath-echo-vertigo 仍处于加重状态，未运诀时也出现方向错判，被许苛记入观察。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "source_evidence": "许苛在值事簿上添了一行：“辰时，方向错判一次，旁人扶正。听息回声仍重。”\n\n“我没有运诀。”陆宁道。\n\n“所以记伤势，不记施术。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "solo-night-listening-ban 继续有效，且复查期间不得听整群兽息。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "source_evidence": "许苛合上簿册，“复查准许。只限白日，须我或同组弟子在场，不得听整群兽息，不得独立触动食槽阵。夜间禁令照旧。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格仍被冻结，冻结木牌继续挂在名册上。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "source_evidence": "乔穗问：“那他的牌呢？”\n\n许苛把“冻结”木牌重新挂回名册：“挂着。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-record-format",
      "state": "knows",
      "belief": "乔穗知道不能把白绒的行为写成告状或证词，已改为记录避槽位置、绕行距离、暖性气味与圆钝压痕等可验证事项。",
      "supersedes_fact_ids": [],
      "change": "乔穗将对白绒行为的拟人化判断改成可验证记录格式。",
      "source_evidence": "乔穗重新铺开沾泥薄纸，将“白绒在告状”彻底划去，逐项写下避槽位置、绕行距离、暖性气味与圆钝压痕。"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-hoofprint-count",
      "state": "investigating",
      "belief": "乔穗已量得中槽后方到食槽阵压力石旁存在宽圆钝厚的非鹿蹄压痕，并发现其与贪食豚蹄垫痕宽度和后缘相近，但来源未确认。",
      "supersedes_fact_ids": [],
      "change": "乔穗的圆钝压痕线索推进到与贪食豚栏常见蹄垫痕相似的可比对记录。",
      "source_evidence": "通往暖料槽路的那块石面沾着薄泥，石旁草根倒伏，正有两枚较完整的圆钝印。\n\n乔穗取出细绳贴着边缘一围，再与方才拓下的尺寸比对。\n\n“宽度相近，后缘也一样钝。”她抬头，“是贪食豚。”"
    },
    {
      "character_id": "lu-ning",
      "fact_id": "wrong-feed-route",
      "state": "investigating",
      "belief": "陆宁正在调查燥阳谷进入鹿栏的路径，并提出压力石持续受压叠加异常铃序可能导致暖料转错槽位，但尚未证明。",
      "supersedes_fact_ids": [],
      "change": "陆宁将调查方向推进到压力石受压、异常铃序与暖料错槽之间的关联。",
      "source_evidence": "陆宁察看倒伏草根：“若此石持续受压，再叠上异常铃序，暖料可能转错槽位。”\n\n许苛看了他一眼：“可能。不是已经证明。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "suspects",
      "belief": "许苛仍未排除陆宁私加暖料，但也承认现有事实不能证明陆宁投放过燥阳谷。",
      "supersedes_fact_ids": [],
      "change": "许苛对陆宁私加暖料的怀疑未解除，但明确仍非定案。",
      "source_evidence": "许苛收起三张纸：“现有事实仍不能排除你私加暖料，也不能证明你投放过。冻结不解，错铃与宵禁记录不撤。”"
    }
  ],
  "thread_changes": [
    {
      "change": "后续核查被拆分为压力石受压记录、饲铃牌异常铃序和燥阳谷残留路线三条线索。",
      "source_evidence": "“第一张，只记压力石：压痕尺寸、泥层、草根倒向，另查受压时长。”\n\n“第二张，只记饲铃牌：哪一铃异常，触发哪个槽位。饲铃牌不记敲铃者，别擅自添名字。”\n\n“第三张，只记燥阳谷残留：中槽、槽缝、阵路沿途各有多少，气味和颗粒往哪边递减。”"
    },
    {
      "change": "下一步将先对白日压力石受压记录进行核查，再与贪食豚栏蹄垫痕对照；若尺寸不合，此线索将被划掉。",
      "source_evidence": "“明日白日，先对压力石受压记录，再对贪食豚栏蹄垫痕。若尺寸不合，这条线便划掉。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗将白绒行为拟人化为态度、失望和拒绝签字，被许苛要求删除。",
      "source_evidence": "乔穗低头看自己的纸。上面第一行写着“白绒态度坚决”，第二行写着“白绒对中槽深感失望”。\n\n她默默把两行划掉，问：“那‘拒绝签字’呢？”\n\n“也删。”"
    },
    {
      "change": "许苛用分项记录规则纠正乔穗把灵兽行为直接拼成责任人的做法。",
      "source_evidence": "乔穗问：“白绒的拒食放哪张？”\n\n“另纸。它能证明自己避了什么，不能替你们把三张纸缝成一个人。”"
    }
  ],
  "new_constraints": [
    {
      "change": "陆宁获得的复查机会受限于白日、有监督、不得听整群兽息、不得独立触动食槽阵，夜间禁令继续有效。",
      "source_evidence": "许苛合上簿册，“复查准许。只限白日，须我或同组弟子在场，不得听整群兽息，不得独立触动食槽阵。夜间禁令照旧。”"
    },
    {
      "change": "陆宁今日承担半个时辰临时加固工时，但不能抵扣已扣除的二点贡献。",
      "source_evidence": "“明白便记工。今日半个时辰，不抵扣那二点贡献。”"
    },
    {
      "change": "圆钝压痕只能记录为与贪食豚栏常见蹄垫痕相似，不能确认具体灵兽或引导者。",
      "source_evidence": "“压力石认重量和持续时间，不认蹄子，更不认引导者。”他说，“压痕与贪食豚栏常见蹄垫痕相似，只能记相似。不得定哪只豚，也不得定谁带来的。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "陆宁试用资格仍被冻结，冻结木牌继续挂在名册上。",
    "陆宁 breath-echo-vertigo 仍重，已被许苛记录辰时方向错判一次、旁人扶正；他本章没有运诀。",
    "陆宁获得一次白日有限复查机会，必须有许苛或同组弟子在场，不得听整群兽息，不得独立触动食槽阵，夜间禁令照旧。",
    "鹿栏门铰仍裂损，仅加临时横撑；报修、工时、赔偿后续照算，今日半个时辰工时不抵扣已扣二点贡献。",
    "乔穗已把白绒行为改写为避槽位置、绕行距离、暖性气味与圆钝压痕等可验证记录，不再把白绒选择直接当定责证词。",
    "压力石旁圆钝压痕与贪食豚栏常见蹄垫痕相似，但不能确认具体哪只灵兽、何时来、是否被人引导。",
    "许苛仍怀疑陆宁可能私加暖料，但承认现有事实既不能排除也不能证明陆宁投放过。",
    "下一步核查分为压力石受压记录、饲铃牌异常铃序、燥阳谷残留路线；明日白日先对压力石受压记录，再对贪食豚栏蹄垫痕。"
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
  "source_sha256": "50d35b77086fcf17fb348e1d30e4ebf34b8ae40eeeb957a305dd218ea898702e",
  "entity_changes": [
    {
      "change": "压力石周边阵沟泥水下发现带甜气的淡黄纤维，并被要求分袋留样。",
      "source_evidence": "泥水下露出几缕黏在阵沟边的淡黄纤维，带着一丝不属于普通草料的甜气。\n\n许苛俯身看了一眼，没有触碰。\n\n“分袋留样。”他道，“再去取甜根囊领用册。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "ability",
      "change": "陆宁的听息诀在监督下通过单兽低强度校验，初步能区分白绒的受热不适呼吸与昨夜群体惊慌节奏，但仍限于报节奏，不得猜人或读心。",
      "state_id": "beast-breath-listening",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“能。”陆宁没有起身，“白绒现在是短促、避热式呼吸。受暖性气味刺激，停顿固定。昨夜冲栏前是节奏互相催快，停顿散乱，属于群体惊慌。两者不同。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "recovery",
      "change": "陆宁的听息回声眩晕出现部分恢复苗头：耳鸣短暂减轻，但眩晕未解除。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "片刻后，耳中的尖鸣稍稍退远，像从耳骨里挪到了院墙外，可脚下仍有轻微倾斜感。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁的夜间独自整群听息禁令继续有效。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“二点贡献也不退，余额仍是四点。试用冻结照旧。”许苛道，“你方才耳鸣减轻，只算恢复苗头。眩晕未除，夜间独自整群听息禁令继续。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格仍被冻结。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“二点贡献也不退，余额仍是四点。试用冻结照旧。”许苛道，“你方才耳鸣减轻，只算恢复苗头。眩晕未除，夜间独自整群听息禁令继续。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "lu-ning",
      "fact_id": "wrong-feed-route",
      "state": "knows",
      "belief": "压力石持续受压会使暖槽偏向鹿栏；解除压力后阵路复位，但昨夜压石对象和诱因尚未确定。",
      "supersedes_fact_ids": [
        "wrong-feed-route"
      ],
      "change": "陆宁参与复核后，原本调查中的错送路线被现场确认到机制层面。",
      "source_evidence": "许苛将三次结果写进阵录：“持续受压，暖槽偏向鹿栏；解除压力，阵路复位。错送可能存在。至于昨夜压石的是不是这只、为何停留，尚不能定。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "pig-pressure-stone",
      "state": "knows",
      "belief": "贪食豚持续趴在压力石上可触发暖槽阵路偏向鹿栏，但压力石只记录重量和时长，不识别压石对象。",
      "supersedes_fact_ids": [
        "pig-pressure-stone"
      ],
      "change": "乔穗对贪食豚压石与暖性饲料错路有关的怀疑被现场复核确认为机制事实。",
      "source_evidence": "乔穗划去两字，又在路线末端重重圈住鹿栏：“但阵路偏了。”\n\n“这可以记。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-hoofprint-count",
      "state": "investigating",
      "belief": "乔穗继续围绕贪食豚栏、压力石周边泥印和草屑留样核查压痕与停留痕迹。",
      "supersedes_fact_ids": [],
      "change": "乔穗被安排清理贪食豚栏和压力石周边，并分别留样泥印、草屑。",
      "source_evidence": "许苛指向贪食豚栏：“能。画图的人最熟压痕与阵沟，午后清豚栏，再刷压力石周边。泥印、草屑分别留样。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "suspects",
      "belief": "许苛承认阵路错送可能存在，但仍继续调查陆宁私加燥阳谷一项，且不因此抵销陆宁错铃、宵禁入栏等违规。",
      "supersedes_fact_ids": [
        "lu-ning-secret-yang-feed-review"
      ],
      "change": "许苛对陆宁私加暖料的怀疑被进一步削弱为仍查，同时明确阵路机制不能直接洗清违规。",
      "source_evidence": "陆宁问：“私加燥阳谷一项呢？”\n\n“仍查。”许苛合上阵录，“阵路能把暖料送错，不等于昨夜一定如此；更不等于你的错铃、宵禁入栏可以不算。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trough-pressure-route",
      "state": "knows",
      "belief": "持续受压会使暖槽偏向鹿栏，解除压力后阵路复位；但昨夜压石对象和停留原因尚不能定。",
      "supersedes_fact_ids": [],
      "change": "许苛亲自把压力石持续受压导致暖槽偏鹿栏的复核结果写入阵录。",
      "source_evidence": "许苛将三次结果写进阵录：“持续受压，暖槽偏向鹿栏；解除压力，阵路复位。错送可能存在。至于昨夜压石的是不是这只、为何停留，尚不能定。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "white-tuft-heat-discomfort",
      "state": "knows",
      "belief": "鹿对暖性余味有受热不适，与群体惊慌节奏不同；该结论不能证明投料者、昨夜具体阵路，也不能抵销陆宁错铃与宵禁违规。",
      "supersedes_fact_ids": [],
      "change": "许苛认可陆宁对白绒单兽低强度听息结果的有限边界，并将其纳入记录。",
      "source_evidence": "“可作低强度对照。”许苛在阵录后添上一行，“鹿对暖性余味有受热不适，与群体惊慌节奏不同。”\n\n他笔锋一转，又补了三句：“不能证明谁投料。不能证明昨夜具体阵路。不能抵销错铃与宵禁违规。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "sweet-root-fiber-sample",
      "state": "investigating",
      "belief": "压力石周边阵沟发现带甜气的淡黄纤维，需要分袋留样并调取甜根囊领用册继续核查。",
      "supersedes_fact_ids": [],
      "change": "许苛开始调查压力石周边淡黄纤维与甜根囊领用去向。",
      "source_evidence": "泥水下露出几缕黏在阵沟边的淡黄纤维，带着一丝不属于普通草料的甜气。\n\n许苛俯身看了一眼，没有触碰。\n\n“分袋留样。”他道，“再去取甜根囊领用册。”"
    }
  ],
  "thread_changes": [
    {
      "change": "食槽阵复核确认压力石持续受压会导致暖槽偏向鹿栏，解除压力后阵路复位，但昨夜具体压石对象和原因未定。",
      "source_evidence": "许苛将三次结果写进阵录：“持续受压，暖槽偏向鹿栏；解除压力，阵路复位。错送可能存在。至于昨夜压石的是不是这只、为何停留，尚不能定。”"
    },
    {
      "change": "压力石不识别压石对象，只记录重量和持续时间。",
      "source_evidence": "许苛扫过她的纸：“删掉‘对象’二字。压力石只记重量和时长，不认压它的是豚、石墩还是人。”"
    },
    {
      "change": "乔穗完成暖槽偏移路线图，并被安排午后清理贪食豚栏和压力石周边，泥印、草屑分别留样。",
      "source_evidence": "许苛指向贪食豚栏：“能。画图的人最熟压痕与阵沟，午后清豚栏，再刷压力石周边。泥印、草屑分别留样。”"
    },
    {
      "change": "压力石周边发现疑似诱引线索，下一步转向甜根囊领用册核查。",
      "source_evidence": "泥水下露出几缕黏在阵沟边的淡黄纤维，带着一丝不属于普通草料的甜气。\n\n许苛俯身看了一眼，没有触碰。\n\n“分袋留样。”他道，“再去取甜根囊领用册。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "贪食豚把压力石当暖垫趴住，还翻面继续取暖，直接触发严肃阵路复核结果。",
      "source_evidence": "灰背贪食豚被铜片声吵醒，换了个方向，把另一面肚皮贴上压力石。赤纹因此更亮，鹿栏铜槽又升了一分温。\n\n陆宁道：“它在翻面。”\n\n乔穗认真记下：“压石对象翻面后，槽温继续上升。”"
    },
    {
      "change": "乔穗把贪食豚当“证人”的说法被许苛纠正为它只是睡觉造成阵路偏移。",
      "source_evidence": "“它没作证。”许苛道，“它只睡了一觉。你记录的是这一觉压坏了哪条路。”"
    }
  ],
  "new_constraints": [
    {
      "change": "复核期间陆宁只能报槽位，不能碰铃或动阵栓；再认错方向即停。",
      "source_evidence": "许苛看了一眼漏刻：“复核期间，你只准报槽位，不准碰铃，不准动阵栓。若再认错方向，立即停。”"
    },
    {
      "change": "陆宁进行听息校验时只能听单只白绒十息，不能扩到鹿群，也不能借呼吸猜人。",
      "source_evidence": "陆宁坐在隔绳外，双手压膝：“只听它一只，十息。若有方向错判，立刻停。”\n\n许苛站在他右后方：“不得扩到鹿群。不得借呼吸猜人。说节奏，不说心思。”"
    },
    {
      "change": "陆宁错铃、宵禁入栏仍不因阵路错送机制而取消。",
      "source_evidence": "“仍查。”许苛合上阵录，“阵路能把暖料送错，不等于昨夜一定如此；更不等于你的错铃、宵禁入栏可以不算。”"
    },
    {
      "change": "陆宁栏门损坏责任、已扣二点贡献、试用冻结和夜间独自整群听息禁令均继续保留。",
      "source_evidence": "陆宁看着那三句：“栏门损坏也不抵。”\n\n“二点贡献也不退，余额仍是四点。试用冻结照旧。”许苛道，“你方才耳鸣减轻，只算恢复苗头。眩晕未除，夜间独自整群听息禁令继续。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "食槽阵已复核确认：持续受压会使暖槽偏向鹿栏，解除压力后阵路复位；但昨夜压石对象和停留原因尚未定。",
    "压力石只记录重量和时长，不能识别压石对象。",
    "陆宁听息诀已在单兽低强度校验中初步区分白绒受热不适与群体惊慌节奏，但不得读心、猜人或扩到整群。",
    "陆宁 breath-echo-vertigo 仅有恢复苗头：耳鸣短暂减轻，眩晕未除；夜间独自整群听息禁令继续。",
    "陆宁试用资格仍被冻结；错铃、宵禁入栏、栏门损坏责任不抵销；已扣二点贡献不退，余额仍是四点。",
    "乔穗已完成暖槽偏移路线图，并被安排清理贪食豚栏与压力石周边，泥印、草屑分别留样。",
    "压力石周边阵沟发现带甜气的淡黄纤维，许苛要求分袋留样并取甜根囊领用册。"
  ],
  "deviations": [
    {
      "change": "本章额外发现压力石周边阵沟有带甜气的淡黄纤维，并启动甜根囊领用册核查；细纲只要求本章尚未完成调取甜根囊领用去向。",
      "source_evidence": "泥水下露出几缕黏在阵沟边的淡黄纤维，带着一丝不属于普通草料的甜气。\n\n许苛俯身看了一眼，没有触碰。\n\n“分袋留样。”他道，“再去取甜根囊领用册。”"
    }
  ]
}
```

## 第 5 章

```json
{
  "state_schema_version": "1.1",
  "event_id": "chapter-0005",
  "chapter": 5,
  "source_draft": "chapters/0005/draft.final.md",
  "source_sha256": "66e607178fb4f675804f29d9e59e46804e7f0c11079328ac364acdb901ab6410",
  "entity_changes": [
    {
      "change": "甜根囊领用册确认昨夜酉末有一袋甜根囊由贺鸣领出，名目为安置贪食豚换栏，且无归还、耗用记录。",
      "source_evidence": "“甜根囊，一袋。酉末领出，名目——安置贪食豚换栏。领用人，贺鸣。”\n\n账房里静了片刻。\n\n贺鸣站在门旁，目光落在账页上：“是我领的。”\n\n许苛问：“归还记录呢？”\n\n“用过了。”\n\n“耗用记录呢？”\n\n“当时忙，漏写了。”"
    },
    {
      "change": "压力石阵沟留样与未拆甜根囊外袋纤维完成比对，记录为气味相近、纤维形态相近、来源待核。",
      "source_evidence": "乔穗用细针拨了拨：“都是三股细丝拧成，断口散开，气味也近。”\n\n许苛问：“能写什么？”\n\n“甜根囊来过这里。”\n\n陆宁摇头：“只能写甜根囊外袋同类纤维曾接近此处。留样不能说明是谁带来，也不能说明贪食豚一定压过石。”\n\n乔穗把笔尖移回去，逐字改成：“气味相近，纤维形态相近，来源待核。”"
    }
  ],
  "relationship_changes": [
    {
      "change": "贺鸣与昨夜甜根囊领用去向建立正式核查关系，但正文未确认其投放燥阳谷或引豚压石。",
      "source_evidence": "“我没往鹿栏投过。”贺鸣道，“甜根囊只是为了让贪食豚离开我的栏位。它后来往哪儿蹭，是它自己的腿。”\n\n“腿不记账，人记。”许苛在领用条目旁落下一笔，“去向待核。你随时听问，不得补写旧记录。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "ability",
      "change": "陆宁在许苛监督下只对白绒施展一次短促单兽听息，确认其可记录单兽受热不适前的躲槽节奏，仍未扩展到整群、读心或辨人。",
      "state_id": "beast-breath-listening",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛看向陆宁：“一次，短息。只听白绒。”\n\n陆宁按住耳后封耳条，缓缓引出一缕灵气。听息诀只落在白绒身上，不向旁侧扩散。\n\n细碎的呼吸声贴近耳中。\n\n两短，一滞，再短促收紧。\n\n不像昨夜群体惊慌时此起彼伏的急乱，也没有互相追随的节奏。更像白绒先前靠近暖槽时，胸息受热后出现的回避。\n\n陆宁立刻收诀。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "injury",
      "change": "陆宁听息后仍有耳闷和轻微晕感，听息回声眩晕未解除。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "耳内仍旧闷响了一下，脚下也有轻微浮晃。他扶住栏柱，等视线定住，才开口：“单兽。受热不适前的躲槽节奏，不是群体惊慌。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁今日不得再听息，夜间独自整群听息禁令继续有效。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“今日不得再听。夜间独自整群听息禁令照旧。”\n\n陆宁应下，重新压紧封耳条。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格继续冻结。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“这不代表你已洗清。宵禁入栏、错铃、栏门铰损坏另册照记。试用资格继续冻结，扣去的二点不退，余额四点。”"
    }
  ],
  "resource_changes": [
    {
      "owner_id": "beast-yard",
      "resource_id": "sweet-root-pouch",
      "operation": "consume",
      "amount": 1,
      "unit": "袋",
      "resulting_balance": 3,
      "source_or_destination": "贺鸣昨夜领出后称已用过且漏写耗用记录",
      "change": "御兽苑甜根囊账面确认少一袋：昨夜由贺鸣领出，贺鸣称已用过但无耗用记录。",
      "source_evidence": "贺鸣站在门旁，目光落在账页上：“是我领的。”\n\n许苛问：“归还记录呢？”\n\n“用过了。”\n\n“耗用记录呢？”\n\n“当时忙，漏写了。”"
    }
  ],
  "knowledge_changes": [
    {
      "character_id": "xu-ke",
      "fact_id": "sweet-root-fiber-sample",
      "state": "investigating",
      "belief": "甜根囊外袋同类纤维曾接近压力石阵沟，气味与形态相近，但不能证明是谁带来，也不能证明贪食豚一定压过石。",
      "supersedes_fact_ids": [],
      "change": "许苛将淡黄纤维线索从取册核查推进为纤维、气味与位置比对后的待核证据。",
      "source_evidence": "陆宁摇头：“只能写甜根囊外袋同类纤维曾接近此处。留样不能说明是谁带来，也不能说明贪食豚一定压过石。”\n\n乔穗把笔尖移回去，逐字改成：“气味相近，纤维形态相近，来源待核。”\n\n许苛收走两份比对记录：“这才是账上能用的话。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "suspects",
      "belief": "陆宁是否私加燥阳谷仍未洗清，但调查不再只围绕陆宁，需并查甜根囊去向、贪食豚停留和暖槽错路。",
      "supersedes_fact_ids": [],
      "change": "许苛保留陆宁私加燥阳谷疑点，同时扩大调查证据链。",
      "source_evidence": "“从今日起，不再只复查陆宁是否私加燥阳谷。”许苛道，“分三段查。甜根囊从领出到耗用去了哪里；贪食豚昨夜停在何处、停了多久；暖槽错路是否与受压时段重合。”\n\n他又在陆宁名字下方点了一笔。\n\n“这不代表你已洗清。宵禁入栏、错铃、栏门铰损坏另册照记。试用资格继续冻结，扣去的二点不退，余额四点。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-record-format",
      "state": "knows",
      "belief": "白绒的反应只能记录为闻到甜气后退半步、未碰槽，不能写成拒绝或指认。",
      "supersedes_fact_ids": [],
      "change": "乔穗修正对白绒反应的记录格式，避免将灵兽行为写成人类证词。",
      "source_evidence": "乔穗提笔便写：“白绒拒绝——”\n\n她顿住，看了看许苛，自己把后两个字划去。\n\n“白绒闻到甜气后退半步，未碰槽。”"
    },
    {
      "character_id": "lu-ning",
      "fact_id": "wrong-feed-route",
      "state": "knows",
      "belief": "甜根囊与燥阳谷是两个饲料问题，甜根囊经贺鸣手不能直接证明贺鸣向鹿栏投放燥阳谷。",
      "supersedes_fact_ids": [],
      "change": "陆宁明确区分甜根囊领用线索与燥阳谷投放问题。",
      "source_evidence": "贺鸣看向陆宁：“你想凭一袋甜根囊，说我往鹿栏投了燥阳谷？”\n\n“不能。”陆宁道，“两种饲料，两个问题。”"
    }
  ],
  "thread_changes": [
    {
      "change": "调查主线从单查陆宁私加燥阳谷，推进为三段证据链：甜根囊去向、贪食豚停留、暖槽错路时段重合。",
      "source_evidence": "“从今日起，不再只复查陆宁是否私加燥阳谷。”许苛道，“分三段查。甜根囊从领出到耗用去了哪里；贪食豚昨夜停在何处、停了多久；暖槽错路是否与受压时段重合。”"
    },
    {
      "change": "下一步复核要求贺鸣写清甜根囊离开账房后的完整路径；若记不清，则从豚栏残留查起。",
      "source_evidence": "许苛转向贺鸣：“下一次复核前，写清甜根囊离开账房后的完整路径。哪一道门，哪一段过道，何时开袋，余料如何处置。”\n\n贺鸣盯着压力石旁那只甲三袋，半晌才道：“若我记不清呢？”\n\n许苛将领用册合上。\n\n“那就去你的豚栏，从残留开始记。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗把留样分袋说成证物沐浴，被陆宁纠正为晾干、分袋，并因留样不合规被许苛罚重清压力石沟。",
      "source_evidence": "乔穗抱着三只留样袋站在桌边，小声道：“淡黄纤维在甲袋，草屑在乙袋，泥印刮样在丙袋。证物已经分开沐浴过了。”\n\n陆宁看了她一眼：“是晾干、分袋，没有沐浴。”\n\n“可我洗了两遍阵沟。”\n\n许苛头也不抬：“所以不合规。”"
    },
    {
      "change": "贺鸣用“顺手”概括甜根囊去向，被许苛、乔穗和陆宁用账册规则压回具体路径。",
      "source_evidence": "“账册也没让你量每一步。它只让你说明，一袋诱引饲料去了哪里。你写的是换栏，不是散失，不是遗落，更不是‘顺手’。”\n\n乔穗认真道：“领用册不认顺手。”\n\n陆宁补了一句：“也不认大概。”"
    }
  ],
  "new_constraints": [
    {
      "change": "乔穗必须重做甲袋编号，写明取样次序，并重新清理压力石沟。",
      "source_evidence": "“第一遍清出的纤维混了草屑，第二遍才分袋。甲袋重做编号，写明取样次序。压力石沟再清一遍。”"
    },
    {
      "change": "贺鸣不得补写旧记录，并需随时接受甜根囊去向核问。",
      "source_evidence": "“腿不记账，人记。”许苛在领用条目旁落下一笔，“去向待核。你随时听问，不得补写旧记录。”"
    },
    {
      "change": "本次纤维比对只能写气味、形态和留样位置，不能把相近写成同一。",
      "source_evidence": "“去压力石。只比气味、形态和留样位置。谁敢把相近写成同一，今日便陪乔穗再清一遍沟。”"
    },
    {
      "change": "陆宁宵禁入栏、错铃、栏门铰损坏仍另册记录；贡献点已扣二点不退，余额仍为四点。",
      "source_evidence": "“这不代表你已洗清。宵禁入栏、错铃、栏门铰损坏另册照记。试用资格继续冻结，扣去的二点不退，余额四点。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "甜根囊领用册确认贺鸣昨夜酉末领出一袋 sweet-root-pouch，名目为安置贪食豚换栏；贺鸣称已用过，但没有归还记录和耗用记录。",
    "贺鸣承认领过甜根囊，称只是为了让贪食豚离开自己的栏位，并否认向鹿栏投放燥阳谷；甜根囊去向仍待核。",
    "压力石阵沟淡黄纤维与未拆甜根囊外袋纤维气味相近、纤维形态相近，只能证明甜根囊外袋同类纤维曾接近此处，不能证明是谁带来或贪食豚一定压石。",
    "陆宁只完成一次许苛监督下的白绒单兽短促听息，确认白绒闻到甜气残留后呈现受热不适前的躲槽节奏，不是群体惊慌；听息诀仍不能读心、辨谎或追踪投料者。",
    "陆宁听息后耳闷、轻晕，今日不得再听，夜间独自整群听息禁令继续有效。",
    "许苛将调查拆成三段：甜根囊从领出到耗用去了哪里、贪食豚昨夜停在何处停了多久、暖槽错路是否与受压时段重合。",
    "陆宁试用资格继续冻结，扣去的二点贡献不退，余额四点；宵禁入栏、错铃、栏门铰损坏另册照记。",
    "乔穗已按沟段重清压力石阵沟，并重新分袋记录草屑、淡黄纤维等留样；其第一遍混装留样不合规已被纠正。",
    "许苛要求贺鸣下一次复核前写清甜根囊离开账房后的完整路径；若记不清，就从贺鸣的豚栏残留开始查。"
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
  "source_sha256": "f95945af889bd8850c15ad18b6098b026c7e8f59e4ba1c6a673beaacfa281aa7",
  "entity_changes": [
    {
      "change": "贺鸣正式承认昨夜私下用甜根囊把贪食豚从自己栏位引开，并在石缝边留甜根囊让其停留，仍否认投燥阳谷。",
      "source_evidence": "贺鸣看着被蹭乱的泥线，终于低下头：“昨夜是我私下用了甜根囊，把它从自己栏位引开。它赖着不走，我又在石缝边留了一点，让它停在那里。我只想让它别回来，没投燥阳谷。”"
    },
    {
      "change": "许苛将贺鸣行为登记为诱引饲料去向违规待处置，并记入后续证据对照，但暂不认定其投放燥阳谷或长期蓄意破坏。",
      "source_evidence": "许苛翻出处置册：“贺鸣，诱引饲料去向违规，待处置。私下引贪食豚停在压力石附近，记入后续对照。暂不认定你投放燥阳谷，也不扩作长期蓄意破坏。”"
    },
    {
      "change": "乔穗获得分栏登记复核路线、甜根残留点、压力石停留位置、蹭乱后泥印的记录任务。",
      "source_evidence": "乔穗只得在册上列出四项：复核路线、甜根残留点、压力石停留位置、蹭乱后泥印。"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "recovery",
      "change": "陆宁听息回声眩晕有所减轻但未解除，仍有耳中闷响。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛又看向陆宁：“你眩晕有所减轻，但未解除。明日白日，可在我监督下继续单兽低强度校验。夜间独自对整群听息，禁令照旧。”\n\n陆宁点头。耳中闷响仍在，只比早间远了些。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "ability",
      "change": "陆宁的听息诀使用边界维持为白日、许苛监督下、单兽低强度校验；仍未扩展到整群、读心、辨谎或追踪投料者。",
      "state_id": "beast-breath-listening",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛又看向陆宁：“你眩晕有所减轻，但未解除。明日白日，可在我监督下继续单兽低强度校验。夜间独自对整群听息，禁令照旧。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁夜间独自对整群听息的禁令继续有效。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛又看向陆宁：“你眩晕有所减轻，但未解除。明日白日，可在我监督下继续单兽低强度校验。夜间独自对整群听息，禁令照旧。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格继续冻结。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "he-ming",
      "fact_id": "sweet-root-lure",
      "state": "knows",
      "belief": "自己昨夜私下用甜根囊把贪食豚从自己栏位引开，并在石缝边留了一点让它停在那里；自己没有投燥阳谷。",
      "supersedes_fact_ids": [
        "sweet-root-lure"
      ],
      "change": "贺鸣不再成功隐瞒甜根囊引豚停留压力石附近一事，已当场承认。",
      "source_evidence": "贺鸣看着被蹭乱的泥线，终于低下头：“昨夜是我私下用了甜根囊，把它从自己栏位引开。它赖着不走，我又在石缝边留了一点，让它停在那里。我只想让它别回来，没投燥阳谷。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "sweet-root-fiber-sample",
      "state": "knows",
      "belief": "少量甜根囊残味足以诱使贪食豚靠近并停留压力石，但这只证明诱因可行，不证明昨夜压石对象有意破坏阵路。",
      "supersedes_fact_ids": [
        "sweet-root-fiber-sample"
      ],
      "change": "许苛将甜根囊纤维线索推进为甜根囊残味可诱使贪食豚停留压力石的已验证诱因。",
      "source_evidence": "许苛收起记时片：“少量甜根囊残味，足以诱使贪食豚靠近并停留压力石。只证诱因可行，不证明昨夜压石对象有意破坏阵路。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "suspects",
      "belief": "陆宁私加燥阳谷的嫌疑已被新证据削弱，但尚不能定结。",
      "supersedes_fact_ids": [
        "lu-ning-secret-yang-feed-review"
      ],
      "change": "许苛对陆宁私加燥阳谷的怀疑进一步削弱，但未最终解除。",
      "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trough-pressure-route",
      "state": "investigating",
      "belief": "下一步需要对照压力石持续受压时长、饲铃牌异常铃序、燥阳谷残留路线。",
      "supersedes_fact_ids": [
        "trough-pressure-route"
      ],
      "change": "许苛将后续调查明确推进为三表同案复核。",
      "source_evidence": "许苛将饲铃牌、记时片和留样袋分别收入木匣：“下一步，对照压力石持续受压时长、饲铃牌异常铃序、燥阳谷残留路线。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-hoofprint-count",
      "state": "investigating",
      "belief": "乔穗需要把复核路线、甜根残留点、压力石停留位置、蹭乱后泥印分开登记。",
      "supersedes_fact_ids": [
        "white-tuft-hoofprint-count"
      ],
      "change": "乔穗的泥印与路线记录任务更新为四项分栏登记。",
      "source_evidence": "乔穗只得在册上列出四项：复核路线、甜根残留点、压力石停留位置、蹭乱后泥印。"
    }
  ],
  "thread_changes": [
    {
      "change": "甜根囊诱使贪食豚停留压力石的证据链成立，但不证明昨夜压石对象有意破坏阵路。",
      "source_evidence": "许苛收起记时片：“少量甜根囊残味，足以诱使贪食豚靠近并停留压力石。只证诱因可行，不证明昨夜压石对象有意破坏阵路。”"
    },
    {
      "change": "贺鸣投放燥阳谷和长期蓄意破坏均暂未被认定。",
      "source_evidence": "许苛翻出处置册：“贺鸣，诱引饲料去向违规，待处置。私下引贪食豚停在压力石附近，记入后续对照。暂不认定你投放燥阳谷，也不扩作长期蓄意破坏。”"
    },
    {
      "change": "下一步调查固定为压力石持续受压时长、饲铃牌异常铃序、燥阳谷残留路线三表同案复核。",
      "source_evidence": "许苛扣上木匣：“明早，三表同案复核。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "贪食豚绕过贺鸣柔缰指令，只按甜味行动，直接验证甜根囊诱因。",
      "source_evidence": "贺鸣将柔缰绳引向贪食豚颈侧。贪食豚懒洋洋走出两步，木钳上的甜气一飘，它鼻子猛地贴地，圆身一拐，绕过柔缰牵出的弧线，直奔压力石。\n\n“左！”贺鸣喝道。\n\n贪食豚向右。\n\n“停！”\n\n它倒真停了，前蹄压住压力石边缘，腹侧贴上石面，鼻子还往木钳下拱。石下铜片轻响，许苛立即按住阵盘，截断槽路灵纹。"
    },
    {
      "change": "贪食豚蹭乱乔穗刚描好的泥线，造成乔穗需要重描并分栏记录。",
      "source_evidence": "乔穗扑过去描泥线。贪食豚闻见她袖口沾了残味，顺势一蹭，刚画出的半圈蹄印顿时糊成一团。\n\n她握着竹签僵了片刻：“它重走昨夜路径，还把脚迹收回去了。”\n\n“复核路线，不是昨夜路径；蹭乱，不是收回。”许苛道，“重描，分栏记。”"
    }
  ],
  "new_constraints": [
    {
      "change": "陆宁宵禁入栏、擅改铃序、栏门铰损坏责任仍另册保留。",
      "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
    },
    {
      "change": "陆宁已扣除的二点贡献不退，贡献点余额仍为四点，试用资格继续冻结。",
      "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
    },
    {
      "change": "复核只使用外袋残味，不开启新甜根囊，不允许暖槽起阵。",
      "source_evidence": "许苛合上册子：“现场复核。只用外袋残味，不开新料，不许暖槽起阵。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "贺鸣已承认昨夜私下用甜根囊把贪食豚从自己栏位引开，并在石缝边留了一点让它停在那里；他仍称自己没投燥阳谷。",
    "许苛已将贺鸣登记为诱引饲料去向违规待处置，并把私下引贪食豚停在压力石附近记入后续对照。",
    "现场复核已证明少量甜根囊残味足以诱使贪食豚靠近并停留压力石，但不证明昨夜压石对象有意破坏阵路。",
    "许苛暂不认定贺鸣投放燥阳谷，也不扩作长期蓄意破坏。",
    "许苛认为新证据削弱了陆宁私加燥阳谷的嫌疑，但还不能定结。",
    "陆宁宵禁入栏、擅改铃序、栏门铰损坏另册照记；二点贡献不退，余额四点，试用资格继续冻结。",
    "陆宁眩晕有所减轻但未解除，明日白日可在许苛监督下继续单兽低强度校验，夜间独自对整群听息禁令照旧。",
    "乔穗需要把复核路线、甜根残留点、压力石停留位置、蹭乱后泥印分开登记，并补上清栏工时。",
    "下一步为三表同案复核：压力石持续受压时长、饲铃牌异常铃序、燥阳谷残留路线。"
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
  "source_sha256": "01cbdb98abe31b82d0c553c5ce0fdbad6bc8dac8897a6b0d7a65321b1d57a42f",
  "entity_changes": [
    {
      "change": "乔穗将白绒避开鹿栏东槽的行为正式拆分记录为槽口甜气、暖料残留、拒食位置和蹄印转向，而非拟人化证词。",
      "source_evidence": "乔穗把脸板正，继续登记。她这回不再写白绒“拒绝认账”，只记东槽甜气较重、槽底有暖料残留、白绒在该槽前停步拒食，蹄印转向西槽。"
    },
    {
      "change": "受损栏门仍未修复，继续由临时横撑支撑。",
      "source_evidence": "受损栏门仍由临时横撑顶着，裂开的门铰垂在一侧。"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "ability",
      "change": "陆宁在白日、许苛监督下完成对白绒的一次单兽低强度听息校验，确认白绒为受热不适而非群体惊慌；听息诀边界仍限于验节奏，不能说明投料者或辨谎。",
      "state_id": "beast-breath-listening",
      "state_action": "set",
      "stage_after": "炼气二层",
      "source_evidence": "“受热不适。”陆宁退开半步，“不是群体惊慌。只能验节奏，不能说明谁投料，也不能验谁说了假话。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "recovery",
      "change": "陆宁听息回声眩晕部分恢复：耳鸣比昨日减轻，但转身仍晕，未解除。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "source_evidence": "许苛检查陆宁耳后：“耳鸣如何？”\n\n“比昨日轻。转身仍晕。”\n\n“回声眩晕只记部分恢复，未解除。夜间独自整群听息禁令照旧。封耳条继续戴，今日不得再校验第二只。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁夜间独自整群听息禁令继续有效，封耳条继续佩戴，且当日不得再校验第二只灵兽。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "source_evidence": "“回声眩晕只记部分恢复，未解除。夜间独自整群听息禁令照旧。封耳条继续戴，今日不得再校验第二只。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格冻结不解除。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "source_evidence": "陆宁问：“试用冻结呢？”\n\n“不解。二点贡献不退，余额四点。宵禁、错铃另册。栏门铰未修，修理与赔偿照旧。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "xu-ke",
      "fact_id": "trough-pressure-route",
      "state": "knows",
      "belief": "三表首次对照显示压力石持续受压覆盖异常三声铃后的暖槽偏移，残留路线与暖槽偏向鹿栏的阵路一致；目前只能说明暖料有错送路径。",
      "supersedes_fact_ids": [
        "trough-pressure-route"
      ],
      "change": "许苛完成压力石时长、饲铃牌铃序和燥阳谷残留路线的三表对照，并将调查从待对照推进为已确认错送路径吻合。",
      "source_evidence": "许苛核过三处：“压力石持续受压，覆盖异常三声铃后的暖槽偏移。残留路线，也与暖槽偏向鹿栏的阵路一致。到这里，只能说明暖料有错送路径。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "investigating",
      "belief": "陆宁私加燥阳谷的旧批注已改为尚无直接投料证据，后续需核定暖槽出料数、鹿栏残留量和原料库登记量。",
      "supersedes_fact_ids": [
        "lu-ning-secret-yang-feed-review"
      ],
      "change": "许苛将对陆宁私加燥阳谷的旧判断降级为尚无直接投料证据、待份量与路线继续核定。",
      "source_evidence": "他收起记录板，当场改了旧案上的批注：“陆宁私加燥阳谷，改为尚无直接投料证据。待暖槽出料数、鹿栏残留量、原料库登记量核定。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trial-qualification-result",
      "state": "knows",
      "belief": "陆宁试用冻结不解，二点贡献不退，余额四点，宵禁和错铃另册，栏门铰未修且修理赔偿照旧。",
      "supersedes_fact_ids": [
        "trial-qualification-result"
      ],
      "change": "许苛明确陆宁相关处罚后果全部保留。",
      "source_evidence": "陆宁问：“试用冻结呢？”\n\n“不解。二点贡献不退，余额四点。宵禁、错铃另册。栏门铰未修，修理与赔偿照旧。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-record-format",
      "state": "knows",
      "belief": "白绒避槽行为不能写成拟人化证词，正式记录应写东槽甜气、槽底暖料残留、拒食位置和蹄印转向。",
      "supersedes_fact_ids": [
        "white-tuft-record-format"
      ],
      "change": "乔穗已按许苛要求把白绒避槽说法改成可复核记录格式。",
      "source_evidence": "乔穗把脸板正，继续登记。她这回不再写白绒“拒绝认账”，只记东槽甜气较重、槽底有暖料残留、白绒在该槽前停步拒食，蹄印转向西槽。"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-hoofprint-count",
      "state": "knows",
      "belief": "白绒前蹄停在东槽外两尺后绕向西侧净槽，中途未回东槽。",
      "supersedes_fact_ids": [
        "white-tuft-hoofprint-count"
      ],
      "change": "乔穗补上白绒东槽外停步并绕向西槽的踏痕记录。",
      "source_evidence": "乔穗沉默片刻，把“不肯签字”划掉，拆成三行。写完又去取泥印拓纸，补上白绒前蹄停在东槽外两尺、绕向西侧净槽的痕迹。她刚想在末尾添一句“态度坚决”，瞥见那列新字，只得改成“中途未回东槽”。"
    },
    {
      "character_id": "lu-ning",
      "fact_id": "wrong-feed-route",
      "state": "knows",
      "belief": "压力石受压覆盖异常三声铃和暖槽未复位时段，残留路线与鹿栏东槽错送路径吻合。",
      "supersedes_fact_ids": [
        "wrong-feed-route"
      ],
      "change": "陆宁参与确认压力石受压时段覆盖异常铃序与暖槽未复位时段。",
      "source_evidence": "“压力石受压到何时？”乔穗问。\n\n“子初三刻。”陆宁道，“覆盖三声铃，也覆盖暖槽未复位的时段。”"
    },
    {
      "character_id": "he-ming",
      "fact_id": "sweet-root-lure",
      "state": "knows",
      "belief": "许苛只认定贺鸣甜根囊时间接近压力石受压诱因，不能证明贺鸣投放燥阳谷。",
      "supersedes_fact_ids": [
        "sweet-root-lure"
      ],
      "change": "贺鸣听到许苛明确三表目前不能证明他投放燥阳谷。",
      "source_evidence": "“表上也没写有关。”许苛指向空着的份量栏，“三张表不替你背锅，也不替陆宁背。时间若对不上，你的甜根囊只算去向违规；时间若对得上，也只能证明压石诱因与你相近，不能证明你投了燥阳谷。”"
    }
  ],
  "thread_changes": [
    {
      "change": "三表复核已启动并合成同一张复核表，裁定标准限定为时辰、铃次、槽位和份量。",
      "source_evidence": "许苛压上镇纸：“合成一张复核表。只对时辰、铃次、槽位、份量。谁看着可疑，不入表。”"
    },
    {
      "change": "压力石受压、异常三声铃和暖槽偏鹿栏残留路线已在时间与阵路上对齐，但只推进到暖料有错送路径。",
      "source_evidence": "许苛核过三处：“压力石持续受压，覆盖异常三声铃后的暖槽偏移。残留路线，也与暖槽偏向鹿栏的阵路一致。到这里，只能说明暖料有错送路径。”"
    },
    {
      "change": "陆宁擅改安抚铃被拆分为异常三声铃之后的单独违规，不再作为异常三声铃起点。",
      "source_evidence": "“这声是你的违规。”许苛道，“宵禁后入栏、擅改安抚铃，照记。却不是异常三声铃的起点。”"
    },
    {
      "change": "下一步调查转入燥阳谷份量缺口核定，需开原料库册。",
      "source_evidence": "“明日开原料库册。我要看错路那一刻，究竟少了多少燥阳谷。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗将白绒避槽拟人化为不肯签字，许苛因此在复核表增加“不得写感想”栏。",
      "source_evidence": "乔穗探头念道：“不得写感想。”\n\n“正是。”\n\n“可它确实不认这口锅。”"
    },
    {
      "change": "乔穗试图继续给白绒行为加拟人化评语，但被“不得写感想”栏迫使改成客观记录。",
      "source_evidence": "她刚想在末尾添一句“态度坚决”，瞥见那列新字，只得改成“中途未回东槽”。"
    },
    {
      "change": "乔穗因表格禁写感想而把白绒行为记录为不作责任判断。",
      "source_evidence": "乔穗看了看许苛新添的那一列，老实写下：白绒接近无燥阳谷气味的袖侧，未进食；此举不作责任判断。"
    }
  ],
  "new_constraints": [
    {
      "change": "复核表只能按时辰、铃次、槽位、份量记录，不按人看起来可疑定责。",
      "source_evidence": "许苛压上镇纸：“合成一张复核表。只对时辰、铃次、槽位、份量。谁看着可疑，不入表。”"
    },
    {
      "change": "陆宁当日听息校验限制为白日、单兽、低强度，只校验白绒，耳鸣加重即停。",
      "source_evidence": "许苛特意让陆宁站在横撑外：“白日，单兽，低强度。只校验白绒。若耳鸣加重，立刻停。”"
    },
    {
      "change": "陆宁试用冻结、扣点、宵禁、错铃、栏门修理与赔偿责任继续保留；贡献点余额仍为四点。",
      "source_evidence": "陆宁问：“试用冻结呢？”\n\n“不解。二点贡献不退，余额四点。宵禁、错铃另册。栏门铰未修，修理与赔偿照旧。”"
    },
    {
      "change": "陆宁回声眩晕未解除，夜间独自整群听息禁令继续有效，封耳条继续戴，今日不得再校验第二只。",
      "source_evidence": "“回声眩晕只记部分恢复，未解除。夜间独自整群听息禁令照旧。封耳条继续戴，今日不得再校验第二只。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "三表首次对照已完成：压力石持续受压覆盖异常三声铃后的暖槽偏移，残留路线与暖槽偏向鹿栏的阵路一致，但目前只能说明暖料有错送路径。",
    "许苛已将“陆宁私加燥阳谷”改为尚无直接投料证据，下一步需核定暖槽出料数、鹿栏残留量、原料库登记量。",
    "陆宁擅改安抚铃发生在鹿群躁动之后，仍是宵禁后入栏、擅改安抚铃的单独违规，但不是异常三声铃起点。",
    "乔穗已把白绒避槽补记为东槽甜气较重、槽底暖料残留、白绒拒食位置、蹄印转向西槽，并编号东槽残留袋、踏痕拓纸和甜气位置。",
    "陆宁完成一次白日、许苛监督下、单兽低强度听息校验，确认白绒受热不适而非群体惊慌；听息诀仍不能说明谁投料或谁说谎。",
    "陆宁 breath-echo-vertigo 仅部分恢复：耳鸣比昨日轻，转身仍晕，未解除；solo-night-listening-ban 继续有效，封耳条继续戴。",
    "陆宁试用资格仍冻结，二点贡献不退，余额四点；宵禁、错铃另册，栏门铰未修，修理与赔偿照旧。",
    "贺鸣甜根囊与压力石受压时间相近，只能证明压石诱因与他相近，不能证明他投放燥阳谷；其甜根囊去向违规仍待处置。",
    "下一章明日开原料库册，核查错路那一刻究竟少了多少燥阳谷。"
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
  "source_sha256": "7be784b58fb6ed76eec154747549338a3307ae55d7f5d754e713b03263428ddf",
  "entity_changes": [
    {
      "change": "受损栏门仍未修复，继续由临时横木支撑。",
      "source_evidence": "鹿栏东槽旁搭了临时称量台。受损的栏门仍由两根横木撑住，裂开的铰座露在外面，没人去碰。"
    },
    {
      "change": "乔穗完成对东槽残留、踏痕拓纸、甜气位置与白绒避槽行为的正式化记录，并被安排继续重抄复称记录、筛净残留袋和清理鹿栏。",
      "source_evidence": "乔穗刚松开抱着的残留袋，许苛便把两叠纸递给她：“复称记录重抄一份，三只袋重新筛净。鹿栏清理也归你。”"
    }
  ],
  "relationship_changes": [],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "ability",
      "change": "陆宁本章未再次运转听息诀，只依据昨日白日、监督下、单兽低强度校验所得辅助判断白绒受热不适；听息诀仍不能判断投料者。",
      "state_id": "beast-breath-listening",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛看向陆宁：“只准用昨日校验所得，不得再运诀。”\n\n陆宁点头。他没有凝神听取整栏兽息，只依白绒昨日单兽低强度校验的记录，对照眼前起伏的腹侧。\n\n“短促，浅，咽前停顿。是受热不适。不是群体惊慌。”\n\n乔穗问：“翻到账上怎么写？”\n\n“东槽暖料残留位置，与受热不适、拒食位置相合。”陆宁顿了顿，“不能写谁投的。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "injury",
      "change": "陆宁回声眩晕仍未解除，转身稍快即耳鸣、站立偏移，封耳条继续佩戴。",
      "state_id": "breath-echo-vertigo",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他说完起身想看秤盘，转得稍快，耳内立刻嗡鸣，脚下偏了半步。乔穗伸手扶住称量台，没去扶他，只把挡路的残留袋先挪开。\n\n许苛皱眉：“坐回去。今日不得再校验第二只。”\n\n陆宁缓了两息，依言坐下。封耳条仍贴得严实，眩晕并未因账目对上便少一分。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁夜间不得独自对整群使用听息诀的禁令继续有效，且回声眩晕未获许苛确认解除。",
      "state_id": "solo-night-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他又指了指陆宁耳后的封耳条：“回声眩晕未由我确认解除。夜间不得独自对整群使用听息诀，仍然有效。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格继续冻结。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛将另一册推到他面前：“私投燥阳谷暂不成立，不等于宵禁后入栏无事。你擅改一次安抚铃，记录保留；阻栏处置不当，栏门铰损坏，修理与赔偿保留；已扣二点贡献不退，余额四点；试用资格继续冻结。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "investigating",
      "belief": "燥阳谷份量缺口与异常铃后暖槽出料相符，鹿栏残留及阵路损耗可核；现有事实暂不支持陆宁私自投放燥阳谷，但尚未结案。",
      "supersedes_fact_ids": [
        "lu-ning-secret-yang-feed-review"
      ],
      "change": "许苛将陆宁名下旧批注进一步改为暂不支持陆宁私自投放燥阳谷，但保留尚未结案。",
      "source_evidence": "许苛提笔，将旧批注划去，重写：“燥阳谷份量缺口与异常铃后暖槽出料相符，鹿栏残留及阵路损耗可核。现有事实暂不支持陆宁私自投放燥阳谷，尚未结案。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trough-pressure-route",
      "state": "knows",
      "belief": "异常三声铃后暖槽出料四升，鹿栏东槽及偏送阵路复称三升八合，二合为沿路损耗，库中短少四升与该次出料相符。",
      "supersedes_fact_ids": [
        "trough-pressure-route"
      ],
      "change": "许苛通过库册、出料与残留复称确认燥阳谷四升缺口可与错路出料核算相符。",
      "source_evidence": "许苛将算盘拨到最后一位：“异常三声铃后，暖槽出料四升。鹿栏东槽及偏送阵路复称三升八合。二合为沿路损耗。库中短少四升，与该次出料相符。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "sweet-root-lure-review",
      "state": "investigating",
      "belief": "贺鸣领用诱引饲料不记耗用并将贪食豚引到压力石附近，压力石持续受压时段与错路重合；此事需与铃序及受压记录合并另行处置，但不等同于认定他另行投放燥阳谷。",
      "supersedes_fact_ids": [],
      "change": "许苛保留贺鸣甜根囊去向违规与压力石受压时段的合并核查。",
      "source_evidence": "“不能。”许苛道，“四升燥阳谷可由错路解释，只说明暂不能认定有人另行投料。你领用诱引饲料不记耗用，又将贪食豚引到压力石附近，压力石持续受压的时段与错路重合。两件事不是一件罪，也不是毫无关系。下一步合并铃序与受压记录，另行处置。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-record-format",
      "state": "knows",
      "belief": "白绒避开东槽的记录必须写成槽底暖料残留、停步位置、未进食与蹄印转向西槽，不能写成拟人化拒绝签收。",
      "supersedes_fact_ids": [
        "white-tuft-record-format"
      ],
      "change": "乔穗把对白绒拒食的拟人化写法改成槽位、残留和蹄印方向记录。",
      "source_evidence": "乔穗立即改口：“东槽一号，槽底暖料残留。白绒于东槽前三尺停步，未进食，蹄印转向西槽。”"
    }
  ],
  "thread_changes": [
    {
      "change": "调查从确认错送路径推进到燥阳谷四升缺口可由异常铃后暖槽错路出料解释。",
      "source_evidence": "许苛将算盘拨到最后一位：“异常三声铃后，暖槽出料四升。鹿栏东槽及偏送阵路复称三升八合。二合为沿路损耗。库中短少四升，与该次出料相符。”"
    },
    {
      "change": "许苛将甜根囊去向、压力石受压时段、异常铃序和燥阳谷缺口并入下一步合案材料。",
      "source_evidence": "廊外，临时横撑被风吹得轻响。许苛将甜根囊去向、压力石受压时段、异常铃序与四升燥阳谷缺口并排夹入同一册，压上木签。\n\n“明日按铃次合案。谁让压力石压住，谁让暖槽错路，各算各的。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗把白绒避槽写成“拒绝签收”，被许苛纠正为证据化记录。",
      "source_evidence": "乔穗抱着三只编号残留袋挤到案前，把最上面一只放下：“东槽一号，白绒拒绝签收。”\n\n许苛笔尖停住。\n\n乔穗立即改口：“东槽一号，槽底暖料残留。白绒于东槽前三尺停步，未进食，蹄印转向西槽。”"
    },
    {
      "change": "乔穗再次险些把白绒拒食写成拟人化拒绝，被迫改成停步、未进食、进食位置和行进方向。",
      "source_evidence": "乔穗的笔已经落下：“白绒再次拒绝在东槽——”\n\n她停了停，自己划掉后半句，改成：“东槽前停步一次，未进食；西槽进食。行进方向与昨日踏痕相合。”"
    },
    {
      "change": "燥阳谷四升缺口被喜剧化为“没有凭空长腿”，但正式记录仍写食槽阵偏送。",
      "source_evidence": "乔穗抱起筛过的垫草：“所以那四升没有凭空长腿。”\n\n“阵路替它走了。”陆宁道。\n\n许苛合上小秤：“写食槽阵偏送，不写谷有腿。”"
    }
  ],
  "new_constraints": [
    {
      "change": "陆宁私投燥阳谷暂不成立，但宵禁后入栏、擅改一次安抚铃、栏门铰损坏、修理赔偿、扣点和试用资格冻结全部保留。",
      "source_evidence": "许苛将另一册推到他面前：“私投燥阳谷暂不成立，不等于宵禁后入栏无事。你擅改一次安抚铃，记录保留；阻栏处置不当，栏门铰损坏，修理与赔偿保留；已扣二点贡献不退，余额四点；试用资格继续冻结。”"
    },
    {
      "change": "陆宁当日不得再校验第二只灵兽。",
      "source_evidence": "许苛皱眉：“坐回去。今日不得再校验第二只。”"
    },
    {
      "change": "乔穗需重抄复称记录、重新筛净三只残留袋并清理鹿栏。",
      "source_evidence": "乔穗刚松开抱着的残留袋，许苛便把两叠纸递给她：“复称记录重抄一份，三只袋重新筛净。鹿栏清理也归你。”"
    }
  ],
  "resolved_constraints": [],
  "next_chapter_inputs": [
    "燥阳谷缺口已核定：异常三声铃后暖槽出料四升，鹿栏东槽及偏送阵路复称三升八合，二合为沿路损耗，库中短少四升与该次出料相符。",
    "许苛已将陆宁私加燥阳谷旧批注改为：现有事实暂不支持陆宁私自投放燥阳谷，但尚未结案。",
    "贺鸣甜根囊领用后未记耗用、诱引贪食豚停在压力石附近，且压力石持续受压时段与错路重合；下一步需合并铃序与受压记录另行处置。",
    "陆宁试用资格继续冻结，已扣二点贡献不退，余额四点；宵禁后入栏、擅改一次安抚铃、栏门铰损坏、修理与赔偿责任均保留。",
    "陆宁回声眩晕未由许苛确认解除，封耳条继续佩戴，夜间不得独自对整群使用听息诀仍然有效。",
    "陆宁本章只依据昨日白日、许苛监督下、单兽低强度校验记录辅助判断白绒受热不适，没有再次运诀，也不能判断投料者。",
    "受损栏门仍由两根横木临时支撑，裂开的铰座未修复。",
    "乔穗需重抄复称记录、筛净三只残留袋并清理鹿栏；她的白绒记录已被正式化为残留重量、蹄印方向、拒食位置和进食位置。",
    "下一章可从许苛将甜根囊去向、压力石受压时段、异常铃序与四升燥阳谷缺口按铃次合案开始。"
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
  "source_sha256": "a0514d9ca35e442043c235e99fe340d26bce633946188beb5511bbb13b2fcbf8",
  "entity_changes": [
    {
      "change": "贺鸣被许苛正式记过一次，并被安排清理压力石周边、安装防豚隔栏、赔工照册核算。",
      "source_evidence": "许苛落下一笔：“私用诱引饲料，漏记耗用，诱使贪食豚持续停留压力石，造成食槽阵错路条件。记过一次，清理压力石周边，安装防豚隔栏，赔工照册核算。”"
    },
    {
      "change": "食槽阵压力石区新增防豚隔栏与铃序复核牌，空槽初试通过但最终验收未完成。",
      "source_evidence": "临时横撑挡住隔栏右脚的位置，他们不能挪横木，只得把隔栏向外移半尺，再加一道斜挡。贺鸣扛桩、压脚、收绳，肩上衣料很快湿透。许苛逐项验过，才准乔穗把铃序复核牌钉在阵台正面：一声开冷槽，二声换栏，三声启暖槽；压力石受压异常，先停铃复核。"
    },
    {
      "change": "受损栏门铰仍未修复，横撑继续顶在原处。",
      "source_evidence": "他转头看了一眼裂开的栏门铰。横撑仍顶在原处，铰座上的裂缝半点没少。"
    }
  ],
  "relationship_changes": [
    {
      "change": "许苛对贺鸣的责任边界作出划分：坐实诱引贪食豚压石造成错路条件，但不认定贺鸣投放燥阳谷或长期毁阵。",
      "source_evidence": "“记录里也没写是你放的。”许苛道，“甜根囊解释压石，不解释燥阳谷由谁投入暖槽。现有材料不能认定你亲手投放，更不能写成你长期蓄意毁阵。”"
    },
    {
      "change": "许苛明确陆宁仍需承担栏门后续修理工时与赔偿，并写入条件审查。",
      "source_evidence": "“食槽阵修了，栏门没修。陆宁，后续修理工时与赔偿写入你的条件审查。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "ability",
      "change": "陆宁的听息诀稳定在单兽低强度校验范围内，可分辨白绒当前平稳、未受热不适，以及受远栏惊动导致的短促应激；未扩听整群。",
      "state_id": "beast-breath-listening",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "他收诀：“白绒当前平稳。没有受热不适。方才短促，是受远栏惊动。”\n\n“远栏呢？”许苛问。\n\n陆宁没有再放开听息：“我不听整群。只从眼前踏蹄与白绒应激变化判断，远处有群体惊慌迹象，不能据此多说。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "recovery",
      "change": "陆宁的听息回声眩晕经停止整群听息、使用封耳条、休养及白日监督下单兽低强度校验后由许苛确认解除。",
      "state_id": "breath-echo-vertigo",
      "state_action": "resolve",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "许苛在伤势册上写道：“经停止整群听息、使用封耳条、休养及白日监督下单兽低强度校验，听息回声眩晕解除。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁夜间不得独自对整群使用听息诀的旧禁令结束。",
      "state_id": "solo-night-listening-ban",
      "state_action": "resolve",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁新增自今日起两日内不得对整群使用听息诀的限制；单兽低强度使用仍须报备。",
      "state_id": "two-day-group-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格继续冻结，临时饲兽牌审查留到明日。",
      "state_id": "trial-qualification-freeze",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“你的试用冻结不解除。”许苛合上伤势册，将食槽阵初试记录、栏门赔偿单和责任卷并排放好，“明日验阵、宣告燥阳谷责任结论，再审临时饲兽牌。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "xu-ke",
      "fact_id": "sweet-root-lure-review",
      "state": "knows",
      "belief": "贺鸣私用诱引饲料、漏记耗用，诱使贪食豚持续停留压力石，造成食槽阵错路条件，应记过并承担清理、安装防豚隔栏和赔工。",
      "supersedes_fact_ids": [
        "sweet-root-lure-review"
      ],
      "change": "许苛将贺鸣甜根囊与压力石受压的核查转为正式认定和处置。",
      "source_evidence": "许苛落下一笔：“私用诱引饲料，漏记耗用，诱使贪食豚持续停留压力石，造成食槽阵错路条件。记过一次，清理压力石周边，安装防豚隔栏，赔工照册核算。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "he-ming-not-yang-feed-caster",
      "state": "knows",
      "belief": "现有材料不能认定贺鸣亲手投放燥阳谷，也不能写成贺鸣长期蓄意毁阵。",
      "supersedes_fact_ids": [],
      "change": "许苛明确贺鸣责任不扩展到投放燥阳谷或长期毁阵。",
      "source_evidence": "“记录里也没写是你放的。”许苛道，“甜根囊解释压石，不解释燥阳谷由谁投入暖槽。现有材料不能认定你亲手投放，更不能写成你长期蓄意毁阵。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "investigating",
      "belief": "错路时段与四升缺口相合，现有事实进一步不支持陆宁私加燥阳谷，但尚未最终验收，试用资格继续冻结。",
      "supersedes_fact_ids": [],
      "change": "许苛进一步削弱陆宁私加燥阳谷嫌疑，但仍未最终结案。",
      "source_evidence": "许苛盖下小印，又看向陆宁：“错路时段与四升缺口相合，现有事实进一步不支持你私加燥阳谷。但尚未最终验收，你的试用资格继续冻结。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "tool-sweet-root-contamination",
      "state": "knows",
      "belief": "施工器具受甜根气味污染，贪食豚沿污染器具移动，妨碍隔栏定位；清洗后贪食豚未再跟随施工路线。",
      "supersedes_fact_ids": [],
      "change": "乔穗将贪食豚跟随施工路线的现象正式改记为工具甜根气味污染。",
      "source_evidence": "她立即划掉前一句，改记：“施工器具受甜根气味污染，贪食豚沿污染器具移动，妨碍隔栏定位。”"
    },
    {
      "character_id": "lu-ning",
      "fact_id": "beast-breath-limited-scope",
      "state": "knows",
      "belief": "本次听息只可辨节奏，不得扩听，不得借兽息判断谁投料或谁说谎。",
      "supersedes_fact_ids": [],
      "change": "陆宁明确遵守许苛划定的听息诀使用边界。",
      "source_evidence": "“你先前已停止整群听息，休养数日，也用过一条封耳条。今日只做单兽低强度校验。”他指向远栏，“不得扩听，不得借兽息判断谁投料、谁说谎。”\n\n陆宁盘膝坐在栏外：“只辨节奏。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trough-array-initial-test",
      "state": "knows",
      "belief": "食槽阵空槽初试中，暖槽按原定阵路滑向豚栏外接料位，没有偏向云蹄鹿东槽；初试通过，最终验收明日做。",
      "supersedes_fact_ids": [],
      "change": "许苛掌握食槽阵修复后的初试结果，但最终验收仍未完成。",
      "source_evidence": "空槽试送时，许苛亲自拨动饲铃牌。\n\n一声，冷槽阵纹亮起。二声，分槽轮转。三声之后，暖槽木斗沿原定阵路滑向豚栏外的接料位，没有偏向云蹄鹿东槽。"
    }
  ],
  "thread_changes": [
    {
      "change": "压力石受压、异常三声铃、燥阳谷出料复称与甜根囊去向已被许苛按同一时辰线合并。",
      "source_evidence": "第一张，压力石自亥初二刻起持续受压。第二张，亥初三刻出现异常三声铃，暖槽阵路偏向鹿栏。第三张，燥阳谷出料四升，鹿栏与偏送阵路复称三升八合，余二合为沿路损耗。第四张，贺鸣于亥初前领走甜根囊一袋，未记耗用，残囊留在压力石旁。\n\n许苛用朱笔将四处时辰连成一线：“贺鸣，复述。”"
    },
    {
      "change": "食槽阵错接阵槽被拆修，导槽与压力石被校正，防豚隔栏因横撑阻挡改位安装。",
      "source_evidence": "器具归净，施工重新开始。贺鸣先铲掉压力石边凝结的泥和甜根碎屑，再拆开偏接阵槽。陆宁不能猛转身搬重件，便沿阵纹逐段报位。\n\n“左侧导槽高半指。”\n\n贺鸣垫平槽脚。\n\n“压力石回弹迟一息。”\n\n乔穗清出石缝细砂，贺鸣重新校紧承簧。"
    },
    {
      "change": "食槽阵空槽初试显示暖槽未再偏向云蹄鹿东槽，初试通过，最终验收推至明日。",
      "source_evidence": "“初试通过，最终验收明日做。”"
    },
    {
      "change": "下一章将进行验阵、燥阳谷责任结论宣告和临时饲兽牌再审。",
      "source_evidence": "“你的试用冻结不解除。”许苛合上伤势册，将食槽阵初试记录、栏门赔偿单和责任卷并排放好，“明日验阵、宣告燥阳谷责任结论，再审临时饲兽牌。”"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗一度把贪食豚跟随贺鸣施工记录成监督赔工，后被陆宁纠正为追甜根味。",
      "source_evidence": "乔穗提笔：“贪食豚监督赔工，态度严谨。”\n\n陆宁扶住阵台，避免转身过快：“它追的是甜根味，不是工时。”"
    },
    {
      "change": "贺鸣因自己诱引贪食豚的违规行为，被许苛用一句话指定负责清洗工具并把猪挡在压力石外。",
      "source_evidence": "贺鸣看着一筐工具：“都洗？”\n\n“会引猪的人，负责把猪挡在外面。”"
    },
    {
      "change": "乔穗把贪食豚清洗后未再跟随施工路线精确记为三息，因为第四息贪食豚去找吃的，不归工具污染记录。",
      "source_evidence": "乔穗在器具栏后添了一句：“清洗后三息内，贪食豚未再跟随施工路线。”\n\n“为何只记三息？”贺鸣问。\n\n“第四息它去找吃的了。那不归工具管。”"
    }
  ],
  "new_constraints": [
    {
      "change": "压力石区以后只准使用无诱引气味工具。",
      "source_evidence": "许苛扫过记录：“停工。器具全洗。以后压力石区只准用无诱引气味工具。”"
    },
    {
      "change": "陆宁自今日起两日内不得对整群使用听息诀；单兽低强度使用仍须报备。",
      "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
    },
    {
      "change": "陆宁的后续栏门修理工时与赔偿将写入临时饲兽牌条件审查。",
      "source_evidence": "“食槽阵修了，栏门没修。陆宁，后续修理工时与赔偿写入你的条件审查。”"
    },
    {
      "change": "最终验收前，每一声饲铃都必须有人核对槽位。",
      "source_evidence": "“先去看。最终验收前，任何一声铃都要有人对槽位。”"
    }
  ],
  "resolved_constraints": [
    {
      "change": "陆宁听息回声眩晕解除。",
      "source_evidence": "许苛在伤势册上写道：“经停止整群听息、使用封耳条、休养及白日监督下单兽低强度校验，听息回声眩晕解除。”"
    },
    {
      "change": "陆宁夜间不得独自对整群使用听息诀的旧禁令结束。",
      "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
    }
  ],
  "next_chapter_inputs": [
    "贺鸣已被正式认定私用诱引饲料、漏记耗用，诱使贪食豚持续停留压力石并造成食槽阵错路条件；处罚为记过一次、清理压力石周边、安装防豚隔栏、赔工照册核算。",
    "许苛明确现有材料不能认定贺鸣亲手投放燥阳谷，也不能写成贺鸣长期蓄意毁阵。",
    "许苛认为错路时段与四升缺口相合，现有事实进一步不支持陆宁私加燥阳谷，但尚未最终验收，责任结论留待下一章宣告。",
    "食槽阵已完成错接阵槽拆修、导槽垫平、压力石校紧、防豚隔栏和铃序复核牌安装；空槽初试显示暖槽按原定阵路滑向豚栏外接料位，没有偏向云蹄鹿东槽。",
    "食槽阵仅为初试通过，最终验收明日做；最终验收前任何一声铃都要有人对槽位。",
    "施工器具甜根气味污染已被乔穗记录并清洗；压力石区以后只准使用无诱引气味工具。",
    "陆宁听息回声眩晕已解除，夜间不得独自对整群使用听息诀的旧禁令结束。",
    "陆宁新增两日内不得对整群使用听息诀的限制；单兽低强度使用仍须报备。",
    "陆宁试用冻结仍不解除；下一章需验阵、宣告燥阳谷责任结论，再审临时饲兽牌。",
    "陆宁已扣二点贡献不退，余额四点；宵禁后入栏、擅改一次安抚铃另册仍在。",
    "栏门铰仍裂着，横撑仍顶在原处；陆宁后续修理工时与赔偿写入条件审查。"
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
  "source_sha256": "dce137a882885f53c9625c584528552749b34746c910ceec70b558d630ca5ac7",
  "entity_changes": [
    {
      "change": "食槽阵完成最终验收并通过，空槽试送无偏移，暖槽路线恢复，压力石、防豚隔栏和铃序复核牌均确认可用。",
      "source_evidence": "许苛逐项检查槽温、出口、隔栏木楔和复核牌，最后在验收册上盖下印章。\n\n“空槽试送无偏移，暖槽恢复原定路线；压力石校紧，防豚隔栏可阻持续压石；铃序复核牌可用。食槽阵，验收通过。”"
    },
    {
      "change": "陆宁领取御兽苑带条件临时饲兽牌。",
      "source_evidence": "许苛取出一块窄长木牌。牌正面烙着“御兽苑临时饲兽”，背面却密密刻了数行小字。\n\n“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
    },
    {
      "change": "受损鹿栏门铰仍未修复，继续由临时横撑支撑。",
      "source_evidence": "棚外忽然传来木头轻响。\n\n临时横撑在风里顶住裂铰，栏门歪了半寸，又被撑回原处。"
    }
  ],
  "relationship_changes": [
    {
      "change": "乔穗与陆宁在临时牌条件下形成明确分工：陆宁负责兽息对照与铃序复核，乔穗负责槽位、气味、踏痕、拒食、进食记录和清栏归档。",
      "source_evidence": "乔穗翻过一页，认真改道：“陆宁负责兽息对照与铃序复核。我负责槽位、气味、踏痕、拒食与进食记录，兼清栏归档。”\n\n“这条可写。”"
    },
    {
      "change": "许苛明确不会因白绒靠近陆宁而放宽陆宁的违规和考核条件。",
      "source_evidence": "“宵禁入栏、擅改一次安抚铃，记录保留。栏门铰修理与赔偿，写入条件。后续考核仍看铃序、份量和损坏。白绒靠近你，只能记气味、蹄印和进食位置，不能替你抵一条违规。”"
    }
  ],
  "cultivation_changes": [
    {
      "subject_id": "lu-ning",
      "kind": "ability",
      "change": "陆宁的听息诀继续限定在单兽低强度校验范围内，本章实际确认可通过白绒呼吸判断无受热急促滞顿、无群体惊慌乱拍，未扩听整群，也未追索气味来处。",
      "state_id": "beast-breath-listening",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "细缓的呼吸混着咀嚼声传来，没有受热时的急促滞顿，也没有群体惊慌时一呼带一呼的乱拍。陆宁只听了三息便收诀，既不牵连旁边鹿群，也不追索气味来处。"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁试用资格冻结解除，改为通过条件审查。",
      "state_id": "trial-qualification-freeze",
      "state_action": "resolve",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
    },
    {
      "subject_id": "lu-ning",
      "kind": "restriction",
      "change": "陆宁两日内不得对整群使用听息诀的限制继续生效，单兽低强度校验仍须报备。",
      "state_id": "two-day-group-listening-ban",
      "state_action": "set",
      "stage_after": "炼气二层",
      "from_stage": "",
      "to_stage": "",
      "prerequisites": [],
      "costs": [],
      "new_limits": [],
      "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
    }
  ],
  "resource_changes": [],
  "knowledge_changes": [
    {
      "character_id": "xu-ke",
      "fact_id": "lu-ning-secret-yang-feed-review",
      "state": "knows",
      "belief": "现有证据不能证明陆宁私加燥阳谷；燥阳谷是经食槽阵错路进入鹿栏，先前对陆宁私自投放燥阳谷的误信已被纠正。",
      "supersedes_fact_ids": [
        "lu-ning-secret-yang-feed-review"
      ],
      "change": "许苛正式裁定纠正陆宁私加燥阳谷的误信。",
      "source_evidence": "“上述记录、铃序、份量与残留路线，足以纠正先前对你私自投放燥阳谷的误信。燥阳谷经食槽阵错路进入鹿栏。现有证据，不能证明你私加燥阳谷。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "he-ming-not-yang-feed-caster",
      "state": "knows",
      "belief": "贺鸣的责任限于私用甜根囊、漏记耗用、诱引贪食豚压石；现有证据不认定他投放燥阳谷，也不认定为长期毁阵。",
      "supersedes_fact_ids": [
        "he-ming-not-yang-feed-caster"
      ],
      "change": "许苛正式限定贺鸣责任边界，没有扩展为投放燥阳谷或长期毁阵。",
      "source_evidence": "许苛继续道：“贺鸣之责，止于私用甜根囊、漏记耗用、诱引贪食豚压石。记过、清理赔工及隔栏安装照旧。现有证据不认定他投放燥阳谷，也不作长期毁阵论处。”"
    },
    {
      "character_id": "xu-ke",
      "fact_id": "trial-qualification-result",
      "state": "knows",
      "belief": "陆宁试用资格由冻结改为通过条件审查，但临时饲兽牌附带两日不得整群听息、单兽低强度校验须报备等条件。",
      "supersedes_fact_ids": [
        "trial-qualification-result"
      ],
      "change": "许苛完成陆宁试用资格条件审查并给出结果。",
      "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
    },
    {
      "character_id": "qiao-sui",
      "fact_id": "white-tuft-record-format",
      "state": "knows",
      "belief": "白绒的表现只能登记为槽温、气味、进食位置、蹄印方向和是否进食等可验材料，不能写成灵兽证词或拟人签收。",
      "supersedes_fact_ids": [
        "white-tuft-record-format"
      ],
      "change": "乔穗把白绒拟人化记录改为可验记录格式。",
      "source_evidence": "乔穗写道：“白绒愿意签收西槽——”\n\n许苛的目光扫过来。\n\n她立刻接下去：“即西槽槽温凉，无燥阳谷甜燥气，进食位置距槽口一尺二寸，蹄印由东向西，东槽未进食。”"
    }
  ],
  "thread_changes": [
    {
      "change": "食槽阵错路线索完成闭环：压力石记录、饲铃牌异常铃序、燥阳谷残留路线、份量缺口和甜根囊领用去向共同支撑最终责任结论。",
      "source_evidence": "“压力石持续受压记录，与饲铃牌异常铃序覆盖时段相合；燥阳谷残留路线与错接阵路相合；原料库四升份量缺口，与暖槽错送量相合；甜根囊领用去向，证明贺鸣曾诱引贪食豚停留压力石，造成错路条件。”"
    },
    {
      "change": "陆宁私加燥阳谷的审查线结案为不成立，但陆宁违规入栏、错铃、栏门铰损坏等责任继续保留。",
      "source_evidence": "“顺序无误。”许苛把违规册推回去，“私加燥阳谷不成立，不等于这三项消失。”"
    },
    {
      "change": "陆宁的栏门铰修理工时和赔偿从口头安排落实为文书条件。",
      "source_evidence": "陆宁在损坏单末尾按下指印。墨迹落定，修理工时与赔偿便不再只是口头安排。"
    }
  ],
  "comedy_changes": [
    {
      "change": "乔穗把白绒进食拟人化写成“愿意签收”，被迫改成可验数据。",
      "source_evidence": "乔穗写道：“白绒愿意签收西槽——”\n\n许苛的目光扫过来。\n\n她立刻接下去：“即西槽槽温凉，无燥阳谷甜燥气，进食位置距槽口一尺二寸，蹄印由东向西，东槽未进食。”"
    },
    {
      "change": "陆宁严肃把白绒的兽息结果翻译成不能夸自己的验收用语。",
      "source_evidence": "许苛问：“结果。”\n\n“能咽，不热，不是夸我。”"
    },
    {
      "change": "乔穗把临时牌条件念得像给白绒排班，被许苛纠正临时牌只管陆宁。",
      "source_evidence": "乔穗抱着归档册在一旁低声念：“陆宁，白日饲兽；白绒，西槽进食；两日内双方不得发生整群听息——”\n\n许苛抬眼：“临时牌只管陆宁，不给白绒排班。”"
    }
  ],
  "new_constraints": [
    {
      "change": "陆宁临时饲兽牌附带条件：两日内不得对整群使用听息诀，单兽低强度校验须报备。",
      "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
    },
    {
      "change": "陆宁宵禁入栏、擅改安抚铃记录保留；栏门铰修理与赔偿写入临时饲兽牌条件；后续考核仍看铃序、份量和损坏。",
      "source_evidence": "“宵禁入栏、擅改一次安抚铃，记录保留。栏门铰修理与赔偿，写入条件。后续考核仍看铃序、份量和损坏。白绒靠近你，只能记气味、蹄印和进食位置，不能替你抵一条违规。”"
    },
    {
      "change": "陆宁需参与栏门铰拆铰、校门和换件，赔偿按材料实耗核算。",
      "source_evidence": "“栏门铰未修复。你参与拆铰、校门和换件，赔偿按材料实耗核算。”"
    }
  ],
  "resolved_constraints": [
    {
      "change": "陆宁试用资格冻结解除，改为通过条件审查。",
      "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
    }
  ],
  "next_chapter_inputs": [
    "陆宁已取得御兽苑带条件临时饲兽牌，但两日内不得对整群使用听息诀，单兽低强度校验仍须报备。",
    "陆宁试用资格冻结已解除，改为通过条件审查；私加燥阳谷不成立。",
    "陆宁宵禁入栏、擅改一次安抚铃、冲栏处置不当导致栏门铰损坏的责任仍保留。",
    "陆宁已扣二点贡献不退，原有六点，现余四点。",
    "受损鹿栏门铰未修复，临时横撑仍在；陆宁需参与拆铰、校门和换件，赔偿按材料实耗核算。",
    "食槽阵最终验收通过：空槽试送无偏移，暖槽恢复原定路线，压力石校紧，防豚隔栏可阻持续压石，铃序复核牌可用。",
    "贺鸣责任限定为私用甜根囊、漏记耗用、诱引贪食豚压石；记过、清理赔工及隔栏安装照旧，不认定为投放燥阳谷或长期毁阵。",
    "乔穗负责槽位、气味、踏痕、拒食与进食记录，兼清栏归档；陆宁负责兽息对照与铃序复核。",
    "许苛后续考核陆宁仍看铃序、份量和损坏；白绒靠近陆宁只能记气味、蹄印和进食位置，不能抵违规。"
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
        "change": "云蹄鹿栏发生拒食，白绒避开中槽，两只幼鹿随行，成鹿闻槽未食。",
        "source_evidence": "陆宁答：“第三声开食后。白绒先避中槽，两只幼鹿随行，成鹿闻槽未食。”"
      },
      {
        "change": "中槽残留被封存，初步辨出有燥阳谷气味，但投放者未被证明。",
        "source_evidence": "陆宁神色微沉：“像燥阳谷。”\n\n“初闻是。”许苛将残留装瓶，封纸压印，“只说明燥阳谷到过这只槽，不说明谁放的。封存，核份量。”"
      },
      {
        "change": "饲铃牌显示今晨除正常三声铃序外，另有一次三声触发，且紧挨陆宁值守时段。",
        "source_evidence": "“一声，聚栏。二声，冷料分左槽。三声，开食。”许苛念到末尾，手指停住，“这里还有一次三声触发。”\n\n陆宁看见那道细痕紧挨着自己的值守时段，间隔不过半刻。"
      },
      {
        "change": "乔穗已开始把白绒行为转化为可查记录，包括气味、踏痕、进食结果、空桶无暖味和白绒主动嗅闻。",
        "source_evidence": "陆宁把桶翻过来给她看：“它只是闻到桶洗过，没有那股暖味。记空桶无异味，白绒愿意靠近。”\n\n乔穗只得把“证物清白”划去，改成“空桶无暖味，白绒主动嗅闻”。"
      },
      {
        "change": "许苛把异常铃序拓印留存，作为后续复核材料。",
        "source_evidence": "许苛收起封存瓶，将饲铃牌上的异常亮痕拓印下来：“鹿群今日拒食未解。入夜前核完青穗草与燥阳谷出库份量，晚间重走三声铃。谁少报一次动作，便从头复述。”"
      },
      {
        "change": "云蹄鹿栏门铰裂损，栏门歪斜，只能临时加固，不能当场恢复，需后续报修。",
        "source_evidence": "许苛蹲下检查门铰。裂口贯过铰片，固定钉也被扯松。他没有伸手硬掰，只取出损坏签压在门柱上，又命乔穗搬来横木，从外侧抵住歪斜栏门。\n\n“铰片裂损，当场不能恢复。今夜只能临时加固，明日起报修。修料、工时与赔偿，你参与核算。”"
      },
      {
        "change": "鹿栏门铰仍裂损，已加临时横撑但未修复，后续仍需报修、工时和赔偿核算。",
        "source_evidence": "他又指了指栏门：“复查前，先加一道横撑。昨夜的麻绳只够撑到今日。门铰裂了就是裂了，不会因为查出别的路径便自己长好。报修、工时、赔偿，后续照算。”"
      },
      {
        "change": "食槽阵压力石被确认只响应重量和持续时间，不能识别压石对象或引导者。",
        "source_evidence": "“压力石认重量和持续时间，不认蹄子，更不认引导者。”他说，“压痕与贪食豚栏常见蹄垫痕相似，只能记相似。不得定哪只豚，也不得定谁带来的。”"
      },
      {
        "change": "压力石周边阵沟泥水下发现带甜气的淡黄纤维，并被要求分袋留样。",
        "source_evidence": "泥水下露出几缕黏在阵沟边的淡黄纤维，带着一丝不属于普通草料的甜气。\n\n许苛俯身看了一眼，没有触碰。\n\n“分袋留样。”他道，“再去取甜根囊领用册。”"
      },
      {
        "change": "甜根囊领用册确认昨夜酉末有一袋甜根囊由贺鸣领出，名目为安置贪食豚换栏，且无归还、耗用记录。",
        "source_evidence": "“甜根囊，一袋。酉末领出，名目——安置贪食豚换栏。领用人，贺鸣。”\n\n账房里静了片刻。\n\n贺鸣站在门旁，目光落在账页上：“是我领的。”\n\n许苛问：“归还记录呢？”\n\n“用过了。”\n\n“耗用记录呢？”\n\n“当时忙，漏写了。”"
      },
      {
        "change": "压力石阵沟留样与未拆甜根囊外袋纤维完成比对，记录为气味相近、纤维形态相近、来源待核。",
        "source_evidence": "乔穗用细针拨了拨：“都是三股细丝拧成，断口散开，气味也近。”\n\n许苛问：“能写什么？”\n\n“甜根囊来过这里。”\n\n陆宁摇头：“只能写甜根囊外袋同类纤维曾接近此处。留样不能说明是谁带来，也不能说明贪食豚一定压过石。”\n\n乔穗把笔尖移回去，逐字改成：“气味相近，纤维形态相近，来源待核。”"
      },
      {
        "change": "贺鸣正式承认昨夜私下用甜根囊把贪食豚从自己栏位引开，并在石缝边留甜根囊让其停留，仍否认投燥阳谷。",
        "source_evidence": "贺鸣看着被蹭乱的泥线，终于低下头：“昨夜是我私下用了甜根囊，把它从自己栏位引开。它赖着不走，我又在石缝边留了一点，让它停在那里。我只想让它别回来，没投燥阳谷。”"
      },
      {
        "change": "许苛将贺鸣行为登记为诱引饲料去向违规待处置，并记入后续证据对照，但暂不认定其投放燥阳谷或长期蓄意破坏。",
        "source_evidence": "许苛翻出处置册：“贺鸣，诱引饲料去向违规，待处置。私下引贪食豚停在压力石附近，记入后续对照。暂不认定你投放燥阳谷，也不扩作长期蓄意破坏。”"
      },
      {
        "change": "乔穗获得分栏登记复核路线、甜根残留点、压力石停留位置、蹭乱后泥印的记录任务。",
        "source_evidence": "乔穗只得在册上列出四项：复核路线、甜根残留点、压力石停留位置、蹭乱后泥印。"
      },
      {
        "change": "乔穗将白绒避开鹿栏东槽的行为正式拆分记录为槽口甜气、暖料残留、拒食位置和蹄印转向，而非拟人化证词。",
        "source_evidence": "乔穗把脸板正，继续登记。她这回不再写白绒“拒绝认账”，只记东槽甜气较重、槽底有暖料残留、白绒在该槽前停步拒食，蹄印转向西槽。"
      },
      {
        "change": "受损栏门仍未修复，继续由临时横撑支撑。",
        "source_evidence": "受损栏门仍由临时横撑顶着，裂开的门铰垂在一侧。"
      },
      {
        "change": "受损栏门仍未修复，继续由临时横木支撑。",
        "source_evidence": "鹿栏东槽旁搭了临时称量台。受损的栏门仍由两根横木撑住，裂开的铰座露在外面，没人去碰。"
      },
      {
        "change": "乔穗完成对东槽残留、踏痕拓纸、甜气位置与白绒避槽行为的正式化记录，并被安排继续重抄复称记录、筛净残留袋和清理鹿栏。",
        "source_evidence": "乔穗刚松开抱着的残留袋，许苛便把两叠纸递给她：“复称记录重抄一份，三只袋重新筛净。鹿栏清理也归你。”"
      },
      {
        "change": "贺鸣被许苛正式记过一次，并被安排清理压力石周边、安装防豚隔栏、赔工照册核算。",
        "source_evidence": "许苛落下一笔：“私用诱引饲料，漏记耗用，诱使贪食豚持续停留压力石，造成食槽阵错路条件。记过一次，清理压力石周边，安装防豚隔栏，赔工照册核算。”"
      },
      {
        "change": "食槽阵压力石区新增防豚隔栏与铃序复核牌，空槽初试通过但最终验收未完成。",
        "source_evidence": "临时横撑挡住隔栏右脚的位置，他们不能挪横木，只得把隔栏向外移半尺，再加一道斜挡。贺鸣扛桩、压脚、收绳，肩上衣料很快湿透。许苛逐项验过，才准乔穗把铃序复核牌钉在阵台正面：一声开冷槽，二声换栏，三声启暖槽；压力石受压异常，先停铃复核。"
      },
      {
        "change": "受损栏门铰仍未修复，横撑继续顶在原处。",
        "source_evidence": "他转头看了一眼裂开的栏门铰。横撑仍顶在原处，铰座上的裂缝半点没少。"
      },
      {
        "change": "食槽阵完成最终验收并通过，空槽试送无偏移，暖槽路线恢复，压力石、防豚隔栏和铃序复核牌均确认可用。",
        "source_evidence": "许苛逐项检查槽温、出口、隔栏木楔和复核牌，最后在验收册上盖下印章。\n\n“空槽试送无偏移，暖槽恢复原定路线；压力石校紧，防豚隔栏可阻持续压石；铃序复核牌可用。食槽阵，验收通过。”"
      },
      {
        "change": "陆宁领取御兽苑带条件临时饲兽牌。",
        "source_evidence": "许苛取出一块窄长木牌。牌正面烙着“御兽苑临时饲兽”，背面却密密刻了数行小字。\n\n“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
      },
      {
        "change": "受损鹿栏门铰仍未修复，继续由临时横撑支撑。",
        "source_evidence": "棚外忽然传来木头轻响。\n\n临时横撑在风里顶住裂铰，栏门歪了半寸，又被撑回原处。"
      }
    ],
    "relationship_changes": [
      {
        "change": "陆宁被许苛列入重点复核对象，但未被正式定责。",
        "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”"
      },
      {
        "change": "乔穗因坚持把白绒当证人，被许苛安排清点中槽周围全部蹄印。",
        "source_evidence": "许苛却把她的册子抽来看了一遍，又指向栏边：“把中槽周围蹄印全部清点，分出避槽、近槽和后来踩乱的。既称它是证人，你便先把证人的脚印认全。”"
      },
      {
        "change": "许苛准许陆宁进行有限复查，但复查必须在白日、有许苛或同组弟子在场，并禁止陆宁听整群兽息或独立触动食槽阵。",
        "source_evidence": "许苛合上簿册，“复查准许。只限白日，须我或同组弟子在场，不得听整群兽息，不得独立触动食槽阵。夜间禁令照旧。”"
      },
      {
        "change": "贺鸣与昨夜甜根囊领用去向建立正式核查关系，但正文未确认其投放燥阳谷或引豚压石。",
        "source_evidence": "“我没往鹿栏投过。”贺鸣道，“甜根囊只是为了让贪食豚离开我的栏位。它后来往哪儿蹭，是它自己的腿。”\n\n“腿不记账，人记。”许苛在领用条目旁落下一笔，“去向待核。你随时听问，不得补写旧记录。”"
      },
      {
        "change": "许苛对贺鸣的责任边界作出划分：坐实诱引贪食豚压石造成错路条件，但不认定贺鸣投放燥阳谷或长期毁阵。",
        "source_evidence": "“记录里也没写是你放的。”许苛道，“甜根囊解释压石，不解释燥阳谷由谁投入暖槽。现有材料不能认定你亲手投放，更不能写成你长期蓄意毁阵。”"
      },
      {
        "change": "许苛明确陆宁仍需承担栏门后续修理工时与赔偿，并写入条件审查。",
        "source_evidence": "“食槽阵修了，栏门没修。陆宁，后续修理工时与赔偿写入你的条件审查。”"
      },
      {
        "change": "乔穗与陆宁在临时牌条件下形成明确分工：陆宁负责兽息对照与铃序复核，乔穗负责槽位、气味、踏痕、拒食、进食记录和清栏归档。",
        "source_evidence": "乔穗翻过一页，认真改道：“陆宁负责兽息对照与铃序复核。我负责槽位、气味、踏痕、拒食与进食记录，兼清栏归档。”\n\n“这条可写。”"
      },
      {
        "change": "许苛明确不会因白绒靠近陆宁而放宽陆宁的违规和考核条件。",
        "source_evidence": "“宵禁入栏、擅改一次安抚铃，记录保留。栏门铰修理与赔偿，写入条件。后续考核仍看铃序、份量和损坏。白绒靠近你，只能记气味、蹄印和进食位置，不能替你抵一条违规。”"
      }
    ],
    "cultivation_changes": [
      {
        "subject_id": "lu-ning",
        "kind": "injury",
        "change": "陆宁低强度使用听息诀后仍出现耳鸣和轻微方向错觉，breath-echo-vertigo 仍处于活动状态。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "耳中仍“嗡”地一响，食槽边缘像轻轻向左滑了半寸。陆宁闭眼定了定，脚下没有移动。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "insight",
        "change": "陆宁确认听息诀本次只能判断鹿群呼吸发紧、节奏乱和不适，不能判断投料者。",
        "state_id": "",
        "state_action": "",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "乔穗凑近：“它们说什么？”\n\n“呼吸发紧，节奏乱。是不适。”\n\n“谁害的？”\n\n“听不出来。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "solo-night-listening-ban 被许苛重申：伤势确认解除前，陆宁不得独自在夜间对整群云蹄鹿用听息诀，低强度复核也须有人在场。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“禁令再记一次。伤势确认解除前，不得独自在夜间对整群云蹄鹿用听息诀。低强度复核也须有人在场。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "injury",
        "change": "陆宁超限对整群使用听息诀后，breath-echo-vertigo 加重，出现更严重耳鸣与方向错判。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "陆宁眼前的栏木陡然倾斜。他分明朝左迈步，身体却撞上右侧门柱。方向在耳鸣里整个翻了过来。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "许苛确认陆宁听息回声加重、方向错判，solo-night-listening-ban 仍持续有效，并另记其超限施术。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛看了他一眼：“听息回声加重，方向错判。禁令仍在，另记超限施术。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格被冻结，复核前不得独立值栏。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "injury",
        "change": "陆宁的 breath-echo-vertigo 仍处于加重状态，未运诀时也出现方向错判，被许苛记入观察。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "source_evidence": "许苛在值事簿上添了一行：“辰时，方向错判一次，旁人扶正。听息回声仍重。”\n\n“我没有运诀。”陆宁道。\n\n“所以记伤势，不记施术。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "solo-night-listening-ban 继续有效，且复查期间不得听整群兽息。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "source_evidence": "许苛合上簿册，“复查准许。只限白日，须我或同组弟子在场，不得听整群兽息，不得独立触动食槽阵。夜间禁令照旧。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格仍被冻结，冻结木牌继续挂在名册上。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "source_evidence": "乔穗问：“那他的牌呢？”\n\n许苛把“冻结”木牌重新挂回名册：“挂着。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "ability",
        "change": "陆宁的听息诀在监督下通过单兽低强度校验，初步能区分白绒的受热不适呼吸与昨夜群体惊慌节奏，但仍限于报节奏，不得猜人或读心。",
        "state_id": "beast-breath-listening",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“能。”陆宁没有起身，“白绒现在是短促、避热式呼吸。受暖性气味刺激，停顿固定。昨夜冲栏前是节奏互相催快，停顿散乱，属于群体惊慌。两者不同。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "recovery",
        "change": "陆宁的听息回声眩晕出现部分恢复苗头：耳鸣短暂减轻，但眩晕未解除。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "片刻后，耳中的尖鸣稍稍退远，像从耳骨里挪到了院墙外，可脚下仍有轻微倾斜感。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁的夜间独自整群听息禁令继续有效。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“二点贡献也不退，余额仍是四点。试用冻结照旧。”许苛道，“你方才耳鸣减轻，只算恢复苗头。眩晕未除，夜间独自整群听息禁令继续。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格仍被冻结。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“二点贡献也不退，余额仍是四点。试用冻结照旧。”许苛道，“你方才耳鸣减轻，只算恢复苗头。眩晕未除，夜间独自整群听息禁令继续。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "ability",
        "change": "陆宁在许苛监督下只对白绒施展一次短促单兽听息，确认其可记录单兽受热不适前的躲槽节奏，仍未扩展到整群、读心或辨人。",
        "state_id": "beast-breath-listening",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛看向陆宁：“一次，短息。只听白绒。”\n\n陆宁按住耳后封耳条，缓缓引出一缕灵气。听息诀只落在白绒身上，不向旁侧扩散。\n\n细碎的呼吸声贴近耳中。\n\n两短，一滞，再短促收紧。\n\n不像昨夜群体惊慌时此起彼伏的急乱，也没有互相追随的节奏。更像白绒先前靠近暖槽时，胸息受热后出现的回避。\n\n陆宁立刻收诀。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "injury",
        "change": "陆宁听息后仍有耳闷和轻微晕感，听息回声眩晕未解除。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "耳内仍旧闷响了一下，脚下也有轻微浮晃。他扶住栏柱，等视线定住，才开口：“单兽。受热不适前的躲槽节奏，不是群体惊慌。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁今日不得再听息，夜间独自整群听息禁令继续有效。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“今日不得再听。夜间独自整群听息禁令照旧。”\n\n陆宁应下，重新压紧封耳条。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格继续冻结。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“这不代表你已洗清。宵禁入栏、错铃、栏门铰损坏另册照记。试用资格继续冻结，扣去的二点不退，余额四点。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "recovery",
        "change": "陆宁听息回声眩晕有所减轻但未解除，仍有耳中闷响。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛又看向陆宁：“你眩晕有所减轻，但未解除。明日白日，可在我监督下继续单兽低强度校验。夜间独自对整群听息，禁令照旧。”\n\n陆宁点头。耳中闷响仍在，只比早间远了些。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "ability",
        "change": "陆宁的听息诀使用边界维持为白日、许苛监督下、单兽低强度校验；仍未扩展到整群、读心、辨谎或追踪投料者。",
        "state_id": "beast-breath-listening",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛又看向陆宁：“你眩晕有所减轻，但未解除。明日白日，可在我监督下继续单兽低强度校验。夜间独自对整群听息，禁令照旧。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁夜间独自对整群听息的禁令继续有效。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛又看向陆宁：“你眩晕有所减轻，但未解除。明日白日，可在我监督下继续单兽低强度校验。夜间独自对整群听息，禁令照旧。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格继续冻结。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "ability",
        "change": "陆宁在白日、许苛监督下完成对白绒的一次单兽低强度听息校验，确认白绒为受热不适而非群体惊慌；听息诀边界仍限于验节奏，不能说明投料者或辨谎。",
        "state_id": "beast-breath-listening",
        "state_action": "set",
        "stage_after": "炼气二层",
        "source_evidence": "“受热不适。”陆宁退开半步，“不是群体惊慌。只能验节奏，不能说明谁投料，也不能验谁说了假话。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "recovery",
        "change": "陆宁听息回声眩晕部分恢复：耳鸣比昨日减轻，但转身仍晕，未解除。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "source_evidence": "许苛检查陆宁耳后：“耳鸣如何？”\n\n“比昨日轻。转身仍晕。”\n\n“回声眩晕只记部分恢复，未解除。夜间独自整群听息禁令照旧。封耳条继续戴，今日不得再校验第二只。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁夜间独自整群听息禁令继续有效，封耳条继续佩戴，且当日不得再校验第二只灵兽。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "source_evidence": "“回声眩晕只记部分恢复，未解除。夜间独自整群听息禁令照旧。封耳条继续戴，今日不得再校验第二只。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格冻结不解除。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "source_evidence": "陆宁问：“试用冻结呢？”\n\n“不解。二点贡献不退，余额四点。宵禁、错铃另册。栏门铰未修，修理与赔偿照旧。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "ability",
        "change": "陆宁本章未再次运转听息诀，只依据昨日白日、监督下、单兽低强度校验所得辅助判断白绒受热不适；听息诀仍不能判断投料者。",
        "state_id": "beast-breath-listening",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛看向陆宁：“只准用昨日校验所得，不得再运诀。”\n\n陆宁点头。他没有凝神听取整栏兽息，只依白绒昨日单兽低强度校验的记录，对照眼前起伏的腹侧。\n\n“短促，浅，咽前停顿。是受热不适。不是群体惊慌。”\n\n乔穗问：“翻到账上怎么写？”\n\n“东槽暖料残留位置，与受热不适、拒食位置相合。”陆宁顿了顿，“不能写谁投的。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "injury",
        "change": "陆宁回声眩晕仍未解除，转身稍快即耳鸣、站立偏移，封耳条继续佩戴。",
        "state_id": "breath-echo-vertigo",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他说完起身想看秤盘，转得稍快，耳内立刻嗡鸣，脚下偏了半步。乔穗伸手扶住称量台，没去扶他，只把挡路的残留袋先挪开。\n\n许苛皱眉：“坐回去。今日不得再校验第二只。”\n\n陆宁缓了两息，依言坐下。封耳条仍贴得严实，眩晕并未因账目对上便少一分。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁夜间不得独自对整群使用听息诀的禁令继续有效，且回声眩晕未获许苛确认解除。",
        "state_id": "solo-night-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他又指了指陆宁耳后的封耳条：“回声眩晕未由我确认解除。夜间不得独自对整群使用听息诀，仍然有效。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格继续冻结。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛将另一册推到他面前：“私投燥阳谷暂不成立，不等于宵禁后入栏无事。你擅改一次安抚铃，记录保留；阻栏处置不当，栏门铰损坏，修理与赔偿保留；已扣二点贡献不退，余额四点；试用资格继续冻结。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "ability",
        "change": "陆宁的听息诀稳定在单兽低强度校验范围内，可分辨白绒当前平稳、未受热不适，以及受远栏惊动导致的短促应激；未扩听整群。",
        "state_id": "beast-breath-listening",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "他收诀：“白绒当前平稳。没有受热不适。方才短促，是受远栏惊动。”\n\n“远栏呢？”许苛问。\n\n陆宁没有再放开听息：“我不听整群。只从眼前踏蹄与白绒应激变化判断，远处有群体惊慌迹象，不能据此多说。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "recovery",
        "change": "陆宁的听息回声眩晕经停止整群听息、使用封耳条、休养及白日监督下单兽低强度校验后由许苛确认解除。",
        "state_id": "breath-echo-vertigo",
        "state_action": "resolve",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "许苛在伤势册上写道：“经停止整群听息、使用封耳条、休养及白日监督下单兽低强度校验，听息回声眩晕解除。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁夜间不得独自对整群使用听息诀的旧禁令结束。",
        "state_id": "solo-night-listening-ban",
        "state_action": "resolve",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁新增自今日起两日内不得对整群使用听息诀的限制；单兽低强度使用仍须报备。",
        "state_id": "two-day-group-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格继续冻结，临时饲兽牌审查留到明日。",
        "state_id": "trial-qualification-freeze",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“你的试用冻结不解除。”许苛合上伤势册，将食槽阵初试记录、栏门赔偿单和责任卷并排放好，“明日验阵、宣告燥阳谷责任结论，再审临时饲兽牌。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "ability",
        "change": "陆宁的听息诀继续限定在单兽低强度校验范围内，本章实际确认可通过白绒呼吸判断无受热急促滞顿、无群体惊慌乱拍，未扩听整群，也未追索气味来处。",
        "state_id": "beast-breath-listening",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "细缓的呼吸混着咀嚼声传来，没有受热时的急促滞顿，也没有群体惊慌时一呼带一呼的乱拍。陆宁只听了三息便收诀，既不牵连旁边鹿群，也不追索气味来处。"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁试用资格冻结解除，改为通过条件审查。",
        "state_id": "trial-qualification-freeze",
        "state_action": "resolve",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
      },
      {
        "subject_id": "lu-ning",
        "kind": "restriction",
        "change": "陆宁两日内不得对整群使用听息诀的限制继续生效，单兽低强度校验仍须报备。",
        "state_id": "two-day-group-listening-ban",
        "state_action": "set",
        "stage_after": "炼气二层",
        "from_stage": "",
        "to_stage": "",
        "prerequisites": [],
        "costs": [],
        "new_limits": [],
        "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
      }
    ],
    "resource_changes": [
      {
        "owner_id": "lu-ning",
        "resource_id": "contribution-point",
        "operation": "consume",
        "amount": 2,
        "unit": "点",
        "resulting_balance": 4,
        "source_or_destination": "御兽苑考核处罚",
        "change": "陆宁因宵禁入栏、擅改铃序和处置不当致栏门铰损坏，被扣除贡献二点，余额由六点变为四点。",
        "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
      },
      {
        "owner_id": "beast-yard",
        "resource_id": "sweet-root-pouch",
        "operation": "consume",
        "amount": 1,
        "unit": "袋",
        "resulting_balance": 3,
        "source_or_destination": "贺鸣昨夜领出后称已用过且漏写耗用记录",
        "change": "御兽苑甜根囊账面确认少一袋：昨夜由贺鸣领出，贺鸣称已用过但无耗用记录。",
        "source_evidence": "贺鸣站在门旁，目光落在账页上：“是我领的。”\n\n许苛问：“归还记录呢？”\n\n“用过了。”\n\n“耗用记录呢？”\n\n“当时忙，漏写了。”"
      }
    ],
    "knowledge_changes": [
      {
        "character_id": "lu-ning",
        "fact_id": "wrong-feed-route",
        "state": "investigating",
        "belief": "燥阳谷到过中槽且异常三声铃紧挨自己的值守时段，但饲铃牌不能证明敲铃者，仍需从铃序、份量和槽路复核。",
        "supersedes_fact_ids": [],
        "change": "陆宁掌握中槽疑似燥阳谷残留与相邻异常铃序的调查焦点，但没有获得投料者结论。",
        "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”\n\n“我没有私加燥阳谷。”陆宁道。\n\n“那就拿铃序、份量和槽路说话。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "investigating",
        "belief": "异常三声铃与陆宁值守相邻，需要复核，但饲铃牌不记敲铃者，不能据此定责陆宁私加燥阳谷。",
        "supersedes_fact_ids": [
          "lu-ning-secret-yang-feed"
        ],
        "change": "许苛不再按既有误信直接认定陆宁私加燥阳谷，而把异常铃序列为复核项。",
        "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trial-qualification-result",
        "state": "investigating",
        "belief": "陆宁试用表现需按铃序、饲料份量和兽栏后果继续复核，灵兽亲近或避开不算证据。",
        "supersedes_fact_ids": [],
        "change": "许苛明确后续裁定标准为铃序、饲料份量和兽栏后果。",
        "source_evidence": "许苛封好瓷瓶：“亲近不抵一粒谷，避开也不抵一声铃。后续我只看铃序、饲料份量和兽栏后果。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-record-format",
        "state": "knows",
        "belief": "白绒避槽不能直接记成证词，必须写成气味、踏痕和进食结果等可复查记录。",
        "supersedes_fact_ids": [],
        "change": "乔穗被陆宁和许苛纠正记录方式。",
        "source_evidence": "乔穗张了张嘴。\n\n“写气味、踏痕、进食结果。”许苛取出封料纸和细口瓷瓶，“灵兽不是值房执事，它不签押。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-hoofprint-count",
        "state": "investigating",
        "belief": "需要清点中槽周围蹄印，分出避槽、近槽和后来踩乱的痕迹。",
        "supersedes_fact_ids": [],
        "change": "乔穗开始调查并记录白绒及鹿群在中槽周围的蹄印。",
        "source_evidence": "许苛却把她的册子抽来看了一遍，又指向栏边：“把中槽周围蹄印全部清点，分出避槽、近槽和后来踩乱的。既称它是证人，你便先把证人的脚印认全。”"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "wrong-feed-route",
        "state": "investigating",
        "belief": "陆宁知道自己没有加燥阳谷，并继续把燥阳谷残留与饲料路线作为需要查明的问题。",
        "supersedes_fact_ids": [],
        "change": "陆宁明确否认自己加过燥阳谷，但正文没有证明其否认已被他人采信或最终定案。",
        "source_evidence": "陆宁听见“冻结”二字，指尖慢慢收紧，却没有辩解前面三项。\n\n“燥阳谷不是我加的。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "suspects",
        "belief": "许苛当前按陆宁可能私加暖料的方向核查，但承认这不是定案，燥阳谷残留只能证明暖性饲料到过鹿栏，不能单独证明投放者。",
        "supersedes_fact_ids": [
          "lu-ning-secret-yang-feed-review"
        ],
        "change": "许苛将核查方向更新为怀疑陆宁可能私加暖料，同时保留饲料路线核查空间。",
        "source_evidence": "许苛合上半边册页：“中槽有燥阳谷残留，错铃发生在你值守相邻时段，今夜你又私自改铃。我当前先按你可能私加暖料核查。”\n\n“饲铃牌不记敲铃者。”\n\n“所以我说核查，不是定案。”许苛指向封住的中槽，“残留只能证明暖性饲料到过鹿栏，不能单独证明谁投放。你的违规与投料责任分开记。铃序、份量、饲料路线，一项都不会少。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trial-qualification-result",
        "state": "knows",
        "belief": "许苛已按宵禁入栏、擅改安抚铃序、处置不当致栏门铰损坏，裁定陆宁扣贡献二点、试用资格冻结、复核前不得独立值栏。",
        "supersedes_fact_ids": [
          "trial-qualification-result"
        ],
        "change": "许苛对陆宁试用表现的复核从调查状态推进为当场处罚裁定。",
        "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-hoofprint-count",
        "state": "investigating",
        "belief": "乔穗在清点白绒与鹿群踏痕时发现一串非鹿蹄的圆钝压痕，压痕通向食槽阵压力石旁，来源尚未确认。",
        "supersedes_fact_ids": [
          "white-tuft-hoofprint-count"
        ],
        "change": "乔穗的蹄印清点从单纯分辨鹿蹄痕，推进到发现压力石旁的非鹿压痕线索。",
        "source_evidence": "泥里有一串圆钝压痕，边缘宽厚，没有分瓣，不是云蹄鹿留下的。压痕从中槽后方斜穿清理道，一直没入食槽阵的石廊。\n\n乔穗挪过灯盏，顺着最后两枚压痕照去。\n\n它们正停在那块压力石旁。"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-record-format",
        "state": "knows",
        "belief": "乔穗知道不能把白绒的行为写成告状或证词，已改为记录避槽位置、绕行距离、暖性气味与圆钝压痕等可验证事项。",
        "supersedes_fact_ids": [],
        "change": "乔穗将对白绒行为的拟人化判断改成可验证记录格式。",
        "source_evidence": "乔穗重新铺开沾泥薄纸，将“白绒在告状”彻底划去，逐项写下避槽位置、绕行距离、暖性气味与圆钝压痕。"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-hoofprint-count",
        "state": "investigating",
        "belief": "乔穗已量得中槽后方到食槽阵压力石旁存在宽圆钝厚的非鹿蹄压痕，并发现其与贪食豚蹄垫痕宽度和后缘相近，但来源未确认。",
        "supersedes_fact_ids": [],
        "change": "乔穗的圆钝压痕线索推进到与贪食豚栏常见蹄垫痕相似的可比对记录。",
        "source_evidence": "通往暖料槽路的那块石面沾着薄泥，石旁草根倒伏，正有两枚较完整的圆钝印。\n\n乔穗取出细绳贴着边缘一围，再与方才拓下的尺寸比对。\n\n“宽度相近，后缘也一样钝。”她抬头，“是贪食豚。”"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "wrong-feed-route",
        "state": "investigating",
        "belief": "陆宁正在调查燥阳谷进入鹿栏的路径，并提出压力石持续受压叠加异常铃序可能导致暖料转错槽位，但尚未证明。",
        "supersedes_fact_ids": [],
        "change": "陆宁将调查方向推进到压力石受压、异常铃序与暖料错槽之间的关联。",
        "source_evidence": "陆宁察看倒伏草根：“若此石持续受压，再叠上异常铃序，暖料可能转错槽位。”\n\n许苛看了他一眼：“可能。不是已经证明。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "suspects",
        "belief": "许苛仍未排除陆宁私加暖料，但也承认现有事实不能证明陆宁投放过燥阳谷。",
        "supersedes_fact_ids": [],
        "change": "许苛对陆宁私加暖料的怀疑未解除，但明确仍非定案。",
        "source_evidence": "许苛收起三张纸：“现有事实仍不能排除你私加暖料，也不能证明你投放过。冻结不解，错铃与宵禁记录不撤。”"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "wrong-feed-route",
        "state": "knows",
        "belief": "压力石持续受压会使暖槽偏向鹿栏；解除压力后阵路复位，但昨夜压石对象和诱因尚未确定。",
        "supersedes_fact_ids": [
          "wrong-feed-route"
        ],
        "change": "陆宁参与复核后，原本调查中的错送路线被现场确认到机制层面。",
        "source_evidence": "许苛将三次结果写进阵录：“持续受压，暖槽偏向鹿栏；解除压力，阵路复位。错送可能存在。至于昨夜压石的是不是这只、为何停留，尚不能定。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "pig-pressure-stone",
        "state": "knows",
        "belief": "贪食豚持续趴在压力石上可触发暖槽阵路偏向鹿栏，但压力石只记录重量和时长，不识别压石对象。",
        "supersedes_fact_ids": [
          "pig-pressure-stone"
        ],
        "change": "乔穗对贪食豚压石与暖性饲料错路有关的怀疑被现场复核确认为机制事实。",
        "source_evidence": "乔穗划去两字，又在路线末端重重圈住鹿栏：“但阵路偏了。”\n\n“这可以记。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-hoofprint-count",
        "state": "investigating",
        "belief": "乔穗继续围绕贪食豚栏、压力石周边泥印和草屑留样核查压痕与停留痕迹。",
        "supersedes_fact_ids": [],
        "change": "乔穗被安排清理贪食豚栏和压力石周边，并分别留样泥印、草屑。",
        "source_evidence": "许苛指向贪食豚栏：“能。画图的人最熟压痕与阵沟，午后清豚栏，再刷压力石周边。泥印、草屑分别留样。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "suspects",
        "belief": "许苛承认阵路错送可能存在，但仍继续调查陆宁私加燥阳谷一项，且不因此抵销陆宁错铃、宵禁入栏等违规。",
        "supersedes_fact_ids": [
          "lu-ning-secret-yang-feed-review"
        ],
        "change": "许苛对陆宁私加暖料的怀疑被进一步削弱为仍查，同时明确阵路机制不能直接洗清违规。",
        "source_evidence": "陆宁问：“私加燥阳谷一项呢？”\n\n“仍查。”许苛合上阵录，“阵路能把暖料送错，不等于昨夜一定如此；更不等于你的错铃、宵禁入栏可以不算。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trough-pressure-route",
        "state": "knows",
        "belief": "持续受压会使暖槽偏向鹿栏，解除压力后阵路复位；但昨夜压石对象和停留原因尚不能定。",
        "supersedes_fact_ids": [],
        "change": "许苛亲自把压力石持续受压导致暖槽偏鹿栏的复核结果写入阵录。",
        "source_evidence": "许苛将三次结果写进阵录：“持续受压，暖槽偏向鹿栏；解除压力，阵路复位。错送可能存在。至于昨夜压石的是不是这只、为何停留，尚不能定。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "white-tuft-heat-discomfort",
        "state": "knows",
        "belief": "鹿对暖性余味有受热不适，与群体惊慌节奏不同；该结论不能证明投料者、昨夜具体阵路，也不能抵销陆宁错铃与宵禁违规。",
        "supersedes_fact_ids": [],
        "change": "许苛认可陆宁对白绒单兽低强度听息结果的有限边界，并将其纳入记录。",
        "source_evidence": "“可作低强度对照。”许苛在阵录后添上一行，“鹿对暖性余味有受热不适，与群体惊慌节奏不同。”\n\n他笔锋一转，又补了三句：“不能证明谁投料。不能证明昨夜具体阵路。不能抵销错铃与宵禁违规。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "sweet-root-fiber-sample",
        "state": "investigating",
        "belief": "压力石周边阵沟发现带甜气的淡黄纤维，需要分袋留样并调取甜根囊领用册继续核查。",
        "supersedes_fact_ids": [],
        "change": "许苛开始调查压力石周边淡黄纤维与甜根囊领用去向。",
        "source_evidence": "泥水下露出几缕黏在阵沟边的淡黄纤维，带着一丝不属于普通草料的甜气。\n\n许苛俯身看了一眼，没有触碰。\n\n“分袋留样。”他道，“再去取甜根囊领用册。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "sweet-root-fiber-sample",
        "state": "investigating",
        "belief": "甜根囊外袋同类纤维曾接近压力石阵沟，气味与形态相近，但不能证明是谁带来，也不能证明贪食豚一定压过石。",
        "supersedes_fact_ids": [],
        "change": "许苛将淡黄纤维线索从取册核查推进为纤维、气味与位置比对后的待核证据。",
        "source_evidence": "陆宁摇头：“只能写甜根囊外袋同类纤维曾接近此处。留样不能说明是谁带来，也不能说明贪食豚一定压过石。”\n\n乔穗把笔尖移回去，逐字改成：“气味相近，纤维形态相近，来源待核。”\n\n许苛收走两份比对记录：“这才是账上能用的话。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "suspects",
        "belief": "陆宁是否私加燥阳谷仍未洗清，但调查不再只围绕陆宁，需并查甜根囊去向、贪食豚停留和暖槽错路。",
        "supersedes_fact_ids": [],
        "change": "许苛保留陆宁私加燥阳谷疑点，同时扩大调查证据链。",
        "source_evidence": "“从今日起，不再只复查陆宁是否私加燥阳谷。”许苛道，“分三段查。甜根囊从领出到耗用去了哪里；贪食豚昨夜停在何处、停了多久；暖槽错路是否与受压时段重合。”\n\n他又在陆宁名字下方点了一笔。\n\n“这不代表你已洗清。宵禁入栏、错铃、栏门铰损坏另册照记。试用资格继续冻结，扣去的二点不退，余额四点。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-record-format",
        "state": "knows",
        "belief": "白绒的反应只能记录为闻到甜气后退半步、未碰槽，不能写成拒绝或指认。",
        "supersedes_fact_ids": [],
        "change": "乔穗修正对白绒反应的记录格式，避免将灵兽行为写成人类证词。",
        "source_evidence": "乔穗提笔便写：“白绒拒绝——”\n\n她顿住，看了看许苛，自己把后两个字划去。\n\n“白绒闻到甜气后退半步，未碰槽。”"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "wrong-feed-route",
        "state": "knows",
        "belief": "甜根囊与燥阳谷是两个饲料问题，甜根囊经贺鸣手不能直接证明贺鸣向鹿栏投放燥阳谷。",
        "supersedes_fact_ids": [],
        "change": "陆宁明确区分甜根囊领用线索与燥阳谷投放问题。",
        "source_evidence": "贺鸣看向陆宁：“你想凭一袋甜根囊，说我往鹿栏投了燥阳谷？”\n\n“不能。”陆宁道，“两种饲料，两个问题。”"
      },
      {
        "character_id": "he-ming",
        "fact_id": "sweet-root-lure",
        "state": "knows",
        "belief": "自己昨夜私下用甜根囊把贪食豚从自己栏位引开，并在石缝边留了一点让它停在那里；自己没有投燥阳谷。",
        "supersedes_fact_ids": [
          "sweet-root-lure"
        ],
        "change": "贺鸣不再成功隐瞒甜根囊引豚停留压力石附近一事，已当场承认。",
        "source_evidence": "贺鸣看着被蹭乱的泥线，终于低下头：“昨夜是我私下用了甜根囊，把它从自己栏位引开。它赖着不走，我又在石缝边留了一点，让它停在那里。我只想让它别回来，没投燥阳谷。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "sweet-root-fiber-sample",
        "state": "knows",
        "belief": "少量甜根囊残味足以诱使贪食豚靠近并停留压力石，但这只证明诱因可行，不证明昨夜压石对象有意破坏阵路。",
        "supersedes_fact_ids": [
          "sweet-root-fiber-sample"
        ],
        "change": "许苛将甜根囊纤维线索推进为甜根囊残味可诱使贪食豚停留压力石的已验证诱因。",
        "source_evidence": "许苛收起记时片：“少量甜根囊残味，足以诱使贪食豚靠近并停留压力石。只证诱因可行，不证明昨夜压石对象有意破坏阵路。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "suspects",
        "belief": "陆宁私加燥阳谷的嫌疑已被新证据削弱，但尚不能定结。",
        "supersedes_fact_ids": [
          "lu-ning-secret-yang-feed-review"
        ],
        "change": "许苛对陆宁私加燥阳谷的怀疑进一步削弱，但未最终解除。",
        "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trough-pressure-route",
        "state": "investigating",
        "belief": "下一步需要对照压力石持续受压时长、饲铃牌异常铃序、燥阳谷残留路线。",
        "supersedes_fact_ids": [
          "trough-pressure-route"
        ],
        "change": "许苛将后续调查明确推进为三表同案复核。",
        "source_evidence": "许苛将饲铃牌、记时片和留样袋分别收入木匣：“下一步，对照压力石持续受压时长、饲铃牌异常铃序、燥阳谷残留路线。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-hoofprint-count",
        "state": "investigating",
        "belief": "乔穗需要把复核路线、甜根残留点、压力石停留位置、蹭乱后泥印分开登记。",
        "supersedes_fact_ids": [
          "white-tuft-hoofprint-count"
        ],
        "change": "乔穗的泥印与路线记录任务更新为四项分栏登记。",
        "source_evidence": "乔穗只得在册上列出四项：复核路线、甜根残留点、压力石停留位置、蹭乱后泥印。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trough-pressure-route",
        "state": "knows",
        "belief": "三表首次对照显示压力石持续受压覆盖异常三声铃后的暖槽偏移，残留路线与暖槽偏向鹿栏的阵路一致；目前只能说明暖料有错送路径。",
        "supersedes_fact_ids": [
          "trough-pressure-route"
        ],
        "change": "许苛完成压力石时长、饲铃牌铃序和燥阳谷残留路线的三表对照，并将调查从待对照推进为已确认错送路径吻合。",
        "source_evidence": "许苛核过三处：“压力石持续受压，覆盖异常三声铃后的暖槽偏移。残留路线，也与暖槽偏向鹿栏的阵路一致。到这里，只能说明暖料有错送路径。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "investigating",
        "belief": "陆宁私加燥阳谷的旧批注已改为尚无直接投料证据，后续需核定暖槽出料数、鹿栏残留量和原料库登记量。",
        "supersedes_fact_ids": [
          "lu-ning-secret-yang-feed-review"
        ],
        "change": "许苛将对陆宁私加燥阳谷的旧判断降级为尚无直接投料证据、待份量与路线继续核定。",
        "source_evidence": "他收起记录板，当场改了旧案上的批注：“陆宁私加燥阳谷，改为尚无直接投料证据。待暖槽出料数、鹿栏残留量、原料库登记量核定。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trial-qualification-result",
        "state": "knows",
        "belief": "陆宁试用冻结不解，二点贡献不退，余额四点，宵禁和错铃另册，栏门铰未修且修理赔偿照旧。",
        "supersedes_fact_ids": [
          "trial-qualification-result"
        ],
        "change": "许苛明确陆宁相关处罚后果全部保留。",
        "source_evidence": "陆宁问：“试用冻结呢？”\n\n“不解。二点贡献不退，余额四点。宵禁、错铃另册。栏门铰未修，修理与赔偿照旧。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-record-format",
        "state": "knows",
        "belief": "白绒避槽行为不能写成拟人化证词，正式记录应写东槽甜气、槽底暖料残留、拒食位置和蹄印转向。",
        "supersedes_fact_ids": [
          "white-tuft-record-format"
        ],
        "change": "乔穗已按许苛要求把白绒避槽说法改成可复核记录格式。",
        "source_evidence": "乔穗把脸板正，继续登记。她这回不再写白绒“拒绝认账”，只记东槽甜气较重、槽底有暖料残留、白绒在该槽前停步拒食，蹄印转向西槽。"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-hoofprint-count",
        "state": "knows",
        "belief": "白绒前蹄停在东槽外两尺后绕向西侧净槽，中途未回东槽。",
        "supersedes_fact_ids": [
          "white-tuft-hoofprint-count"
        ],
        "change": "乔穗补上白绒东槽外停步并绕向西槽的踏痕记录。",
        "source_evidence": "乔穗沉默片刻，把“不肯签字”划掉，拆成三行。写完又去取泥印拓纸，补上白绒前蹄停在东槽外两尺、绕向西侧净槽的痕迹。她刚想在末尾添一句“态度坚决”，瞥见那列新字，只得改成“中途未回东槽”。"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "wrong-feed-route",
        "state": "knows",
        "belief": "压力石受压覆盖异常三声铃和暖槽未复位时段，残留路线与鹿栏东槽错送路径吻合。",
        "supersedes_fact_ids": [
          "wrong-feed-route"
        ],
        "change": "陆宁参与确认压力石受压时段覆盖异常铃序与暖槽未复位时段。",
        "source_evidence": "“压力石受压到何时？”乔穗问。\n\n“子初三刻。”陆宁道，“覆盖三声铃，也覆盖暖槽未复位的时段。”"
      },
      {
        "character_id": "he-ming",
        "fact_id": "sweet-root-lure",
        "state": "knows",
        "belief": "许苛只认定贺鸣甜根囊时间接近压力石受压诱因，不能证明贺鸣投放燥阳谷。",
        "supersedes_fact_ids": [
          "sweet-root-lure"
        ],
        "change": "贺鸣听到许苛明确三表目前不能证明他投放燥阳谷。",
        "source_evidence": "“表上也没写有关。”许苛指向空着的份量栏，“三张表不替你背锅，也不替陆宁背。时间若对不上，你的甜根囊只算去向违规；时间若对得上，也只能证明压石诱因与你相近，不能证明你投了燥阳谷。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "investigating",
        "belief": "燥阳谷份量缺口与异常铃后暖槽出料相符，鹿栏残留及阵路损耗可核；现有事实暂不支持陆宁私自投放燥阳谷，但尚未结案。",
        "supersedes_fact_ids": [
          "lu-ning-secret-yang-feed-review"
        ],
        "change": "许苛将陆宁名下旧批注进一步改为暂不支持陆宁私自投放燥阳谷，但保留尚未结案。",
        "source_evidence": "许苛提笔，将旧批注划去，重写：“燥阳谷份量缺口与异常铃后暖槽出料相符，鹿栏残留及阵路损耗可核。现有事实暂不支持陆宁私自投放燥阳谷，尚未结案。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trough-pressure-route",
        "state": "knows",
        "belief": "异常三声铃后暖槽出料四升，鹿栏东槽及偏送阵路复称三升八合，二合为沿路损耗，库中短少四升与该次出料相符。",
        "supersedes_fact_ids": [
          "trough-pressure-route"
        ],
        "change": "许苛通过库册、出料与残留复称确认燥阳谷四升缺口可与错路出料核算相符。",
        "source_evidence": "许苛将算盘拨到最后一位：“异常三声铃后，暖槽出料四升。鹿栏东槽及偏送阵路复称三升八合。二合为沿路损耗。库中短少四升，与该次出料相符。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "sweet-root-lure-review",
        "state": "investigating",
        "belief": "贺鸣领用诱引饲料不记耗用并将贪食豚引到压力石附近，压力石持续受压时段与错路重合；此事需与铃序及受压记录合并另行处置，但不等同于认定他另行投放燥阳谷。",
        "supersedes_fact_ids": [],
        "change": "许苛保留贺鸣甜根囊去向违规与压力石受压时段的合并核查。",
        "source_evidence": "“不能。”许苛道，“四升燥阳谷可由错路解释，只说明暂不能认定有人另行投料。你领用诱引饲料不记耗用，又将贪食豚引到压力石附近，压力石持续受压的时段与错路重合。两件事不是一件罪，也不是毫无关系。下一步合并铃序与受压记录，另行处置。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-record-format",
        "state": "knows",
        "belief": "白绒避开东槽的记录必须写成槽底暖料残留、停步位置、未进食与蹄印转向西槽，不能写成拟人化拒绝签收。",
        "supersedes_fact_ids": [
          "white-tuft-record-format"
        ],
        "change": "乔穗把对白绒拒食的拟人化写法改成槽位、残留和蹄印方向记录。",
        "source_evidence": "乔穗立即改口：“东槽一号，槽底暖料残留。白绒于东槽前三尺停步，未进食，蹄印转向西槽。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "sweet-root-lure-review",
        "state": "knows",
        "belief": "贺鸣私用诱引饲料、漏记耗用，诱使贪食豚持续停留压力石，造成食槽阵错路条件，应记过并承担清理、安装防豚隔栏和赔工。",
        "supersedes_fact_ids": [
          "sweet-root-lure-review"
        ],
        "change": "许苛将贺鸣甜根囊与压力石受压的核查转为正式认定和处置。",
        "source_evidence": "许苛落下一笔：“私用诱引饲料，漏记耗用，诱使贪食豚持续停留压力石，造成食槽阵错路条件。记过一次，清理压力石周边，安装防豚隔栏，赔工照册核算。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "he-ming-not-yang-feed-caster",
        "state": "knows",
        "belief": "现有材料不能认定贺鸣亲手投放燥阳谷，也不能写成贺鸣长期蓄意毁阵。",
        "supersedes_fact_ids": [],
        "change": "许苛明确贺鸣责任不扩展到投放燥阳谷或长期毁阵。",
        "source_evidence": "“记录里也没写是你放的。”许苛道，“甜根囊解释压石，不解释燥阳谷由谁投入暖槽。现有材料不能认定你亲手投放，更不能写成你长期蓄意毁阵。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "investigating",
        "belief": "错路时段与四升缺口相合，现有事实进一步不支持陆宁私加燥阳谷，但尚未最终验收，试用资格继续冻结。",
        "supersedes_fact_ids": [],
        "change": "许苛进一步削弱陆宁私加燥阳谷嫌疑，但仍未最终结案。",
        "source_evidence": "许苛盖下小印，又看向陆宁：“错路时段与四升缺口相合，现有事实进一步不支持你私加燥阳谷。但尚未最终验收，你的试用资格继续冻结。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "tool-sweet-root-contamination",
        "state": "knows",
        "belief": "施工器具受甜根气味污染，贪食豚沿污染器具移动，妨碍隔栏定位；清洗后贪食豚未再跟随施工路线。",
        "supersedes_fact_ids": [],
        "change": "乔穗将贪食豚跟随施工路线的现象正式改记为工具甜根气味污染。",
        "source_evidence": "她立即划掉前一句，改记：“施工器具受甜根气味污染，贪食豚沿污染器具移动，妨碍隔栏定位。”"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "beast-breath-limited-scope",
        "state": "knows",
        "belief": "本次听息只可辨节奏，不得扩听，不得借兽息判断谁投料或谁说谎。",
        "supersedes_fact_ids": [],
        "change": "陆宁明确遵守许苛划定的听息诀使用边界。",
        "source_evidence": "“你先前已停止整群听息，休养数日，也用过一条封耳条。今日只做单兽低强度校验。”他指向远栏，“不得扩听，不得借兽息判断谁投料、谁说谎。”\n\n陆宁盘膝坐在栏外：“只辨节奏。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trough-array-initial-test",
        "state": "knows",
        "belief": "食槽阵空槽初试中，暖槽按原定阵路滑向豚栏外接料位，没有偏向云蹄鹿东槽；初试通过，最终验收明日做。",
        "supersedes_fact_ids": [],
        "change": "许苛掌握食槽阵修复后的初试结果，但最终验收仍未完成。",
        "source_evidence": "空槽试送时，许苛亲自拨动饲铃牌。\n\n一声，冷槽阵纹亮起。二声，分槽轮转。三声之后，暖槽木斗沿原定阵路滑向豚栏外的接料位，没有偏向云蹄鹿东槽。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "knows",
        "belief": "现有证据不能证明陆宁私加燥阳谷；燥阳谷是经食槽阵错路进入鹿栏，先前对陆宁私自投放燥阳谷的误信已被纠正。",
        "supersedes_fact_ids": [
          "lu-ning-secret-yang-feed-review"
        ],
        "change": "许苛正式裁定纠正陆宁私加燥阳谷的误信。",
        "source_evidence": "“上述记录、铃序、份量与残留路线，足以纠正先前对你私自投放燥阳谷的误信。燥阳谷经食槽阵错路进入鹿栏。现有证据，不能证明你私加燥阳谷。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "he-ming-not-yang-feed-caster",
        "state": "knows",
        "belief": "贺鸣的责任限于私用甜根囊、漏记耗用、诱引贪食豚压石；现有证据不认定他投放燥阳谷，也不认定为长期毁阵。",
        "supersedes_fact_ids": [
          "he-ming-not-yang-feed-caster"
        ],
        "change": "许苛正式限定贺鸣责任边界，没有扩展为投放燥阳谷或长期毁阵。",
        "source_evidence": "许苛继续道：“贺鸣之责，止于私用甜根囊、漏记耗用、诱引贪食豚压石。记过、清理赔工及隔栏安装照旧。现有证据不认定他投放燥阳谷，也不作长期毁阵论处。”"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trial-qualification-result",
        "state": "knows",
        "belief": "陆宁试用资格由冻结改为通过条件审查，但临时饲兽牌附带两日不得整群听息、单兽低强度校验须报备等条件。",
        "supersedes_fact_ids": [
          "trial-qualification-result"
        ],
        "change": "许苛完成陆宁试用资格条件审查并给出结果。",
        "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-record-format",
        "state": "knows",
        "belief": "白绒的表现只能登记为槽温、气味、进食位置、蹄印方向和是否进食等可验材料，不能写成灵兽证词或拟人签收。",
        "supersedes_fact_ids": [
          "white-tuft-record-format"
        ],
        "change": "乔穗把白绒拟人化记录改为可验记录格式。",
        "source_evidence": "乔穗写道：“白绒愿意签收西槽——”\n\n许苛的目光扫过来。\n\n她立刻接下去：“即西槽槽温凉，无燥阳谷甜燥气，进食位置距槽口一尺二寸，蹄印由东向西，东槽未进食。”"
      }
    ],
    "thread_changes": [
      {
        "change": "燥阳谷残留调查正式启动，下一步要核青穗草与燥阳谷出库份量并复走三声铃。",
        "source_evidence": "许苛收起封存瓶，将饲铃牌上的异常亮痕拓印下来：“鹿群今日拒食未解。入夜前核完青穗草与燥阳谷出库份量，晚间重走三声铃。谁少报一次动作，便从头复述。”"
      },
      {
        "change": "陆宁今夜将在监督下复核封存残留、铃序和鹿栏安抚流程。",
        "source_evidence": "许苛转向陆宁：“今夜在我或指定弟子监督下，复核封存残留、铃序和鹿栏安抚流程。你的听息回声眩晕尚在，方才只听数息，耳鸣也没避过。”"
      },
      {
        "change": "鹿群拒食仍未解决，成为晚间复核和安抚流程的紧迫问题。",
        "source_evidence": "许苛收起封存瓶，将饲铃牌上的异常亮痕拓印下来：“鹿群今日拒食未解。入夜前核完青穗草与燥阳谷出库份量，晚间重走三声铃。谁少报一次动作，便从头复述。”"
      },
      {
        "change": "陆宁在宵禁后违规入栏查看鹿群拒食变化。",
        "source_evidence": "监督复核已经结束，许苛临走前封了中槽，也重申过禁令。按规矩，此刻陆宁该回试舍。\n\n白绒忽然晃了一下，前膝几乎碰到地面。\n\n陆宁推门入栏。"
      },
      {
        "change": "陆宁为避开白绒惊跳而擅自改变安抚铃顺序，饲铃牌留下右、左、中错铃记录。",
        "source_evidence": "他抬手先敲了右铃。\n\n清响荡过栏顶。\n\n饲铃牌上，一道银纹随即亮起，右侧槽位下方也闪过一线微光。\n\n乔穗脸色变了：“顺序错了。”"
      },
      {
        "change": "暖性残留与错位铃声共同刺激鹿群，拒食升级为冲栏，柔缰引导无法压制整群。",
        "source_evidence": "白绒从中槽边横窜，鹿群被它带得挤向栏门。暖性残留令几只鹿呼吸发急，错位的铃声又把它们引向相反方向。前鹿想退，后鹿仍在向前，鹿角与栏木接连擦响。\n\n陆宁甩出柔缰。\n\n两缕低强度灵气绕上最前方两只鹿的肩颈，将它们往侧道牵。它们偏开半步，后方鹿群一拥，两缕柔缰当即绷直。陆宁手腕一沉，鞋底被拖过湿草，掌中灵气也被冲势震得断续。\n\n炼气二层的柔缰能改小兽方向，压不住整群冲势。"
      },
      {
        "change": "乔穗发现通向食槽阵压力石旁的非鹿圆钝压痕，为后续追查压力石受压留下入口。",
        "source_evidence": "尺端忽然停住。\n\n泥里有一串圆钝压痕，边缘宽厚，没有分瓣，不是云蹄鹿留下的。压痕从中槽后方斜穿清理道，一直没入食槽阵的石廊。\n\n乔穗挪过灯盏，顺着最后两枚压痕照去。\n\n它们正停在那块压力石旁。"
      },
      {
        "change": "后续核查被拆分为压力石受压记录、饲铃牌异常铃序和燥阳谷残留路线三条线索。",
        "source_evidence": "“第一张，只记压力石：压痕尺寸、泥层、草根倒向，另查受压时长。”\n\n“第二张，只记饲铃牌：哪一铃异常，触发哪个槽位。饲铃牌不记敲铃者，别擅自添名字。”\n\n“第三张，只记燥阳谷残留：中槽、槽缝、阵路沿途各有多少，气味和颗粒往哪边递减。”"
      },
      {
        "change": "下一步将先对白日压力石受压记录进行核查，再与贪食豚栏蹄垫痕对照；若尺寸不合，此线索将被划掉。",
        "source_evidence": "“明日白日，先对压力石受压记录，再对贪食豚栏蹄垫痕。若尺寸不合，这条线便划掉。”"
      },
      {
        "change": "食槽阵复核确认压力石持续受压会导致暖槽偏向鹿栏，解除压力后阵路复位，但昨夜具体压石对象和原因未定。",
        "source_evidence": "许苛将三次结果写进阵录：“持续受压，暖槽偏向鹿栏；解除压力，阵路复位。错送可能存在。至于昨夜压石的是不是这只、为何停留，尚不能定。”"
      },
      {
        "change": "压力石不识别压石对象，只记录重量和持续时间。",
        "source_evidence": "许苛扫过她的纸：“删掉‘对象’二字。压力石只记重量和时长，不认压它的是豚、石墩还是人。”"
      },
      {
        "change": "乔穗完成暖槽偏移路线图，并被安排午后清理贪食豚栏和压力石周边，泥印、草屑分别留样。",
        "source_evidence": "许苛指向贪食豚栏：“能。画图的人最熟压痕与阵沟，午后清豚栏，再刷压力石周边。泥印、草屑分别留样。”"
      },
      {
        "change": "压力石周边发现疑似诱引线索，下一步转向甜根囊领用册核查。",
        "source_evidence": "泥水下露出几缕黏在阵沟边的淡黄纤维，带着一丝不属于普通草料的甜气。\n\n许苛俯身看了一眼，没有触碰。\n\n“分袋留样。”他道，“再去取甜根囊领用册。”"
      },
      {
        "change": "调查主线从单查陆宁私加燥阳谷，推进为三段证据链：甜根囊去向、贪食豚停留、暖槽错路时段重合。",
        "source_evidence": "“从今日起，不再只复查陆宁是否私加燥阳谷。”许苛道，“分三段查。甜根囊从领出到耗用去了哪里；贪食豚昨夜停在何处、停了多久；暖槽错路是否与受压时段重合。”"
      },
      {
        "change": "下一步复核要求贺鸣写清甜根囊离开账房后的完整路径；若记不清，则从豚栏残留查起。",
        "source_evidence": "许苛转向贺鸣：“下一次复核前，写清甜根囊离开账房后的完整路径。哪一道门，哪一段过道，何时开袋，余料如何处置。”\n\n贺鸣盯着压力石旁那只甲三袋，半晌才道：“若我记不清呢？”\n\n许苛将领用册合上。\n\n“那就去你的豚栏，从残留开始记。”"
      },
      {
        "change": "甜根囊诱使贪食豚停留压力石的证据链成立，但不证明昨夜压石对象有意破坏阵路。",
        "source_evidence": "许苛收起记时片：“少量甜根囊残味，足以诱使贪食豚靠近并停留压力石。只证诱因可行，不证明昨夜压石对象有意破坏阵路。”"
      },
      {
        "change": "贺鸣投放燥阳谷和长期蓄意破坏均暂未被认定。",
        "source_evidence": "许苛翻出处置册：“贺鸣，诱引饲料去向违规，待处置。私下引贪食豚停在压力石附近，记入后续对照。暂不认定你投放燥阳谷，也不扩作长期蓄意破坏。”"
      },
      {
        "change": "下一步调查固定为压力石持续受压时长、饲铃牌异常铃序、燥阳谷残留路线三表同案复核。",
        "source_evidence": "许苛扣上木匣：“明早，三表同案复核。”"
      },
      {
        "change": "三表复核已启动并合成同一张复核表，裁定标准限定为时辰、铃次、槽位和份量。",
        "source_evidence": "许苛压上镇纸：“合成一张复核表。只对时辰、铃次、槽位、份量。谁看着可疑，不入表。”"
      },
      {
        "change": "压力石受压、异常三声铃和暖槽偏鹿栏残留路线已在时间与阵路上对齐，但只推进到暖料有错送路径。",
        "source_evidence": "许苛核过三处：“压力石持续受压，覆盖异常三声铃后的暖槽偏移。残留路线，也与暖槽偏向鹿栏的阵路一致。到这里，只能说明暖料有错送路径。”"
      },
      {
        "change": "陆宁擅改安抚铃被拆分为异常三声铃之后的单独违规，不再作为异常三声铃起点。",
        "source_evidence": "“这声是你的违规。”许苛道，“宵禁后入栏、擅改安抚铃，照记。却不是异常三声铃的起点。”"
      },
      {
        "change": "下一步调查转入燥阳谷份量缺口核定，需开原料库册。",
        "source_evidence": "“明日开原料库册。我要看错路那一刻，究竟少了多少燥阳谷。”"
      },
      {
        "change": "调查从确认错送路径推进到燥阳谷四升缺口可由异常铃后暖槽错路出料解释。",
        "source_evidence": "许苛将算盘拨到最后一位：“异常三声铃后，暖槽出料四升。鹿栏东槽及偏送阵路复称三升八合。二合为沿路损耗。库中短少四升，与该次出料相符。”"
      },
      {
        "change": "许苛将甜根囊去向、压力石受压时段、异常铃序和燥阳谷缺口并入下一步合案材料。",
        "source_evidence": "廊外，临时横撑被风吹得轻响。许苛将甜根囊去向、压力石受压时段、异常铃序与四升燥阳谷缺口并排夹入同一册，压上木签。\n\n“明日按铃次合案。谁让压力石压住，谁让暖槽错路，各算各的。”"
      },
      {
        "change": "压力石受压、异常三声铃、燥阳谷出料复称与甜根囊去向已被许苛按同一时辰线合并。",
        "source_evidence": "第一张，压力石自亥初二刻起持续受压。第二张，亥初三刻出现异常三声铃，暖槽阵路偏向鹿栏。第三张，燥阳谷出料四升，鹿栏与偏送阵路复称三升八合，余二合为沿路损耗。第四张，贺鸣于亥初前领走甜根囊一袋，未记耗用，残囊留在压力石旁。\n\n许苛用朱笔将四处时辰连成一线：“贺鸣，复述。”"
      },
      {
        "change": "食槽阵错接阵槽被拆修，导槽与压力石被校正，防豚隔栏因横撑阻挡改位安装。",
        "source_evidence": "器具归净，施工重新开始。贺鸣先铲掉压力石边凝结的泥和甜根碎屑，再拆开偏接阵槽。陆宁不能猛转身搬重件，便沿阵纹逐段报位。\n\n“左侧导槽高半指。”\n\n贺鸣垫平槽脚。\n\n“压力石回弹迟一息。”\n\n乔穗清出石缝细砂，贺鸣重新校紧承簧。"
      },
      {
        "change": "食槽阵空槽初试显示暖槽未再偏向云蹄鹿东槽，初试通过，最终验收推至明日。",
        "source_evidence": "“初试通过，最终验收明日做。”"
      },
      {
        "change": "下一章将进行验阵、燥阳谷责任结论宣告和临时饲兽牌再审。",
        "source_evidence": "“你的试用冻结不解除。”许苛合上伤势册，将食槽阵初试记录、栏门赔偿单和责任卷并排放好，“明日验阵、宣告燥阳谷责任结论，再审临时饲兽牌。”"
      },
      {
        "change": "食槽阵错路线索完成闭环：压力石记录、饲铃牌异常铃序、燥阳谷残留路线、份量缺口和甜根囊领用去向共同支撑最终责任结论。",
        "source_evidence": "“压力石持续受压记录，与饲铃牌异常铃序覆盖时段相合；燥阳谷残留路线与错接阵路相合；原料库四升份量缺口，与暖槽错送量相合；甜根囊领用去向，证明贺鸣曾诱引贪食豚停留压力石，造成错路条件。”"
      },
      {
        "change": "陆宁私加燥阳谷的审查线结案为不成立，但陆宁违规入栏、错铃、栏门铰损坏等责任继续保留。",
        "source_evidence": "“顺序无误。”许苛把违规册推回去，“私加燥阳谷不成立，不等于这三项消失。”"
      },
      {
        "change": "陆宁的栏门铰修理工时和赔偿从口头安排落实为文书条件。",
        "source_evidence": "陆宁在损坏单末尾按下指印。墨迹落定，修理工时与赔偿便不再只是口头安排。"
      }
    ],
    "comedy_changes": [
      {
        "change": "乔穗把白绒避槽称为指认，被陆宁纠正为不能给鹿安身份。",
        "source_evidence": "乔穗立刻放下空桶：“白绒指认中槽。”\n\n“先别给它安身份。”"
      },
      {
        "change": "乔穗把白绒嗅空桶解读为证物清白，被陆宁改成空桶无暖味、白绒主动嗅闻的记录。",
        "source_evidence": "乔穗抬头：“它选了证物。”\n\n“桶里什么都没有。”\n\n“所以清白。”\n\n陆宁把桶翻过来给她看：“它只是闻到桶洗过，没有那股暖味。记空桶无异味，白绒愿意靠近。”"
      },
      {
        "change": "许苛把乔穗的拟人化证词说法转化成清点全部蹄印的苦差。",
        "source_evidence": "乔穗望着满地交叠的鹿蹄印，抱紧册子：“它的证词略显繁复。”\n\n“所以让你清点。”"
      },
      {
        "change": "乔穗把安抚铃戏称为“白绒同意铃”，但鹿群实际躁动使这个说法失效。",
        "source_evidence": "乔穗盯着那三道纹：“这不是白日的安抚铃。”\n\n“我知道。”\n\n“我原先还想叫它‘白绒同意铃’。”\n\n“它现在不同意。”"
      },
      {
        "change": "乔穗把白绒受惊后的走法比作证人改口，被许苛压回量尺记录。",
        "source_evidence": "“它方才受惊，前后走法不一样，像是证人改了口。”\n\n“闭嘴，量尺。”"
      },
      {
        "change": "乔穗将白绒行为拟人化为态度、失望和拒绝签字，被许苛要求删除。",
        "source_evidence": "乔穗低头看自己的纸。上面第一行写着“白绒态度坚决”，第二行写着“白绒对中槽深感失望”。\n\n她默默把两行划掉，问：“那‘拒绝签字’呢？”\n\n“也删。”"
      },
      {
        "change": "许苛用分项记录规则纠正乔穗把灵兽行为直接拼成责任人的做法。",
        "source_evidence": "乔穗问：“白绒的拒食放哪张？”\n\n“另纸。它能证明自己避了什么，不能替你们把三张纸缝成一个人。”"
      },
      {
        "change": "贪食豚把压力石当暖垫趴住，还翻面继续取暖，直接触发严肃阵路复核结果。",
        "source_evidence": "灰背贪食豚被铜片声吵醒，换了个方向，把另一面肚皮贴上压力石。赤纹因此更亮，鹿栏铜槽又升了一分温。\n\n陆宁道：“它在翻面。”\n\n乔穗认真记下：“压石对象翻面后，槽温继续上升。”"
      },
      {
        "change": "乔穗把贪食豚当“证人”的说法被许苛纠正为它只是睡觉造成阵路偏移。",
        "source_evidence": "“它没作证。”许苛道，“它只睡了一觉。你记录的是这一觉压坏了哪条路。”"
      },
      {
        "change": "乔穗把留样分袋说成证物沐浴，被陆宁纠正为晾干、分袋，并因留样不合规被许苛罚重清压力石沟。",
        "source_evidence": "乔穗抱着三只留样袋站在桌边，小声道：“淡黄纤维在甲袋，草屑在乙袋，泥印刮样在丙袋。证物已经分开沐浴过了。”\n\n陆宁看了她一眼：“是晾干、分袋，没有沐浴。”\n\n“可我洗了两遍阵沟。”\n\n许苛头也不抬：“所以不合规。”"
      },
      {
        "change": "贺鸣用“顺手”概括甜根囊去向，被许苛、乔穗和陆宁用账册规则压回具体路径。",
        "source_evidence": "“账册也没让你量每一步。它只让你说明，一袋诱引饲料去了哪里。你写的是换栏，不是散失，不是遗落，更不是‘顺手’。”\n\n乔穗认真道：“领用册不认顺手。”\n\n陆宁补了一句：“也不认大概。”"
      },
      {
        "change": "贪食豚绕过贺鸣柔缰指令，只按甜味行动，直接验证甜根囊诱因。",
        "source_evidence": "贺鸣将柔缰绳引向贪食豚颈侧。贪食豚懒洋洋走出两步，木钳上的甜气一飘，它鼻子猛地贴地，圆身一拐，绕过柔缰牵出的弧线，直奔压力石。\n\n“左！”贺鸣喝道。\n\n贪食豚向右。\n\n“停！”\n\n它倒真停了，前蹄压住压力石边缘，腹侧贴上石面，鼻子还往木钳下拱。石下铜片轻响，许苛立即按住阵盘，截断槽路灵纹。"
      },
      {
        "change": "贪食豚蹭乱乔穗刚描好的泥线，造成乔穗需要重描并分栏记录。",
        "source_evidence": "乔穗扑过去描泥线。贪食豚闻见她袖口沾了残味，顺势一蹭，刚画出的半圈蹄印顿时糊成一团。\n\n她握着竹签僵了片刻：“它重走昨夜路径，还把脚迹收回去了。”\n\n“复核路线，不是昨夜路径；蹭乱，不是收回。”许苛道，“重描，分栏记。”"
      },
      {
        "change": "乔穗将白绒避槽拟人化为不肯签字，许苛因此在复核表增加“不得写感想”栏。",
        "source_evidence": "乔穗探头念道：“不得写感想。”\n\n“正是。”\n\n“可它确实不认这口锅。”"
      },
      {
        "change": "乔穗试图继续给白绒行为加拟人化评语，但被“不得写感想”栏迫使改成客观记录。",
        "source_evidence": "她刚想在末尾添一句“态度坚决”，瞥见那列新字，只得改成“中途未回东槽”。"
      },
      {
        "change": "乔穗因表格禁写感想而把白绒行为记录为不作责任判断。",
        "source_evidence": "乔穗看了看许苛新添的那一列，老实写下：白绒接近无燥阳谷气味的袖侧，未进食；此举不作责任判断。"
      },
      {
        "change": "乔穗把白绒避槽写成“拒绝签收”，被许苛纠正为证据化记录。",
        "source_evidence": "乔穗抱着三只编号残留袋挤到案前，把最上面一只放下：“东槽一号，白绒拒绝签收。”\n\n许苛笔尖停住。\n\n乔穗立即改口：“东槽一号，槽底暖料残留。白绒于东槽前三尺停步，未进食，蹄印转向西槽。”"
      },
      {
        "change": "乔穗再次险些把白绒拒食写成拟人化拒绝，被迫改成停步、未进食、进食位置和行进方向。",
        "source_evidence": "乔穗的笔已经落下：“白绒再次拒绝在东槽——”\n\n她停了停，自己划掉后半句，改成：“东槽前停步一次，未进食；西槽进食。行进方向与昨日踏痕相合。”"
      },
      {
        "change": "燥阳谷四升缺口被喜剧化为“没有凭空长腿”，但正式记录仍写食槽阵偏送。",
        "source_evidence": "乔穗抱起筛过的垫草：“所以那四升没有凭空长腿。”\n\n“阵路替它走了。”陆宁道。\n\n许苛合上小秤：“写食槽阵偏送，不写谷有腿。”"
      },
      {
        "change": "乔穗一度把贪食豚跟随贺鸣施工记录成监督赔工，后被陆宁纠正为追甜根味。",
        "source_evidence": "乔穗提笔：“贪食豚监督赔工，态度严谨。”\n\n陆宁扶住阵台，避免转身过快：“它追的是甜根味，不是工时。”"
      },
      {
        "change": "贺鸣因自己诱引贪食豚的违规行为，被许苛用一句话指定负责清洗工具并把猪挡在压力石外。",
        "source_evidence": "贺鸣看着一筐工具：“都洗？”\n\n“会引猪的人，负责把猪挡在外面。”"
      },
      {
        "change": "乔穗把贪食豚清洗后未再跟随施工路线精确记为三息，因为第四息贪食豚去找吃的，不归工具污染记录。",
        "source_evidence": "乔穗在器具栏后添了一句：“清洗后三息内，贪食豚未再跟随施工路线。”\n\n“为何只记三息？”贺鸣问。\n\n“第四息它去找吃的了。那不归工具管。”"
      },
      {
        "change": "乔穗把白绒进食拟人化写成“愿意签收”，被迫改成可验数据。",
        "source_evidence": "乔穗写道：“白绒愿意签收西槽——”\n\n许苛的目光扫过来。\n\n她立刻接下去：“即西槽槽温凉，无燥阳谷甜燥气，进食位置距槽口一尺二寸，蹄印由东向西，东槽未进食。”"
      },
      {
        "change": "陆宁严肃把白绒的兽息结果翻译成不能夸自己的验收用语。",
        "source_evidence": "许苛问：“结果。”\n\n“能咽，不热，不是夸我。”"
      },
      {
        "change": "乔穗把临时牌条件念得像给白绒排班，被许苛纠正临时牌只管陆宁。",
        "source_evidence": "乔穗抱着归档册在一旁低声念：“陆宁，白日饲兽；白绒，西槽进食；两日内双方不得发生整群听息——”\n\n许苛抬眼：“临时牌只管陆宁，不给白绒排班。”"
      }
    ],
    "new_constraints": [
      {
        "change": "饲铃牌异常只可作为复核项，不能单独证明敲铃者或定责。",
        "source_evidence": "许苛敲了敲饲铃牌：“牌只记铃序和触发槽位，不记敲铃的人。这一次异常与你值守相邻，是复核项，不是定责。”"
      },
      {
        "change": "中槽燥阳谷残留只证明燥阳谷到过该槽，不证明投放者。",
        "source_evidence": "“初闻是。”许苛将残留装瓶，封纸压印，“只说明燥阳谷到过这只槽，不说明谁放的。封存，核份量。”"
      },
      {
        "change": "灵兽亲近或避开某人不作为免责或定责证据，后续裁定只看铃序、饲料份量和兽栏后果。",
        "source_evidence": "许苛封好瓷瓶：“亲近不抵一粒谷，避开也不抵一声铃。后续我只看铃序、饲料份量和兽栏后果。”"
      },
      {
        "change": "陆宁晚间复核听息与鹿栏流程必须在许苛或指定弟子监督下进行。",
        "source_evidence": "许苛转向陆宁：“今夜在我或指定弟子监督下，复核封存残留、铃序和鹿栏安抚流程。你的听息回声眩晕尚在，方才只听数息，耳鸣也没避过。”"
      },
      {
        "change": "鹿栏门铰裂损不可当场恢复，今夜只能临时加固，明日起报修，陆宁要参与修料、工时与赔偿核算。",
        "source_evidence": "“铰片裂损，当场不能恢复。今夜只能临时加固，明日起报修。修料、工时与赔偿，你参与核算。”"
      },
      {
        "change": "陆宁试用资格冻结，复核前不得独立值栏。",
        "source_evidence": "“宵禁入栏，擅改一次安抚铃序，处置不当致栏门铰损坏。扣贡献二点，余四点。试用资格冻结，复核前不得独立值栏。”"
      },
      {
        "change": "陆宁被另记超限施术，solo-night-listening-ban 继续有效。",
        "source_evidence": "许苛看了他一眼：“听息回声加重，方向错判。禁令仍在，另记超限施术。”"
      },
      {
        "change": "陆宁获得的复查机会受限于白日、有监督、不得听整群兽息、不得独立触动食槽阵，夜间禁令继续有效。",
        "source_evidence": "许苛合上簿册，“复查准许。只限白日，须我或同组弟子在场，不得听整群兽息，不得独立触动食槽阵。夜间禁令照旧。”"
      },
      {
        "change": "陆宁今日承担半个时辰临时加固工时，但不能抵扣已扣除的二点贡献。",
        "source_evidence": "“明白便记工。今日半个时辰，不抵扣那二点贡献。”"
      },
      {
        "change": "圆钝压痕只能记录为与贪食豚栏常见蹄垫痕相似，不能确认具体灵兽或引导者。",
        "source_evidence": "“压力石认重量和持续时间，不认蹄子，更不认引导者。”他说，“压痕与贪食豚栏常见蹄垫痕相似，只能记相似。不得定哪只豚，也不得定谁带来的。”"
      },
      {
        "change": "复核期间陆宁只能报槽位，不能碰铃或动阵栓；再认错方向即停。",
        "source_evidence": "许苛看了一眼漏刻：“复核期间，你只准报槽位，不准碰铃，不准动阵栓。若再认错方向，立即停。”"
      },
      {
        "change": "陆宁进行听息校验时只能听单只白绒十息，不能扩到鹿群，也不能借呼吸猜人。",
        "source_evidence": "陆宁坐在隔绳外，双手压膝：“只听它一只，十息。若有方向错判，立刻停。”\n\n许苛站在他右后方：“不得扩到鹿群。不得借呼吸猜人。说节奏，不说心思。”"
      },
      {
        "change": "陆宁错铃、宵禁入栏仍不因阵路错送机制而取消。",
        "source_evidence": "“仍查。”许苛合上阵录，“阵路能把暖料送错，不等于昨夜一定如此；更不等于你的错铃、宵禁入栏可以不算。”"
      },
      {
        "change": "陆宁栏门损坏责任、已扣二点贡献、试用冻结和夜间独自整群听息禁令均继续保留。",
        "source_evidence": "陆宁看着那三句：“栏门损坏也不抵。”\n\n“二点贡献也不退，余额仍是四点。试用冻结照旧。”许苛道，“你方才耳鸣减轻，只算恢复苗头。眩晕未除，夜间独自整群听息禁令继续。”"
      },
      {
        "change": "乔穗必须重做甲袋编号，写明取样次序，并重新清理压力石沟。",
        "source_evidence": "“第一遍清出的纤维混了草屑，第二遍才分袋。甲袋重做编号，写明取样次序。压力石沟再清一遍。”"
      },
      {
        "change": "贺鸣不得补写旧记录，并需随时接受甜根囊去向核问。",
        "source_evidence": "“腿不记账，人记。”许苛在领用条目旁落下一笔，“去向待核。你随时听问，不得补写旧记录。”"
      },
      {
        "change": "本次纤维比对只能写气味、形态和留样位置，不能把相近写成同一。",
        "source_evidence": "“去压力石。只比气味、形态和留样位置。谁敢把相近写成同一，今日便陪乔穗再清一遍沟。”"
      },
      {
        "change": "陆宁宵禁入栏、错铃、栏门铰损坏仍另册记录；贡献点已扣二点不退，余额仍为四点。",
        "source_evidence": "“这不代表你已洗清。宵禁入栏、错铃、栏门铰损坏另册照记。试用资格继续冻结，扣去的二点不退，余额四点。”"
      },
      {
        "change": "陆宁宵禁入栏、擅改铃序、栏门铰损坏责任仍另册保留。",
        "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
      },
      {
        "change": "陆宁已扣除的二点贡献不退，贡献点余额仍为四点，试用资格继续冻结。",
        "source_evidence": "他转向陆宁：“今日新证据削弱了你私加燥阳谷的嫌疑，但还不能定结。宵禁入栏、擅改铃序、栏门铰损坏另册照记。二点贡献不退，余额四点，试用资格继续冻结。”"
      },
      {
        "change": "复核只使用外袋残味，不开启新甜根囊，不允许暖槽起阵。",
        "source_evidence": "许苛合上册子：“现场复核。只用外袋残味，不开新料，不许暖槽起阵。”"
      },
      {
        "change": "复核表只能按时辰、铃次、槽位、份量记录，不按人看起来可疑定责。",
        "source_evidence": "许苛压上镇纸：“合成一张复核表。只对时辰、铃次、槽位、份量。谁看着可疑，不入表。”"
      },
      {
        "change": "陆宁当日听息校验限制为白日、单兽、低强度，只校验白绒，耳鸣加重即停。",
        "source_evidence": "许苛特意让陆宁站在横撑外：“白日，单兽，低强度。只校验白绒。若耳鸣加重，立刻停。”"
      },
      {
        "change": "陆宁试用冻结、扣点、宵禁、错铃、栏门修理与赔偿责任继续保留；贡献点余额仍为四点。",
        "source_evidence": "陆宁问：“试用冻结呢？”\n\n“不解。二点贡献不退，余额四点。宵禁、错铃另册。栏门铰未修，修理与赔偿照旧。”"
      },
      {
        "change": "陆宁回声眩晕未解除，夜间独自整群听息禁令继续有效，封耳条继续戴，今日不得再校验第二只。",
        "source_evidence": "“回声眩晕只记部分恢复，未解除。夜间独自整群听息禁令照旧。封耳条继续戴，今日不得再校验第二只。”"
      },
      {
        "change": "陆宁私投燥阳谷暂不成立，但宵禁后入栏、擅改一次安抚铃、栏门铰损坏、修理赔偿、扣点和试用资格冻结全部保留。",
        "source_evidence": "许苛将另一册推到他面前：“私投燥阳谷暂不成立，不等于宵禁后入栏无事。你擅改一次安抚铃，记录保留；阻栏处置不当，栏门铰损坏，修理与赔偿保留；已扣二点贡献不退，余额四点；试用资格继续冻结。”"
      },
      {
        "change": "陆宁当日不得再校验第二只灵兽。",
        "source_evidence": "许苛皱眉：“坐回去。今日不得再校验第二只。”"
      },
      {
        "change": "乔穗需重抄复称记录、重新筛净三只残留袋并清理鹿栏。",
        "source_evidence": "乔穗刚松开抱着的残留袋，许苛便把两叠纸递给她：“复称记录重抄一份，三只袋重新筛净。鹿栏清理也归你。”"
      },
      {
        "change": "压力石区以后只准使用无诱引气味工具。",
        "source_evidence": "许苛扫过记录：“停工。器具全洗。以后压力石区只准用无诱引气味工具。”"
      },
      {
        "change": "陆宁自今日起两日内不得对整群使用听息诀；单兽低强度使用仍须报备。",
        "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
      },
      {
        "change": "陆宁的后续栏门修理工时与赔偿将写入临时饲兽牌条件审查。",
        "source_evidence": "“食槽阵修了，栏门没修。陆宁，后续修理工时与赔偿写入你的条件审查。”"
      },
      {
        "change": "最终验收前，每一声饲铃都必须有人核对槽位。",
        "source_evidence": "“先去看。最终验收前，任何一声铃都要有人对槽位。”"
      },
      {
        "change": "陆宁临时饲兽牌附带条件：两日内不得对整群使用听息诀，单兽低强度校验须报备。",
        "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
      },
      {
        "change": "陆宁宵禁入栏、擅改安抚铃记录保留；栏门铰修理与赔偿写入临时饲兽牌条件；后续考核仍看铃序、份量和损坏。",
        "source_evidence": "“宵禁入栏、擅改一次安抚铃，记录保留。栏门铰修理与赔偿，写入条件。后续考核仍看铃序、份量和损坏。白绒靠近你，只能记气味、蹄印和进食位置，不能替你抵一条违规。”"
      },
      {
        "change": "陆宁需参与栏门铰拆铰、校门和换件，赔偿按材料实耗核算。",
        "source_evidence": "“栏门铰未修复。你参与拆铰、校门和换件，赔偿按材料实耗核算。”"
      }
    ],
    "resolved_constraints": [
      {
        "change": "陆宁听息回声眩晕解除。",
        "source_evidence": "许苛在伤势册上写道：“经停止整群听息、使用封耳条、休养及白日监督下单兽低强度校验，听息回声眩晕解除。”"
      },
      {
        "change": "陆宁夜间不得独自对整群使用听息诀的旧禁令结束。",
        "source_evidence": "“夜间不得独自对整群使用听息诀的旧禁令随之结束。自今日起两日内，不得对整群使用听息诀。单兽低强度使用，仍须报备。”"
      },
      {
        "change": "陆宁试用资格冻结解除，改为通过条件审查。",
        "source_evidence": "“陆宁，试用资格由冻结改为通过条件审查。听息回声眩晕已经确认解除，原先夜间独自整群听息禁令随之结束。但自昨日计，两日内不得对整群使用听息诀；单兽低强度校验仍须报备。”"
      }
    ]
  },
  "structured_state": {
    "cultivation": [
      {
        "subject_id": "he-ming",
        "stage": "炼气二层",
        "abilities": [
          "柔缰引导",
          "饲料配比"
        ],
        "injuries": [],
        "limits": [
          "不能正面对抗考核管事"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "lu-ning",
        "stage": "炼气二层",
        "abilities": [
          "柔缰引导",
          "基础吐纳",
          "陆宁的听息诀继续限定在单兽低强度校验范围内，本章实际确认可通过白绒呼吸判断无受热急促滞顿、无群体惊慌乱拍，未扩听整群，也未追索气味来处。"
        ],
        "injuries": [],
        "limits": [
          "陆宁两日内不得对整群使用听息诀的限制继续生效，单兽低强度校验仍须报备。"
        ],
        "tracked_states": [
          {
            "state_id": "beast-breath-listening",
            "kind": "ability",
            "description": "陆宁的听息诀继续限定在单兽低强度校验范围内，本章实际确认可通过白绒呼吸判断无受热急促滞顿、无群体惊慌乱拍，未扩听整群，也未追索气味来处。"
          },
          {
            "state_id": "two-day-group-listening-ban",
            "kind": "restriction",
            "description": "陆宁两日内不得对整群使用听息诀的限制继续生效，单兽低强度校验仍须报备。"
          }
        ],
        "last_kind": "restriction",
        "last_change": "陆宁两日内不得对整群使用听息诀的限制继续生效，单兽低强度校验仍须报备。"
      },
      {
        "subject_id": "qiao-sui",
        "stage": "炼气一层",
        "abilities": [
          "基础吐纳",
          "灵兽日常照看"
        ],
        "injuries": [],
        "limits": [
          "不能独立处理冲栏兽群"
        ],
        "tracked_states": []
      },
      {
        "subject_id": "xu-ke",
        "stage": "炼气三层",
        "abilities": [
          "御兽苑考核",
          "食槽阵基础检修"
        ],
        "injuries": [],
        "limits": [
          "必须依据铃序、份量和正式损坏记录裁定"
        ],
        "tracked_states": []
      }
    ],
    "resources": [
      {
        "owner_id": "beast-yard",
        "resource_id": "sweet-root-pouch",
        "amount": 3.0,
        "unit": "袋",
        "last_operation": "consume",
        "last_source_or_destination": "贺鸣昨夜领出后称已用过且漏写耗用记录"
      },
      {
        "owner_id": "lu-ning",
        "resource_id": "calm-mint-leaf",
        "amount": 3,
        "unit": "片"
      },
      {
        "owner_id": "lu-ning",
        "resource_id": "contribution-point",
        "amount": 4.0,
        "unit": "点",
        "last_operation": "consume",
        "last_source_or_destination": "御兽苑考核处罚"
      },
      {
        "owner_id": "lu-ning",
        "resource_id": "ear-seal-strip",
        "amount": 1,
        "unit": "条"
      }
    ],
    "knowledge": [
      {
        "character_id": "he-ming",
        "fact_id": "sweet-root-lure",
        "state": "knows",
        "belief": "许苛只认定贺鸣甜根囊时间接近压力石受压诱因，不能证明贺鸣投放燥阳谷。",
        "last_change": "贺鸣听到许苛明确三表目前不能证明他投放燥阳谷。"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "beast-breath-limited-scope",
        "state": "knows",
        "belief": "本次听息只可辨节奏，不得扩听，不得借兽息判断谁投料或谁说谎。",
        "last_change": "陆宁明确遵守许苛划定的听息诀使用边界。"
      },
      {
        "character_id": "lu-ning",
        "fact_id": "wrong-feed-route",
        "state": "knows",
        "belief": "压力石受压覆盖异常三声铃和暖槽未复位时段，残留路线与鹿栏东槽错送路径吻合。",
        "last_change": "陆宁参与确认压力石受压时段覆盖异常铃序与暖槽未复位时段。"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "pig-pressure-stone",
        "state": "knows",
        "belief": "贪食豚持续趴在压力石上可触发暖槽阵路偏向鹿栏，但压力石只记录重量和时长，不识别压石对象。",
        "last_change": "乔穗对贪食豚压石与暖性饲料错路有关的怀疑被现场复核确认为机制事实。"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "tool-sweet-root-contamination",
        "state": "knows",
        "belief": "施工器具受甜根气味污染，贪食豚沿污染器具移动，妨碍隔栏定位；清洗后贪食豚未再跟随施工路线。",
        "last_change": "乔穗将贪食豚跟随施工路线的现象正式改记为工具甜根气味污染。"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-hoofprint-count",
        "state": "knows",
        "belief": "白绒前蹄停在东槽外两尺后绕向西侧净槽，中途未回东槽。",
        "last_change": "乔穗补上白绒东槽外停步并绕向西槽的踏痕记录。"
      },
      {
        "character_id": "qiao-sui",
        "fact_id": "white-tuft-record-format",
        "state": "knows",
        "belief": "白绒的表现只能登记为槽温、气味、进食位置、蹄印方向和是否进食等可验材料，不能写成灵兽证词或拟人签收。",
        "last_change": "乔穗把白绒拟人化记录改为可验记录格式。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "he-ming-not-yang-feed-caster",
        "state": "knows",
        "belief": "贺鸣的责任限于私用甜根囊、漏记耗用、诱引贪食豚压石；现有证据不认定他投放燥阳谷，也不认定为长期毁阵。",
        "last_change": "许苛正式限定贺鸣责任边界，没有扩展为投放燥阳谷或长期毁阵。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "lu-ning-secret-yang-feed-review",
        "state": "knows",
        "belief": "现有证据不能证明陆宁私加燥阳谷；燥阳谷是经食槽阵错路进入鹿栏，先前对陆宁私自投放燥阳谷的误信已被纠正。",
        "last_change": "许苛正式裁定纠正陆宁私加燥阳谷的误信。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "sweet-root-fiber-sample",
        "state": "knows",
        "belief": "少量甜根囊残味足以诱使贪食豚靠近并停留压力石，但这只证明诱因可行，不证明昨夜压石对象有意破坏阵路。",
        "last_change": "许苛将甜根囊纤维线索推进为甜根囊残味可诱使贪食豚停留压力石的已验证诱因。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "sweet-root-lure-review",
        "state": "knows",
        "belief": "贺鸣私用诱引饲料、漏记耗用，诱使贪食豚持续停留压力石，造成食槽阵错路条件，应记过并承担清理、安装防豚隔栏和赔工。",
        "last_change": "许苛将贺鸣甜根囊与压力石受压的核查转为正式认定和处置。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trial-qualification-result",
        "state": "knows",
        "belief": "陆宁试用资格由冻结改为通过条件审查，但临时饲兽牌附带两日不得整群听息、单兽低强度校验须报备等条件。",
        "last_change": "许苛完成陆宁试用资格条件审查并给出结果。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trough-array-initial-test",
        "state": "knows",
        "belief": "食槽阵空槽初试中，暖槽按原定阵路滑向豚栏外接料位，没有偏向云蹄鹿东槽；初试通过，最终验收明日做。",
        "last_change": "许苛掌握食槽阵修复后的初试结果，但最终验收仍未完成。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "trough-pressure-route",
        "state": "knows",
        "belief": "异常三声铃后暖槽出料四升，鹿栏东槽及偏送阵路复称三升八合，二合为沿路损耗，库中短少四升与该次出料相符。",
        "last_change": "许苛通过库册、出料与残留复称确认燥阳谷四升缺口可与错路出料核算相符。"
      },
      {
        "character_id": "xu-ke",
        "fact_id": "white-tuft-heat-discomfort",
        "state": "knows",
        "belief": "鹿对暖性余味有受热不适，与群体惊慌节奏不同；该结论不能证明投料者、昨夜具体阵路，也不能抵销陆宁错铃与宵禁违规。",
        "last_change": "许苛认可陆宁对白绒单兽低强度听息结果的有限边界，并将其纳入记录。"
      }
    ]
  },
  "next_chapter_inputs": [
    "陆宁已取得御兽苑带条件临时饲兽牌，但两日内不得对整群使用听息诀，单兽低强度校验仍须报备。",
    "陆宁试用资格冻结已解除，改为通过条件审查；私加燥阳谷不成立。",
    "陆宁宵禁入栏、擅改一次安抚铃、冲栏处置不当导致栏门铰损坏的责任仍保留。",
    "陆宁已扣二点贡献不退，原有六点，现余四点。",
    "受损鹿栏门铰未修复，临时横撑仍在；陆宁需参与拆铰、校门和换件，赔偿按材料实耗核算。",
    "食槽阵最终验收通过：空槽试送无偏移，暖槽恢复原定路线，压力石校紧，防豚隔栏可阻持续压石，铃序复核牌可用。",
    "贺鸣责任限定为私用甜根囊、漏记耗用、诱引贪食豚压石；记过、清理赔工及隔栏安装照旧，不认定为投放燥阳谷或长期毁阵。",
    "乔穗负责槽位、气味、踏痕、拒食与进食记录，兼清栏归档；陆宁负责兽息对照与铃序复核。",
    "许苛后续考核陆宁仍看铃序、份量和损坏；白绒靠近陆宁只能记气味、蹄印和进食位置，不能抵违规。"
  ],
  "deviations": [],
  "last_source_draft": "chapters/0010/draft.final.md",
  "last_source_sha256": "dce137a882885f53c9625c584528552749b34746c910ceec70b558d630ca5ac7",
  "source": "chapters/0010/state-event.json"
}
```
