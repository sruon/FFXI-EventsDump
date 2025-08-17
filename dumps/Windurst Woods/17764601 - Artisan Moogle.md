# 17764601 - Artisan Moogle

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 1360 bytes               |
| Total Events     | 2                        |
| References Count | 35                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [833](#event-833)     | 0x0001       |   1193 |            211 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x34BA      |       13498 |
|       2 | 0x34BB      |       13499 |
|       3 | 0x34BC      |       13500 |
|       4 | 0x34BD      |       13501 |
|       5 | 0x34BE      |       13502 |
|       6 | 0x26FC      |        9980 |
|       7 | 0x2710      |       10000 |
|       8 | 0x34BF      |       13503 |
|       9 | 0x34C0      |       13504 |
|      10 | 0x0004      |           4 |
|      11 | 0x0001      |           1 |
|      12 | 0x34C1      |       13505 |
|      13 | 0x34C4      |       13508 |
|      14 | 0x34C2      |       13506 |
|      15 | 0x0002      |           2 |
|      16 | 0x34C3      |       13507 |
|      17 | 0x00B4      |         180 |
|      18 | 0x34C5      |       13509 |
|      19 | 0x34C7      |       13511 |
|      20 | 0x0800      |        2048 |
|      21 | 0x0078      |         120 |
|      22 | 0x34C8      |       13512 |
|      23 | 0x34C9      |       13513 |
|      24 | 0x0010      |          16 |
|      25 | 0x34CA      |       13514 |
|      26 | 0x34CC      |       13516 |
|      27 | 0x34CD      |       13517 |
|      28 | 0x34CE      |       13518 |
|      29 | 0x34C6      |       13510 |
|      30 | 0x34CB      |       13515 |
|      31 | 0x000A      |          10 |
|      32 | 0x0003      |           3 |
|      33 | 0x34CF      |       13519 |
|      34 | 0x0063      |          99 |

## String References

- **13505**: Kupo? (Current gil: $2) [Buy a mog sack. ($1 gil)/Expand your mog sack./About mog sacks./About expansion./Do nothing.]
- **13512**: You hear the disconcerting sound of fabric being stretched to its limits...

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 833

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0001     |
| Data Size    | 1193 bytes |
| Instructions | 209        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 04 00 05 10 03  00 00 08 10 03 01 00 09   B..............
0010: 10 1E F0 FF FF 7F 6F 76  F8 FF FF 7F 2C F9 10 0F  ......ov....,...
0020: 01 F9 10 0F 01 68 61 70  30 02 01 00 00 80 00 6B  .....hap0......k
0030: 00 2B F9 10 0F 01 01 80  23 2B F9 10 0F 01 02 80  .+......#+......
0040: 23 2B F9 10 0F 01 03 80  23 2B F9 10 0F 01 04 80  #+......#+......
0050: 23 2B F9 10 0F 01 05 80  23 03 03 10 06 80 03 04  #+......#.......
0060: 10 07 80 2B F9 10 0F 01  08 80 23 2B F9 10 0F 01  ...+......#+....
0070: 09 80 23 2C F9 10 0F 01  F9 10 0F 01 68 61 70 31  ..#,........hap1
0080: 03 01 10 0A 80 43 00 43  01 03 03 00 04 10 03 03  .....C.C........
0090: 10 06 80 03 04 10 03 00  02 04 00 00 80 02 A7 00  ................
00A0: 3C 00 00 00 80 0B 80 24  0C 80 00 80 00 00 25 02  <......$......%.
00B0: 00 10 00 80 00 74 02 03  01 10 0B 80 43 00 43 01  .....t......C.C.
00C0: 03 04 00 05 10 02 09 10  00 80 80 F2 00 2C F9 10  .............,..
00D0: 0F 01 F9 10 0F 01 67 61  6B 30 2B F9 10 0F 01 0D  ......gak0+.....
00E0: 80 23 2C F9 10 0F 01 F9  10 0F 01 67 61 6B 31 01  .#,........gak1.
00F0: 71 02 02 09 10 0B 80 80  1F 01 2C F9 10 0F 01 F9  q.........,.....
0100: 10 0F 01 65 78 70 30 2B  F9 10 0F 01 0E 80 23 2C  ...exp0+......#,
0110: F9 10 0F 01 F9 10 0F 01  65 78 70 31 01 71 02 02  ........exp1.q..
0120: 09 10 0F 80 80 71 02 06  00 00 2C F9 10 0F 01 F9  .....q....,.....
0130: 10 0F 01 6A 6F 62 30 2B  F9 10 0F 01 10 80 1C 11  ...job0+........
0140: 80 23 03 01 10 0F 80 43  00 43 01 2C F9 10 0F 01  .#.....C.C.,....
0150: F9 10 0F 01 6A 6F 62 31  02 08 10 00 80 80 D4 01  ....job1........
0160: 2B F9 10 0F 01 12 80 23  2B F9 10 0F 01 13 80 3A  +......#+......:
0170: F9 10 0F 01 02 00 07 02  00 14 80 4B F9 10 0F 01  ...........K....
0180: 02 00 6F 76 F9 10 0F 01  2C F9 10 0F 01 F9 10 0F  ..ov....,.......
0190: 01 64 61 6E 32 1C 15 80  23 48 16 80 1C 15 80 2C  .dan2...#H.....,
01A0: F9 10 0F 01 F9 10 0F 01  64 61 65 32 4A F9 10 0F  ........dae2J...
01B0: 01 F0 FF FF 7F 2B F9 10  0F 01 17 80 23 6E F0 FF  .....+......#n..
01C0: FF 7F 18 80 99 F0 FF FF  7F 2B F9 10 0F 01 19 80  .........+......
01D0: 23 01 6B 02 02 08 10 0B  80 80 11 02 2B F9 10 0F  #.k.........+...
01E0: 01 1A 80 23 2C F9 10 0F  01 F9 10 0F 01 6E 65 77  ...#,........new
01F0: 30 2B F9 10 0F 01 1B 80  23 2C F9 10 0F 01 F9 10  0+......#,......
0200: 0F 01 6E 65 77 31 2B F9  10 0F 01 1C 80 23 01 6B  ..new1+......#.k
0210: 02 02 08 10 0F 80 80 6B  02 2B F9 10 0F 01 12 80  .......k.+......
0220: 23 2B F9 10 0F 01 13 80  3A F9 10 0F 01 02 00 07  #+......:.......
0230: 02 00 14 80 4B F9 10 0F  01 02 00 6F 76 F9 10 0F  ....K......ov...
0240: 01 2C F9 10 0F 01 F9 10  0F 01 64 61 6E 32 1C 15  .,........dan2..
0250: 80 2C F9 10 0F 01 F9 10  0F 01 64 61 65 32 4A F9  .,........dae2J.
0260: 10 0F 01 F0 FF FF 7F 23  01 6B 02 01 70 04 01 71  .......#.k..p..q
0270: 02 01 6D 04 02 00 10 0B  80 00 D3 03 2B F9 10 0F  ..m.........+...
0280: 01 1D 80 23 03 01 10 0F  80 43 00 43 01 03 04 00  ...#.....C.C....
0290: 05 10 02 08 10 00 80 80  CC 02 2C F9 10 0F 01 F9  ..........,.....
02A0: 10 0F 01 67 61 6B 30 2B  F9 10 0F 01 1E 80 23 53  ...gak0+......#S
02B0: F9 10 0F 01 F9 10 0F 01  67 61 6B 30 2C F9 10 0F  ........gak0,...
02C0: 01 F9 10 0F 01 67 61 6B  31 01 D0 03 02 08 10 0B  .....gak1.......
02D0: 80 80 09 03 2B F9 10 0F  01 1A 80 23 2C F9 10 0F  ....+......#,...
02E0: 01 F9 10 0F 01 6E 65 77  30 2B F9 10 0F 01 1B 80  .....new0+......
02F0: 23 2B F9 10 0F 01 1C 80  23 2C F9 10 0F 01 F9 10  #+......#,......
0300: 0F 01 6E 65 77 31 01 D0  03 02 08 10 0F 80 80 D0  ..new1..........
0310: 03 2B F9 10 0F 01 13 80  3A F9 10 0F 01 02 00 07  .+......:.......
0320: 02 00 14 80 4B F9 10 0F  01 02 00 6F 76 F9 10 0F  ....K......ov...
0330: 01 2C F9 10 0F 01 F9 10  0F 01 64 61 6E 32 1C 15  .,........dan2..
0340: 80 23 02 02 10 1F 80 00  85 03 48 16 80 1C 15 80  .#........H.....
0350: 2C F9 10 0F 01 F9 10 0F  01 64 61 65 32 4A F9 10  ,........dae2J..
0360: 0F 01 F0 FF FF 7F 2B F9  10 0F 01 17 80 23 6E F0  ......+......#n.
0370: FF FF 7F 18 80 99 F0 FF  FF 7F 2B F9 10 0F 01 19  ..........+.....
0380: 80 23 01 CD 03 2C F9 10  0F 01 F9 10 0F 01 64 61  .#...,........da
0390: 65 32 4A F9 10 0F 01 F0  FF FF 7F 2B F9 10 0F 01  e2J........+....
03A0: 1A 80 23 2C F9 10 0F 01  F9 10 0F 01 6E 65 77 30  ..#,........new0
03B0: 2B F9 10 0F 01 1B 80 23  2C F9 10 0F 01 F9 10 0F  +......#,.......
03C0: 01 6E 65 77 31 2B F9 10  0F 01 1C 80 23 01 D0 03  .new1+......#...
03D0: 01 6D 04 02 00 10 0F 80  00 2A 04 2C F9 10 0F 01  .m.......*.,....
03E0: F9 10 0F 01 68 61 70 30  2B F9 10 0F 01 02 80 23  ....hap0+......#
03F0: 2B F9 10 0F 01 03 80 23  2B F9 10 0F 01 04 80 23  +......#+......#
0400: 2B F9 10 0F 01 05 80 23  03 03 10 06 80 03 04 10  +......#........
0410: 07 80 2B F9 10 0F 01 08  80 23 2C F9 10 0F 01 F9  ..+......#,.....
0420: 10 0F 01 68 61 70 31 01  6D 04 02 00 10 20 80 00  ...hap1.m.... ..
0430: 5F 04 2C F9 10 0F 01 F9  10 0F 01 6E 65 77 30 2B  _.,........new0+
0440: F9 10 0F 01 1B 80 23 2C  F9 10 0F 01 F9 10 0F 01  ......#,........
0450: 6E 65 77 31 2B F9 10 0F  01 1C 80 23 01 6D 04 02  new1+......#.m..
0460: 00 10 0A 80 00 6D 04 01  70 04 01 6D 04 01 8E 00  .....m..p..m....
0470: 03 01 10 20 80 43 00 43  01 02 09 10 0B 80 00 A8  ... .C.C........
0480: 04 2C F9 10 0F 01 F9 10  0F 01 74 6C 6B 30 2B F9  .,........tlk0+.
0490: 10 0F 01 21 80 23 2C F9  10 0F 01 F9 10 0F 01 74  ...!.#,........t
04A0: 6C 6B 31 03 01 10 22 80  21 00                    lk1...".!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[5]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[8]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[9]
  4: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0016 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0017 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x001C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
  8: 0x0029 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x006B
  9: 0x0031 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13498*]:
    → "Capacity-challenged adventurers, come one, come all, kupo! The Mog House Management Union (MHMU) has developed the supreme solution for your storage woes!"
 10: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0039 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13499*]:
    → "Ah, another adventurer has arrived to take advantage of world-renowned moogle altruism and artisanship! Rest assured that you will not depart disappointed, my friend."
 12: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0041 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13500*]:
    → "Feast your eyes on the stylish, fashionable Mog Sack!"
 14: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0049 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13501*]:
    → "Why, it's the perfect union of form and function! Who could ask for more, kupo?"
 16: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0051 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13502*]:
    → "What's more, its carrying capacity can be customized to meet its owner's needs. Greedaloxes and Grand Greedaloxes haven't seen anything like this!"
 18: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0059 [0x03] Work_Zone[3] = 9980*
 20: 0x005E [0x03] Work_Zone[4] = 10000*
 21: 0x0063 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13503*]:
    → "And it can be yours--yes, yours!--for the low, low price of only $1 gil! Why, that's $2 gil off the moogle manufacturer's suggested retail price."
 22: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x006B [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13504*]:
    → "That's right, we at the MHMU don't care how far into debt we go this time! Why, I personally would starve to death in the streets of San d'Oria to free adventurers the world over from inventory frustration! So how about it, kupo?"
 24: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0073 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 26: 0x0080 [0x03] Work_Zone[1] = 4*
 27: 0x0085 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 28: 0x0087 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 29: 0x0089 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[4]
 30: 0x008E [0x03] Work_Zone[3] = 9980*
 31: 0x0093 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 32: 0x0098 [0x02] IF !(ExtData[1]->WorkLocal[4] <= 0*) GOTO 0x00A7
 33: 0x00A0 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=0*, condition_work_offset=1*)
 34: 0x00A7 [0x24] CREATE_DIALOG(message_id=13505*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "Kupo? (Current gil: $2) [Buy a mog sack. ($1 gil)/Expand your mog sack./About mog sacks./About expansion./Do nothing.]"
 35: 0x00AE [0x25] WAIT_DIALOG_SELECT()
 36: 0x00AF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0274
 37: 0x00B7 [0x03] Work_Zone[1] = 1*
 38: 0x00BC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 39: 0x00BE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 40: 0x00C0 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[5]
 41: 0x00C5 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x00F2
 42: 0x00CD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 43: 0x00DA [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13508*]:
    → "We go through such pains for you adventurers, and you would try to procure our products without sufficient funds, kupo? Will you not be content until every last moogle is in the poorhouse!? <Sniff>...<sob>..."
 44: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x00E2 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 46: 0x00EF [0x01] GOTO 0x0271
 47: 0x00F2 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x011F
 48: 0x00FA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 49: 0x0107 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13506*]:
    → "I'm sorry, kupo. Our special-order mog sacks are limited to one per adventurer."
 50: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x010F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "exp1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 52: 0x011C [0x01] GOTO 0x0271
 53: 0x011F [0x02] IF !(Work_Zone[9] == 2*) GOTO 0x0271
 54: 0x0127 [0x06] ExtData[1]->WorkLocal[0] = 0
 55: 0x012A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 56: 0x0137 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13507*]:
    → "Transaction complete, kupo! Say goodbye to days of rummaging through your gobbiebag, and hello to a life of haute hupoture, because you are now the proud owner of a spectacular, snazzy, state-of-the-art mog sack!"
 57: 0x013E [0x1C] WAIT(180* ticks)
 58: 0x0141 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0142 [0x03] Work_Zone[1] = 2*
 60: 0x0147 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 61: 0x0149 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 62: 0x014B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 63: 0x0158 [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x01D4
 64: 0x0160 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13509*]:
    → "Oh dear! I almost forgot the most important part, kupo!"
 65: 0x0167 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x0168 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13511*]:
    → "A little dose of moogle magic, and...voila, kupo! Your mog sack can now hold an incredible [/35/40/45/50/55/60/65/70/75/80] items!"
 67: 0x016F [0x3A] CONVERT_YAW_TO_BYTE(entity=Artisan Moogle (ID: 17764601/0x010F10F9), result_destination=ExtData[1]->WorkLocal[2])
 68: 0x0176 [0x07] ExtData[1]->WorkLocal[2] += 2048*
 69: 0x017B [0x4B] UPDATE_ENTITY_YAW(entity=Artisan Moogle (ID: 17764601/0x010F10F9), yaw=ExtData[1]->WorkLocal[2])
 70: 0x0182 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 71: 0x0183 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Artisan Moogle (ID: 17764601/0x010F10F9) Render.Flags0 and Render.Flags3 conditions are met
 72: 0x0188 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan2" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 73: 0x0195 [0x1C] WAIT(120* ticks)
 74: 0x0198 [0x23] WAIT_FOR_DIALOG_INTERACTION
 75: 0x0199 [0x48] [System] [13512*]:
    → "You hear the disconcerting sound of fabric being stretched to its limits..."
 76: 0x019C [0x1C] WAIT(120* ticks)
 77: 0x019F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dae2" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 78: 0x01AC [0x4A] Artisan Moogle (ID: 17764601/0x010F10F9) looks at LocalPlayer
 79: 0x01B5 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13513*]:
    → "There you go, kupo! And with that, it looks like I've enlarged your mog sack as far as it will go."
 80: 0x01BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 81: 0x01BD [0x6E] LocalPlayer uses emote 16*
 82: 0x01C4 [0x99] Wait for LocalPlayer animation to complete
 83: 0x01C9 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13514*]:
    → "A ripping sound? I haven't the foggiest idea what you're talking about, kupo. My, oh my, that's one stupendous mog sack you've got there!"
 84: 0x01D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 85: 0x01D1 [0x01] GOTO 0x026B
 86: 0x01D4 [0x02] IF !(Work_Zone[8] == 1*) GOTO 0x0211
 87: 0x01DC [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13516*]:
    → "I'm afraid your mog sack has reached its limits. Your gobbiebag, on the other hand, looks like it could still be tailored up in the right hands."
 88: 0x01E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x01E4 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 90: 0x01F1 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13517*]:
    → "The mog sack is a marvel of modern moogle craftsmanship, imbued with moogle magic that allows its capacity to be increased proportional to the size of your gobbiebag!"
 91: 0x01F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 92: 0x01F9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
 93: 0x0206 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13518*]:
    → "How does that work, you ask? Let's just call it a moogle and Gobbie mystery! Kupohohoho!"
 94: 0x020D [0x23] WAIT_FOR_DIALOG_INTERACTION
 95: 0x020E [0x01] GOTO 0x026B
 96: 0x0211 [0x02] IF !(Work_Zone[8] == 2*) GOTO 0x026B
 97: 0x0219 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13509*]:
    → "Oh dear! I almost forgot the most important part, kupo!"
 98: 0x0220 [0x23] WAIT_FOR_DIALOG_INTERACTION
 99: 0x0221 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13511*]:
    → "A little dose of moogle magic, and...voila, kupo! Your mog sack can now hold an incredible [/35/40/45/50/55/60/65/70/75/80] items!"
