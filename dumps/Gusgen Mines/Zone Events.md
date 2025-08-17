# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Gusgen Mines (ID: 196) |
| Block Size       | 1420 bytes             |
| Total Events     | 10                     |
| References Count | 54                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |    185 |             37 |
| [10](#event-10)          | 0x00E0       |    410 |             47 |
| [65535.3](#event-655353) | 0x027A       |    222 |             26 |
| [65535.4](#event-655354) | 0x0358       |    222 |             26 |
| [65535.5](#event-655355) | 0x0436       |     35 |              9 |
| [65535.6](#event-655356) | 0x0459       |     20 |              6 |
| [65535.7](#event-655357) | 0x046D       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x000A      |          10 |
|       4 | 0x0009      |           9 |
|       5 | 0x0046      |          70 |
|       6 | 0x008C      |         140 |
|       7 | 0x00D2      |         210 |
|       8 | 0x40FD      |       16637 |
|       9 | 0x00C8      |         200 |
|      10 | 0x0000      |           0 |
|      11 | 0x32CE0     |      208096 |
|      12 | 0xFFFE74E5  |  4294866149 |
|      13 | 0xFFFF17B2  |  4294907826 |
|      14 | 0x0241      |         577 |
|      15 | 0x0013      |          19 |
|      16 | 0x0060      |          96 |
|      17 | 0x00B4      |         180 |
|      18 | 0x1CC3      |        7363 |
|      19 | 0x1CC4      |        7364 |
|      20 | 0x00F3      |         243 |
|      21 | 0x1CC5      |        7365 |
|      22 | 0x1CC6      |        7366 |
|      23 | 0x003C      |          60 |
|      24 | 0x00C9      |         201 |
|      25 | 0x0095      |         149 |
|      26 | 0x009F      |         159 |
|      27 | 0x0003      |           3 |
|      28 | 0x00A9      |         169 |
|      29 | 0x0004      |           4 |
|      30 | 0x00B3      |         179 |
|      31 | 0x00BD      |         189 |
|      32 | 0x0006      |           6 |
|      33 | 0x0007      |           7 |
|      34 | 0x00C7      |         199 |
|      35 | 0x0008      |           8 |
|      36 | 0x00D1      |         209 |
|      37 | 0x000D      |          13 |
|      38 | 0xFFFE2777  |  4294846327 |
|      39 | 0x51A13     |      334355 |
|      40 | 0x05DC      |        1500 |
|      41 | 0xFFFE26B4  |  4294846132 |
|      42 | 0x50E7D     |      331389 |
|      43 | 0x0588      |        1416 |
|      44 | 0xFFFE0DA4  |  4294839716 |
|      45 | 0x4D97E     |      317822 |
|      46 | 0x04E1      |        1249 |
|      47 | 0xFFFE23B6  |  4294845366 |
|      48 | 0x3ABC9     |      240585 |
|      49 | 0x03E7      |         999 |
|      50 | 0x0028      |          40 |
|      51 | 0xFFFE7038  |  4294864952 |
|      52 | 0x3590B     |      219403 |
|      53 | 0x01A1      |         417 |

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 07 7F 1A  4C 00 66 01 00 F8 FF FF    ......L.f.....
0010: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0020: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0019 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0027    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      03  00 00 07 7F 1A 4C 00 66         ......L.f
0030: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0040: FF FF 7F F8 FF FF 7F 73  68 61 31 00 03 01 00 00  .......sha1.....
0050: 00 02 01 00 00 80 05 61  00 08 01 00 01 80 01 66  .......a.......f
0060: 00 08 01 00 02 80 14 01  00 03 80 07 01 00 04 80  ................
0070: 1B 03 01 00 00 00 02 01  00 00 80 05 86 00 08 01  ................
0080: 00 01 80 01 8B 00 08 01  00 02 80 14 01 00 03 80  ................
0090: 07 01 00 05 80 1B 03 01  00 00 00 02 01 00 00 80  ................
00A0: 05 AB 00 08 01 00 01 80  01 B0 00 08 01 00 02 80  ................
00B0: 14 01 00 03 80 07 01 00  06 80 1B 03 01 00 00 00  ................
00C0: 02 01 00 00 80 05 D0 00  08 01 00 01 80 01 D5 00  ................
00D0: 08 01 00 02 80 14 01 00  03 80 07 01 00 07 80 1B  ................
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x002C [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x004B [0x00] END_REQSTACK()

SUBROUTINE_004C:
  5: 0x004C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x0051 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0061
  7: 0x0059 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x005E [0x01] GOTO 0x0066
  9: 0x0061 [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0066:
 10: 0x0066 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x006B [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x0070 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0071 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0076 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0086
     0x007E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0083 [0x01] GOTO 0x008B
     0x0086 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x008B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0090 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0095 [0x1B] RETURN
     0x0096 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x009B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00AB
     0x00A3 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00A8 [0x01] GOTO 0x00B0
     0x00AB [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00B0 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00B5 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00BA [0x1B] RETURN
     0x00BB [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00C0 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00D0
     0x00C8 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00CD [0x01] GOTO 0x00D5
     0x00D0 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00D5 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00DA [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00DF [0x1B] RETURN
```

### Event 10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E0    |
| Data Size    | 410 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 03 09 10 08 80 20 01 42  45 09 80 F8 FF FF 7F F8  ..... .BE.......
00F0: FF FF 7F 66 64 6F 30 0A  80 55 09 80 F8 FF FF 7F  ...fdo0..U......
0100: F8 FF FF 7F 66 64 6F 30  46 01 37 0B 80 0C 80 0D  ....fdo0F.7.....
0110: 80 0E 80 38 0F 80 45 10  80 F8 FF FF 7F F8 FF FF  ...8..E.........
0120: 7F 73 30 30 30 0A 80 45  09 80 F8 FF FF 7F F8 FF  .s000..E........
0130: FF 7F 66 64 69 32 0A 80  27 0A 63 41 0C 01 02 1C  ..fdi2..'.cA....
0140: 11 80 2B 63 41 0C 01 12  80 23 1E 63 41 0C 01 2A  ..+cA....#.cA..*
0150: 0A 63 41 0C 01 45 10 80  F8 FF FF 7F F8 FF FF 7F  .cA..E..........
0160: 73 30 30 31 0A 80 2B 63  41 0C 01 13 80 23 4A 63  s001..+cA....#Jc
0170: 41 0C 01 F0 FF FF 7F 6F  76 63 41 0C 01 7B 63 41  A......ovcA..{cA
0180: 0C 01 55 10 80 F8 FF FF  7F F8 FF FF 7F 73 30 30  ..U..........s00
0190: 31 45 09 80 F8 FF FF 7F  F8 FF FF 7F 66 64 6F 30  1E..........fdo0
01A0: 0A 80 55 09 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  ..U..........fdo
01B0: 30 22 01 2C 63 41 0C 01  63 41 0C 01 77 6F 6E 34  0".,cA..cA..won4
01C0: 5B 14 80 63 41 0C 01 63  41 0C 01 73 77 6F 31 45  [..cA..cA..swo1E
01D0: 10 80 F8 FF FF 7F F8 FF  FF 7F 73 30 30 32 0A 80  ..........s002..
01E0: 45 09 80 F8 FF FF 7F F8  FF FF 7F 66 64 69 30 0A  E..........fdi0.
01F0: 80 2B 63 41 0C 01 15 80  23 2C 63 41 0C 01 63 41  .+cA....#,cA..cA
0200: 0C 01 77 6F 66 34 5B 14  80 63 41 0C 01 63 41 0C  ..wof4[..cA..cA.
0210: 01 73 77 6F 32 2B 63 41  0C 01 16 80 23 53 63 41  .swo2+cA....#ScA
0220: 0C 01 63 41 0C 01 73 77  6F 32 27 0A 63 41 0C 01  ..cA..swo2'.cA..
0230: 03 1C 17 80 45 09 80 F8  FF FF 7F F8 FF FF 7F 66  ....E..........f
0240: 64 6F 32 0A 80 55 09 80  F8 FF FF 7F F8 FF FF 7F  do2..U..........
0250: 66 64 6F 32 45 18 80 F8  FF FF 7F F8 FF FF 7F 71  fdo2E..........q
0260: 73 74 63 0A 80 46 00 45  09 80 F8 FF FF 7F F8 FF  stc..F.E........
0270: FF 7F 66 64 69 32 0A 80  21 00                    ..fdi2..!.      
```

#### Opcodes

```
  0: 0x00E0 [0x03] Work_Zone[9] = 16637*
  1: 0x00E5 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x00E7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x00E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x00F9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
  5: 0x0108 [0x46] CAMERA_CONTROL: Disable user control
  6: 0x010A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=208.096*, z=-101.147*, y=-59.470*, direction=50.7°*
  7: 0x0113 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0116 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[96*, 0*]
  9: 0x0127 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 10: 0x0138 [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17580387/0x010C4163), tag_num=0x02)
 11: 0x013F [0x1C] WAIT(180* ticks)
 12: 0x0142 [0x2B] Zeid (ID: 17580387/0x010C4163) [7363*]:
    → "I see you have become quite skilled with that blade."
 13: 0x0149 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x014A [0x1E] EventEntity looks at Zeid (ID: 17580387/0x010C4163) and starts talking
 15: 0x014F [0x2A] GET_REQ_LEVEL(level=10, entity_id=Zeid (ID: 17580387/0x010C4163))
 16: 0x0155 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [EventEntity, EventEntity], work=[96*, 0*]
 17: 0x0166 [0x2B] Zeid (ID: 17580387/0x010C4163) [7364*]:
    → "It is no longer worthy of your ability. Take this, and unleash its true power."
 18: 0x016D [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x016E [0x4A] Zeid (ID: 17580387/0x010C4163) looks at LocalPlayer
 20: 0x0177 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 21: 0x0178 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Zeid (ID: 17580387/0x010C4163) Render.Flags0 and Render.Flags3 conditions are met
 22: 0x017D [0x7B] Zeid (ID: 17580387/0x010C4163) stops talking
 23: 0x0182 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s001" with entities [EventEntity, EventEntity], work=96*
 24: 0x0191 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 25: 0x01A2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
 26: 0x01B1 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 27: 0x01B3 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "won4" with entities [Zeid (ID: 17580387/0x010C4163), Zeid (ID: 17580387/0x010C4163)]
 28: 0x01C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "swo1" with entities [Zeid (ID: 17580387/0x010C4163), Zeid (ID: 17580387/0x010C4163)], work=243*
 29: 0x01CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s002" with entities [EventEntity, EventEntity], work=[96*, 0*]
 30: 0x01E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 31: 0x01F1 [0x2B] Zeid (ID: 17580387/0x010C4163) [7365*]:
    → "Behold, $7, bringer of death. Grasp now the blade that hears not the cry of justice."
 32: 0x01F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x01F9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "wof4" with entities [Zeid (ID: 17580387/0x010C4163), Zeid (ID: 17580387/0x010C4163)]
 34: 0x0206 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "swo2" with entities [Zeid (ID: 17580387/0x010C4163), Zeid (ID: 17580387/0x010C4163)], work=243*
 35: 0x0215 [0x2B] Zeid (ID: 17580387/0x010C4163) [7366*]:
    → "The battle calls upon Death...but now it calls upon you. The title that this sword bestows...can you withstand its terrible weight?"
 36: 0x021C [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x021D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "swo2" with entities [Zeid (ID: 17580387/0x010C4163), Zeid (ID: 17580387/0x010C4163)]
 38: 0x022A [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17580387/0x010C4163), tag_num=0x03)
 39: 0x0231 [0x1C] WAIT(60* ticks)
 40: 0x0234 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 41: 0x0245 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [EventEntity, EventEntity], work=200*
 42: 0x0254 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 43: 0x0265 [0x46] CAMERA_CONTROL: Restore default settings
 44: 0x0267 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 45: 0x0278 [0x21] END_EVENT
 46: 0x0279 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x027A    |
| Data Size    | 222 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                                02 07 7F 01 80 80            ......
0280: 94 02 66 19 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
0290: 30 01 4A 03 02 07 7F 02  80 80 AE 02 66 1A 80 F8  0.J.........f...
02A0: FF FF 7F F8 FF FF 7F 74  6C 6B 30 01 4A 03 02 07  .......tlk0.J...
02B0: 7F 1B 80 80 C8 02 66 1C  80 F8 FF FF 7F F8 FF FF  ......f.........
02C0: 7F 74 6C 6B 30 01 4A 03  02 07 7F 1D 80 80 E2 02  .tlk0.J.........
02D0: 66 1E 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 01  f..........tlk0.
02E0: 4A 03 02 07 7F 00 80 80  FC 02 66 1F 80 F8 FF FF  J.........f.....
02F0: 7F F8 FF FF 7F 74 6C 6B  30 01 4A 03 02 07 7F 20  .....tlk0.J.... 
0300: 80 80 16 03 66 1F 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
0310: 6C 6B 30 01 4A 03 02 07  7F 21 80 80 30 03 66 22  lk0.J....!..0.f"
0320: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 01 4A 03  .........tlk0.J.
0330: 02 07 7F 23 80 80 4A 03  66 24 80 F8 FF FF 7F F8  ...#..J.f$......
0340: FF FF 7F 74 6C 6B 30 01  4A 03 53 F8 FF FF 7F F8  ...tlk0.J.S.....
0350: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x027A [0x02] IF !(Entity->Race == 1*) GOTO 0x0294
  1: 0x0282 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=149*
  2: 0x0291 [0x01] GOTO 0x034A
  3: 0x0294 [0x02] IF !(Entity->Race == 2*) GOTO 0x02AE
  4: 0x029C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=159*
  5: 0x02AB [0x01] GOTO 0x034A
  6: 0x02AE [0x02] IF !(Entity->Race == 3*) GOTO 0x02C8
  7: 0x02B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=169*
  8: 0x02C5 [0x01] GOTO 0x034A
  9: 0x02C8 [0x02] IF !(Entity->Race == 4*) GOTO 0x02E2
 10: 0x02D0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=179*
 11: 0x02DF [0x01] GOTO 0x034A
 12: 0x02E2 [0x02] IF !(Entity->Race == 5*) GOTO 0x02FC
 13: 0x02EA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=189*
 14: 0x02F9 [0x01] GOTO 0x034A
 15: 0x02FC [0x02] IF !(Entity->Race == 6*) GOTO 0x0316
 16: 0x0304 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=189*
 17: 0x0313 [0x01] GOTO 0x034A
 18: 0x0316 [0x02] IF !(Entity->Race == 7*) GOTO 0x0330
 19: 0x031E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=199*
 20: 0x032D [0x01] GOTO 0x034A
 21: 0x0330 [0x02] IF !(Entity->Race == 8*) GOTO 0x034A
 22: 0x0338 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=209*
 23: 0x0347 [0x01] GOTO 0x034A

SUBROUTINE_034A:
 24: 0x034A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 25: 0x0357 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0358    |
| Data Size    | 222 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0350:                          02 07 7F 01 80 80 72 03          ......r.
0360: 66 19 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 01  f..........tlk1.
0370: 28 04 02 07 7F 02 80 80  8C 03 66 1A 80 F8 FF FF  (.........f.....
0380: 7F F8 FF FF 7F 74 6C 6B  31 01 28 04 02 07 7F 1B  .....tlk1.(.....
0390: 80 80 A6 03 66 1C 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
03A0: 6C 6B 31 01 28 04 02 07  7F 1D 80 80 C0 03 66 1E  lk1.(.........f.
03B0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 01 28 04  .........tlk1.(.
03C0: 02 07 7F 00 80 80 DA 03  66 1F 80 F8 FF FF 7F F8  ........f.......
03D0: FF FF 7F 74 6C 6B 31 01  28 04 02 07 7F 20 80 80  ...tlk1.(.... ..
03E0: F4 03 66 1F 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
03F0: 31 01 28 04 02 07 7F 21  80 80 0E 04 66 22 80 F8  1.(....!....f"..
0400: FF FF 7F F8 FF FF 7F 74  6C 6B 31 01 28 04 02 07  .......tlk1.(...
0410: 7F 23 80 80 28 04 66 24  80 F8 FF FF 7F F8 FF FF  .#..(.f$........
0420: 7F 74 6C 6B 31 01 28 04  53 F8 FF FF 7F F8 FF FF  .tlk1.(.S.......
0430: 7F 74 6C 6B 31 00                                 .tlk1.          
```

#### Opcodes

```
  0: 0x0358 [0x02] IF !(Entity->Race == 1*) GOTO 0x0372
  1: 0x0360 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=149*
  2: 0x036F [0x01] GOTO 0x0428
  3: 0x0372 [0x02] IF !(Entity->Race == 2*) GOTO 0x038C
  4: 0x037A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=159*
  5: 0x0389 [0x01] GOTO 0x0428
  6: 0x038C [0x02] IF !(Entity->Race == 3*) GOTO 0x03A6
  7: 0x0394 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=169*
  8: 0x03A3 [0x01] GOTO 0x0428
  9: 0x03A6 [0x02] IF !(Entity->Race == 4*) GOTO 0x03C0
 10: 0x03AE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=179*
 11: 0x03BD [0x01] GOTO 0x0428
 12: 0x03C0 [0x02] IF !(Entity->Race == 5*) GOTO 0x03DA
 13: 0x03C8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=189*
 14: 0x03D7 [0x01] GOTO 0x0428
 15: 0x03DA [0x02] IF !(Entity->Race == 6*) GOTO 0x03F4
 16: 0x03E2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=189*
 17: 0x03F1 [0x01] GOTO 0x0428
 18: 0x03F4 [0x02] IF !(Entity->Race == 7*) GOTO 0x040E
 19: 0x03FC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=199*
 20: 0x040B [0x01] GOTO 0x0428
 21: 0x040E [0x02] IF !(Entity->Race == 8*) GOTO 0x0428
 22: 0x0416 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=209*
 23: 0x0425 [0x01] GOTO 0x0428

SUBROUTINE_0428:
 24: 0x0428 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 25: 0x0435 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0436   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0430:                   32 25  80 1F 00 26 80 27 80 28        2%...&.'.(
0440: 80 1F 01 1F 00 29 80 2A  80 2B 80 1F 01 1F 00 2C  .....).*.+.....,
0450: 80 2D 80 2E 80 1F 01 6F  00                       .-.....o.       
```

#### Opcodes

```
  0: 0x0436 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0439 [0x1F] MOVE_ENTITY: EventEntity moves to X=-120.969*, Z=334.355*, Y=1.500*
  2: 0x0441 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0443 [0x1F] MOVE_ENTITY: EventEntity moves to X=-121.164*, Z=331.389*, Y=1.416*
  4: 0x044B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x044D [0x1F] MOVE_ENTITY: EventEntity moves to X=-127.580*, Z=317.822*, Y=1.249*
  6: 0x0455 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0457 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0458 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0459   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0450:                             32 25 80 1F 00 2F 80           2%.../.
0460: 30 80 31 80 1F 01 6F 1E  91 41 0C 01 00           0.1...o..A...   
```

#### Opcodes

```
  0: 0x0459 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x045C [0x1F] MOVE_ENTITY: EventEntity moves to X=-121.930*, Z=240.585*, Y=0.999*
  2: 0x0464 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0466 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0467 [0x1E] EventEntity looks at Dazbog (ID: 17580433/0x010C4191) and starts talking
  5: 0x046C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x046D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0460:                                         32 32 80               22.
0470: 1F 00 33 80 34 80 35 80  1F 01 6F 00              ..3.4.5...o.    
```

#### Opcodes

```
  0: 0x046D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0470 [0x1F] MOVE_ENTITY: EventEntity moves to X=-102.344*, Z=219.403*, Y=0.417*
  2: 0x0478 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x047A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x047B [0x00] END_REQSTACK()
```
