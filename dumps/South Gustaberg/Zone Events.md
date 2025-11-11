# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | South Gustaberg (ID: 107) |
| Block Size       | 1052 bytes                |
| Total Events     | 15                        |
| References Count | 34                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     10 |              2 |
| [907](#event-907)          | 0x000C       |    370 |             49 |
| [65535.2](#event-655352)   | 0x017E       |     16 |              3 |
| [65535.3](#event-655353)   | 0x018E       |     41 |              5 |
| [65535.4](#event-655354)   | 0x01B7       |      6 |              2 |
| [65535.5](#event-655355)   | 0x01BD       |      6 |              2 |
| [65535.6](#event-655356)   | 0x01C3       |     37 |              5 |
| [65535.7](#event-655357)   | 0x01E8       |    185 |             37 |
| [65535.8](#event-655358)   | 0x02A1       |     24 |              4 |
| [65535.9](#event-655359)   | 0x02B9       |     24 |              4 |
| [65535.10](#event-6553510) | 0x02D1       |     37 |              5 |
| [65535.11](#event-6553511) | 0x02F6       |     37 |              5 |
| [65535.12](#event-6553512) | 0x031B       |     42 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xBD19D     |      774557 |
|       1 | 0xFFF5C8E8  |  4294297832 |
|       2 | 0x01A4      |         420 |
|       3 | 0x043E      |        1086 |
|       4 | 0x00C8      |         200 |
|       5 | 0x0000      |           0 |
|       6 | 0x0013      |          19 |
|       7 | 0x0090      |         144 |
|       8 | 0x003C      |          60 |
|       9 | 0x8D9B9     |      580025 |
|      10 | 0xFFFB37BB  |  4294653883 |
|      11 | 0x0564      |        1380 |
|      12 | 0x0BAA      |        2986 |
|      13 | 0x0005      |           5 |
|      14 | 0x1E0E      |        7694 |
|      15 | 0x001E      |          30 |
|      16 | 0x1E0F      |        7695 |
|      17 | 0x1E10      |        7696 |
|      18 | 0x1E14      |        7700 |
|      19 | 0x1E11      |        7697 |
|      20 | 0x00C9      |         201 |
|      21 | 0x5307C     |      340092 |
|      22 | 0xFFF5B7DF  |  4294293471 |
|      23 | 0xFFFFFFF9  |  4294967289 |
|      24 | 0x0401      |        1025 |
|      25 | 0x0094      |         148 |
|      26 | 0x00F0      |         240 |
|      27 | 0x0001      |           1 |
|      28 | 0x0002      |           2 |
|      29 | 0x000A      |          10 |
|      30 | 0x0009      |           9 |
|      31 | 0x0046      |          70 |
|      32 | 0x008C      |         140 |
|      33 | 0x00D2      |         210 |

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=774.557*, z=-669.464*, y=0.420*, direction=95.4°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 907

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000C    |
| Data Size    | 370 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      42 46 01 03              BF..
0010: 00 00 05 10 45 04 80 F8  FF FF 7F F8 FF FF 7F 66  ....E..........f
0020: 64 6F 30 05 80 55 04 80  F8 FF FF 7F F8 FF FF 7F  do0..U..........
0030: 66 64 6F 30 4E 00 B9 B2  06 01 4E 00 BA B2 06 01  fdo0N.....N.....
0040: 38 06 80 79 00 F0 FF FF  7F B9 B2 06 01 03 05 10  8..y............
0050: 02 10 03 06 10 02 10 03  07 10 02 10 15 05 10 07  ................
0060: 80 15 06 10 08 80 3F 07  10 07 10 08 80 37 09 80  ......?......7..
0070: 0A 80 0B 80 0C 80 45 0D  80 F8 FF FF 7F F8 FF FF  ......E.........
0080: 7F 73 30 30 30 05 80 4A  B9 B2 06 01 F0 FF FF 7F  .s000..J........
0090: 45 04 80 F8 FF FF 7F F8  FF FF 7F 66 64 69 31 05  E..........fdi1.
00A0: 80 2B B9 B2 06 01 0E 80  23 66 0F 80 B9 B2 06 01  .+......#f......
00B0: B9 B2 06 01 74 6C 6B 30  2B B9 B2 06 01 10 80 23  ....tlk0+......#
00C0: 02 04 10 05 80 01 12 01  66 0F 80 B9 B2 06 01 B9  ........f.......
00D0: B2 06 01 74 6C 6B 31 03  05 10 04 10 03 06 10 04  ...tlk1.........
00E0: 10 03 07 10 04 10 15 05  10 07 80 15 06 10 08 80  ................
00F0: 3F 07 10 07 10 08 80 02  00 00 05 80 00 0A 01 2B  ?..............+
0100: B9 B2 06 01 11 80 23 01  12 01 2B B9 B2 06 01 12  ......#...+.....
0110: 80 23 66 0F 80 B9 B2 06  01 B9 B2 06 01 70 61 73  .#f..........pas
0120: 30 2B B9 B2 06 01 13 80  23 52 0D 80 F8 FF FF 7F  0+......#R......
0130: F8 FF FF 7F 73 30 30 30  45 04 80 F8 FF FF 7F F8  ....s000E.......
0140: FF FF 7F 66 64 6F 31 05  80 55 04 80 F8 FF FF 7F  ...fdo1..U......
0150: F8 FF FF 7F 66 64 6F 31  46 00 45 14 80 F0 FF FF  ....fdo1F.E.....
0160: 7F F0 FF FF 7F 71 73 74  63 05 80 45 04 80 F8 FF  .....qstc..E....
0170: FF 7F F8 FF FF 7F 66 64  69 32 05 80 21 00        ......fdi2..!.  
```

#### Opcodes

```
  0: 0x000C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000D [0x46] CAMERA_CONTROL: Disable user control
  2: 0x000F [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[5]
  3: 0x0014 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x0025 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
  5: 0x0034 [0x4E] SET_ENTITY_HIDE_FLAG: Show Azette (ID: 17216185/0x0106B2B9)
  6: 0x003A [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17216186/0x0106B2BA)
  7: 0x0040 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0043 [0x79] LocalPlayer looks at Azette (ID: 17216185/0x0106B2B9) (Basic look)
  9: 0x004D [0x03] Work_Zone[5] = Work_Zone[2]
 10: 0x0052 [0x03] Work_Zone[6] = Work_Zone[2]
 11: 0x0057 [0x03] Work_Zone[7] = Work_Zone[2]
 12: 0x005C [0x15] Work_Zone[5] /= 144*
 13: 0x0061 [0x15] Work_Zone[6] /= 60*
 14: 0x0066 [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 15: 0x006D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=580.025*, z=-313.413*, y=1.380*, direction=262.4°*
 16: 0x0076 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[5*, 0*]
 17: 0x0087 [0x4A] Azette (ID: 17216185/0x0106B2B9) looks at LocalPlayer
 18: 0x0090 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 19: 0x00A1 [0x2B] Azette (ID: 17216185/0x0106B2B9) [7694*]:
    → "You've helped our poor girl find her way home! I don't know how to thank you!"
 20: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00A9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Azette (ID: 17216185/0x0106B2B9), Azette (ID: 17216185/0x0106B2B9)], work=30*
 22: 0x00B8 [0x2B] Azette (ID: 17216185/0x0106B2B9) [7695*]:
    → "And to think you made it here in a mere $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 23: 0x00BF [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00C0 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0112
 25: 0x00C8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Azette (ID: 17216185/0x0106B2B9), Azette (ID: 17216185/0x0106B2B9)], work=30*
 26: 0x00D7 [0x03] Work_Zone[5] = Work_Zone[4]
 27: 0x00DC [0x03] Work_Zone[6] = Work_Zone[4]
 28: 0x00E1 [0x03] Work_Zone[7] = Work_Zone[4]
 29: 0x00E6 [0x15] Work_Zone[5] /= 144*
 30: 0x00EB [0x15] Work_Zone[6] /= 60*
 31: 0x00F0 [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 32: 0x00F7 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x010A
 33: 0x00FF [0x2B] Azette (ID: 17216185/0x0106B2B9) [7696*]:
    → "Oh, and by the way, the fastest adventurer to date has been %0. That talented rider traversed the same course as you in $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 34: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0107 [0x01] GOTO 0x0112
 36: 0x010A [0x2B] Azette (ID: 17216185/0x0106B2B9) [7700*]:
    → "Oh, and by the way, the fastest adventurer to date has been...you! Your remarkable record of $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time) still stands strong!"
 37: 0x0111 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0112:
 38: 0x0112 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [Azette (ID: 17216185/0x0106B2B9), Azette (ID: 17216185/0x0106B2B9)], work=30*
 39: 0x0121 [0x2B] Azette (ID: 17216185/0x0106B2B9) [7697*]:
    → "Anyway, please take this as a token of our appreciation. And stop by again sometime. We may have more work for you!"
 40: 0x0128 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0129 [0x52] END_LOAD_SCHEDULER: End scheduler "s000" with entities [EventEntity, EventEntity], work=5*
 42: 0x0138 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 43: 0x0149 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 44: 0x0158 [0x46] CAMERA_CONTROL: Restore default settings
 45: 0x015A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 46: 0x016B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 47: 0x017C [0x21] END_EVENT
 48: 0x017D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017E   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            92 01                ..
0180: F0 FF FF 7F 37 15 80 16  80 17 80 18 80 00        ....7.........  
```

#### Opcodes

```
  0: 0x017E [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  1: 0x0184 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=340.092*, z=-673.825*, y=-0.007*, direction=90.1°*
  2: 0x018D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018E   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                            BB 19                ..
0190: 80 F0 FF FF 7F C9 B2 06  01 6D 61 69 6E 05 80 1C  .........main...
01A0: 1A 80 45 04 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
01B0: 31 05 80 1C 08 80 00                              1......         
```

#### Opcodes

```
  0: 0x018E [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17216201/0x0106B2C9)], work=[148*, 0*]
  1: 0x019F [0x1C] WAIT(240* ticks)
  2: 0x01A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x01B3 [0x1C] WAIT(60* ticks)
  4: 0x01B6 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B7  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                      03  02 10 07 7F 00                  ......   
```

#### Opcodes

```
  0: 0x01B7 [0x03] Work_Zone[2] = Entity->Race
  1: 0x01BC [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01BD  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                         03 02 10               ...
01C0: 0B 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x01BD [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x01C2 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C3   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:          03 01 00 07 7F  1A 0D 02 66 02 00 F8 FF     ........f....
01D0: FF 7F F8 FF FF 7F 73 68  61 30 53 F8 FF FF 7F F8  ......sha0S.....
01E0: FF FF 7F 73 68 61 30 00                           ...sha0.        
```

#### Opcodes

```
  0: 0x01C3 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x01C8 [0x1A] CALL_SUBROUTINE(address=0x020D)
  2: 0x01CB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x01DA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x01E7 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01E8    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                          03 01 00 07 7F 1A 0D 02          ........
01F0: 66 02 00 F8 FF FF 7F F8  FF FF 7F 73 68 61 31 53  f..........sha1S
0200: F8 FF FF 7F F8 FF FF 7F  73 68 61 31 00 03 02 00  ........sha1....
0210: 01 00 02 02 00 0D 80 05  22 02 08 02 00 1B 80 01  ........".......
0220: 27 02 08 02 00 1C 80 14  02 00 1D 80 07 02 00 1E  '...............
0230: 80 1B 03 02 00 01 00 02  02 00 0D 80 05 47 02 08  .............G..
0240: 02 00 1B 80 01 4C 02 08  02 00 1C 80 14 02 00 1D  .....L..........
0250: 80 07 02 00 1F 80 1B 03  02 00 01 00 02 02 00 0D  ................
0260: 80 05 6C 02 08 02 00 1B  80 01 71 02 08 02 00 1C  ..l.......q.....
0270: 80 14 02 00 1D 80 07 02  00 20 80 1B 03 02 00 01  ......... ......
0280: 00 02 02 00 0D 80 05 91  02 08 02 00 1B 80 01 96  ................
0290: 02 08 02 00 1C 80 14 02  00 1D 80 07 02 00 21 80  ..............!.
02A0: 1B                                                .               
```

#### Opcodes

```
  0: 0x01E8 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x01ED [0x1A] CALL_SUBROUTINE(address=0x020D)
  2: 0x01F0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x01FF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x020C [0x00] END_REQSTACK()

SUBROUTINE_020D:
  5: 0x020D [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
  6: 0x0212 [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x0222
  7: 0x021A [0x08] ExtData[1]->WorkLocal[2] -= 1*
  8: 0x021F [0x01] GOTO 0x0227
  9: 0x0222 [0x08] ExtData[1]->WorkLocal[2] -= 2*

SUBROUTINE_0227:
 10: 0x0227 [0x14] ExtData[1]->WorkLocal[2] *= 10*
 11: 0x022C [0x07] ExtData[1]->WorkLocal[2] += 9*
 12: 0x0231 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0232 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
     0x0237 [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x0247
     0x023F [0x08] ExtData[1]->WorkLocal[2] -= 1*
     0x0244 [0x01] GOTO 0x024C
     0x0247 [0x08] ExtData[1]->WorkLocal[2] -= 2*
     0x024C [0x14] ExtData[1]->WorkLocal[2] *= 10*
     0x0251 [0x07] ExtData[1]->WorkLocal[2] += 70*
     0x0256 [0x1B] RETURN
     0x0257 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
     0x025C [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x026C
     0x0264 [0x08] ExtData[1]->WorkLocal[2] -= 1*
     0x0269 [0x01] GOTO 0x0271
     0x026C [0x08] ExtData[1]->WorkLocal[2] -= 2*
     0x0271 [0x14] ExtData[1]->WorkLocal[2] *= 10*
     0x0276 [0x07] ExtData[1]->WorkLocal[2] += 140*
     0x027B [0x1B] RETURN
     0x027C [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[1]
     0x0281 [0x02] IF !(ExtData[1]->WorkLocal[2] > 5*) GOTO 0x0291
     0x0289 [0x08] ExtData[1]->WorkLocal[2] -= 1*
     0x028E [0x01] GOTO 0x0296
     0x0291 [0x08] ExtData[1]->WorkLocal[2] -= 2*
     0x0296 [0x14] ExtData[1]->WorkLocal[2] *= 10*
     0x029B [0x07] ExtData[1]->WorkLocal[2] += 210*
     0x02A0 [0x1B] RETURN
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02A1   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:    03 01 00 07 7F 1A 0D  02 66 02 00 F8 FF FF 7F   ........f......
02B0: F8 FF FF 7F 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x02A1 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x02A6 [0x1A] CALL_SUBROUTINE(address=0x020D)
  2: 0x02A9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x02B8 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02B9   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                             03 01 00 07 7F 1A 0D           .......
02C0: 02 66 02 00 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31  .f..........tlk1
02D0: 00                                                .               
```

#### Opcodes

```
  0: 0x02B9 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x02BE [0x1A] CALL_SUBROUTINE(address=0x020D)
  2: 0x02C1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x02D0 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02D1   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0:    03 01 00 07 7F 1A 0D  02 66 02 00 F8 FF FF 7F   ........f......
02E0: F8 FF FF 7F 73 69 74 30  53 F8 FF FF 7F F8 FF FF  ....sit0S.......
02F0: 7F 73 69 74 30 00                                 .sit0.          
```

#### Opcodes

```
  0: 0x02D1 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x02D6 [0x1A] CALL_SUBROUTINE(address=0x020D)
  2: 0x02D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x02E8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit0" with entities [EventEntity, EventEntity]
  4: 0x02F5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02F6   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02F0:                   03 01  00 07 7F 1A 0D 02 66 02        ........f.
0300: 00 F8 FF FF 7F F8 FF FF  7F 73 69 74 31 53 F8 FF  .........sit1S..
0310: FF 7F F8 FF FF 7F 73 69  74 31 00                 ......sit1.     
```

#### Opcodes

```
  0: 0x02F6 [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x02FB [0x1A] CALL_SUBROUTINE(address=0x020D)
  2: 0x02FE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x030D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit1" with entities [EventEntity, EventEntity]
  4: 0x031A [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x031B   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                                   03 01 00 07 7F             .....
0320: 1A 0D 02 66 02 00 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...f..........tl
0330: 6B 30 1C 08 80 66 02 00  F8 FF FF 7F F8 FF FF 7F  k0...f..........
0340: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x031B [0x03] ExtData[1]->WorkLocal[1] = Entity->Race
  1: 0x0320 [0x1A] CALL_SUBROUTINE(address=0x020D)
  2: 0x0323 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  3: 0x0332 [0x1C] WAIT(60* ticks)
  4: 0x0335 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[2]
  5: 0x0344 [0x00] END_REQSTACK()
```