100: 0x0228 [0x3A] CONVERT_YAW_TO_BYTE(entity=Artisan Moogle (ID: 17764601/0x010F10F9), result_destination=ExtData[1]->WorkLocal[2])
101: 0x022F [0x07] ExtData[1]->WorkLocal[2] += 2048*
102: 0x0234 [0x4B] UPDATE_ENTITY_YAW(entity=Artisan Moogle (ID: 17764601/0x010F10F9), yaw=ExtData[1]->WorkLocal[2])
103: 0x023B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
104: 0x023C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Artisan Moogle (ID: 17764601/0x010F10F9) Render.Flags0 and Render.Flags3 conditions are met
105: 0x0241 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan2" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
106: 0x024E [0x1C] WAIT(120* ticks)
107: 0x0251 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dae2" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
108: 0x025E [0x4A] Artisan Moogle (ID: 17764601/0x010F10F9) looks at LocalPlayer
109: 0x0267 [0x23] WAIT_FOR_DIALOG_INTERACTION
110: 0x0268 [0x01] GOTO 0x026B

SUBROUTINE_026B:
111: 0x026B [0x01] GOTO 0x0470

SUBROUTINE_0271:
112: 0x0271 [0x01] GOTO 0x046D
113: 0x0274 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03D3
114: 0x027C [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13510*]:
    → "Looking to expand your mog sack? You've come to the right place, kupo!"
115: 0x0283 [0x23] WAIT_FOR_DIALOG_INTERACTION
116: 0x0284 [0x03] Work_Zone[1] = 2*
117: 0x0289 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
118: 0x028B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
119: 0x028D [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[5]
120: 0x0292 [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x02CC
121: 0x029A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
122: 0x02A7 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13515*]:
    → "I'm afraid your mog sack has already been enlarged to its limits. We wouldn't want to have any...fabric malfunctions, would we, kupo?"
123: 0x02AE [0x23] WAIT_FOR_DIALOG_INTERACTION
124: 0x02AF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
125: 0x02BC [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
126: 0x02C9 [0x01] GOTO 0x03D0
127: 0x02CC [0x02] IF !(Work_Zone[8] == 1*) GOTO 0x0309
128: 0x02D4 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13516*]:
    → "I'm afraid your mog sack has reached its limits. Your gobbiebag, on the other hand, looks like it could still be tailored up in the right hands."
129: 0x02DB [0x23] WAIT_FOR_DIALOG_INTERACTION
130: 0x02DC [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
131: 0x02E9 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13517*]:
    → "The mog sack is a marvel of modern moogle craftsmanship, imbued with moogle magic that allows its capacity to be increased proportional to the size of your gobbiebag!"
132: 0x02F0 [0x23] WAIT_FOR_DIALOG_INTERACTION
133: 0x02F1 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13518*]:
    → "How does that work, you ask? Let's just call it a moogle and Gobbie mystery! Kupohohoho!"
134: 0x02F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
135: 0x02F9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
136: 0x0306 [0x01] GOTO 0x03D0
137: 0x0309 [0x02] IF !(Work_Zone[8] == 2*) GOTO 0x03D0
138: 0x0311 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13511*]:
    → "A little dose of moogle magic, and...voila, kupo! Your mog sack can now hold an incredible [/35/40/45/50/55/60/65/70/75/80] items!"
139: 0x0318 [0x3A] CONVERT_YAW_TO_BYTE(entity=Artisan Moogle (ID: 17764601/0x010F10F9), result_destination=ExtData[1]->WorkLocal[2])
140: 0x031F [0x07] ExtData[1]->WorkLocal[2] += 2048*
141: 0x0324 [0x4B] UPDATE_ENTITY_YAW(entity=Artisan Moogle (ID: 17764601/0x010F10F9), yaw=ExtData[1]->WorkLocal[2])
142: 0x032B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
143: 0x032C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Artisan Moogle (ID: 17764601/0x010F10F9) Render.Flags0 and Render.Flags3 conditions are met
144: 0x0331 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dan2" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
145: 0x033E [0x1C] WAIT(120* ticks)
146: 0x0341 [0x23] WAIT_FOR_DIALOG_INTERACTION
147: 0x0342 [0x02] IF !(Work_Zone[2] == 10*) GOTO 0x0385
148: 0x034A [0x48] [System] [13512*]:
    → "You hear the disconcerting sound of fabric being stretched to its limits..."
149: 0x034D [0x1C] WAIT(120* ticks)
150: 0x0350 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dae2" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
151: 0x035D [0x4A] Artisan Moogle (ID: 17764601/0x010F10F9) looks at LocalPlayer
152: 0x0366 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13513*]:
    → "There you go, kupo! And with that, it looks like I've enlarged your mog sack as far as it will go."
153: 0x036D [0x23] WAIT_FOR_DIALOG_INTERACTION
154: 0x036E [0x6E] LocalPlayer uses emote 16*
155: 0x0375 [0x99] Wait for LocalPlayer animation to complete
156: 0x037A [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13514*]:
    → "A ripping sound? I haven't the foggiest idea what you're talking about, kupo. My, oh my, that's one stupendous mog sack you've got there!"
157: 0x0381 [0x23] WAIT_FOR_DIALOG_INTERACTION
158: 0x0382 [0x01] GOTO 0x03CD
159: 0x0385 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dae2" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
160: 0x0392 [0x4A] Artisan Moogle (ID: 17764601/0x010F10F9) looks at LocalPlayer
161: 0x039B [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13516*]:
    → "I'm afraid your mog sack has reached its limits. Your gobbiebag, on the other hand, looks like it could still be tailored up in the right hands."
162: 0x03A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
163: 0x03A3 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
164: 0x03B0 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13517*]:
    → "The mog sack is a marvel of modern moogle craftsmanship, imbued with moogle magic that allows its capacity to be increased proportional to the size of your gobbiebag!"
165: 0x03B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
166: 0x03B8 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
167: 0x03C5 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13518*]:
    → "How does that work, you ask? Let's just call it a moogle and Gobbie mystery! Kupohohoho!"
168: 0x03CC [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_03CD:
169: 0x03CD [0x01] GOTO 0x03D0

SUBROUTINE_03D0:
170: 0x03D0 [0x01] GOTO 0x046D
171: 0x03D3 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x042A
172: 0x03DB [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
173: 0x03E8 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13499*]:
    → "Ah, another adventurer has arrived to take advantage of world-renowned moogle altruism and artisanship! Rest assured that you will not depart disappointed, my friend."
174: 0x03EF [0x23] WAIT_FOR_DIALOG_INTERACTION
175: 0x03F0 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13500*]:
    → "Feast your eyes on the stylish, fashionable Mog Sack!"
176: 0x03F7 [0x23] WAIT_FOR_DIALOG_INTERACTION
177: 0x03F8 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13501*]:
    → "Why, it's the perfect union of form and function! Who could ask for more, kupo?"
178: 0x03FF [0x23] WAIT_FOR_DIALOG_INTERACTION
179: 0x0400 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13502*]:
    → "What's more, its carrying capacity can be customized to meet its owner's needs. Greedaloxes and Grand Greedaloxes haven't seen anything like this!"
180: 0x0407 [0x23] WAIT_FOR_DIALOG_INTERACTION
181: 0x0408 [0x03] Work_Zone[3] = 9980*
182: 0x040D [0x03] Work_Zone[4] = 10000*
183: 0x0412 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13503*]:
    → "And it can be yours--yes, yours!--for the low, low price of only $1 gil! Why, that's $2 gil off the moogle manufacturer's suggested retail price."
184: 0x0419 [0x23] WAIT_FOR_DIALOG_INTERACTION
185: 0x041A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
186: 0x0427 [0x01] GOTO 0x046D
187: 0x042A [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x045F
188: 0x0432 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
189: 0x043F [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13517*]:
    → "The mog sack is a marvel of modern moogle craftsmanship, imbued with moogle magic that allows its capacity to be increased proportional to the size of your gobbiebag!"
190: 0x0446 [0x23] WAIT_FOR_DIALOG_INTERACTION
191: 0x0447 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "new1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
192: 0x0454 [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13518*]:
    → "How does that work, you ask? Let's just call it a moogle and Gobbie mystery! Kupohohoho!"
193: 0x045B [0x23] WAIT_FOR_DIALOG_INTERACTION
194: 0x045C [0x01] GOTO 0x046D
195: 0x045F [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x046D
196: 0x0467 [0x01] GOTO 0x0470

SUBROUTINE_046D:
197: 0x046D [0x01] GOTO 0x008E

SUBROUTINE_0470:
198: 0x0470 [0x03] Work_Zone[1] = 3*
199: 0x0475 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
200: 0x0477 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
201: 0x0479 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x04A8
202: 0x0481 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk0" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
203: 0x048E [0x2B] Artisan Moogle (ID: 17764601/0x010F10F9) [13519*]:
    → "Ah, yes. And for being such a valued customer, here's a special present from the MHMU to you! Truly, our benevolence knows no bounds, kupo!"
204: 0x0495 [0x23] WAIT_FOR_DIALOG_INTERACTION
205: 0x0496 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk1" with entities [Artisan Moogle (ID: 17764601/0x010F10F9), Artisan Moogle (ID: 17764601/0x010F10F9)]
206: 0x04A3 [0x03] Work_Zone[1] = 99*
207: 0x04A8 [0x21] END_EVENT
208: 0x04A9 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x026E [0x01] GOTO 0x0271
# Dead code (unreachable instructions):
     0x046A [0x01] GOTO 0x046D
```
