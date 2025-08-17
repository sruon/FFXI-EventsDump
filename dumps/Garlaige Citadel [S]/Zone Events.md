# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 872 bytes                      |
| Total Events     | 21                             |
| References Count | 34                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [41](#event-41)            | 0x0002       |    102 |             15 |
| [65535.1](#event-655351)   | 0x0068       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0072       |     14 |              4 |
| [65535.3](#event-655353)   | 0x0080       |     10 |              2 |
| [65535.4](#event-655354)   | 0x008A       |     14 |              4 |
| [65535.5](#event-655355)   | 0x0098       |     13 |              3 |
| [65535.6](#event-655356)   | 0x00A5       |     13 |              3 |
| [65535.7](#event-655357)   | 0x00B2       |     24 |              4 |
| [65535.8](#event-655358)   | 0x00CA       |     24 |              4 |
| [65535.9](#event-655359)   | 0x00E2       |     37 |              5 |
| [65535.10](#event-6553510) | 0x0107       |    185 |             37 |
| [65535.11](#event-6553511) | 0x01C0       |     19 |              4 |
| [65535.12](#event-6553512) | 0x01D3       |     46 |              9 |
| [65535.13](#event-6553513) | 0x0201       |     19 |              4 |
| [65535.14](#event-6553514) | 0x0214       |     19 |              4 |
| [65535.15](#event-6553515) | 0x0227       |     35 |              9 |
| [65535.16](#event-6553516) | 0x024A       |     35 |              9 |
| [65535.17](#event-6553517) | 0x026D       |      7 |              3 |
| [65535.18](#event-6553518) | 0x0274       |      7 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F1D      |        7965 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x005A      |          90 |
|       5 | 0x003C      |          60 |
|       6 | 0x00C9      |         201 |
|       7 | 0x35B3E     |      219966 |
|       8 | 0xFFFE44A4  |  4294853796 |
|       9 | 0xFFFFE890  |  4294961296 |
|      10 | 0x0C00      |        3072 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFFE5444  |  4294857796 |
|      13 | 0x0400      |        1024 |
|      14 | 0x0005      |           5 |
|      15 | 0x0002      |           2 |
|      16 | 0x000A      |          10 |
|      17 | 0x0009      |           9 |
|      18 | 0x0046      |          70 |
|      19 | 0x008C      |         140 |
|      20 | 0x00D2      |         210 |
|      21 | 0x0028      |          40 |
|      22 | 0xFFFE5329  |  4294857513 |
|      23 | 0x2C0A9     |      180393 |
|      24 | 0xFFFFFFB2  |  4294967218 |
|      25 | 0x001E      |          30 |
|      26 | 0x000F      |          15 |
|      27 | 0x0050      |          80 |
|      28 | 0x03BF      |         959 |
|      29 | 0x0029      |          41 |
|      30 | 0xFFFE5129  |  4294857001 |
|      31 | 0x2BFD7     |      180183 |
|      32 | 0xFFFE5147  |  4294857031 |
|      33 | 0x2F3DC     |      193500 |

## String References

- **7965**: The order has been given by your party leader to enter [Everbloom Hollow/the Ruhotz Silvermines/Ghoyu's Reverie].

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

### Event 41

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 102 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       42 48 00 80 45 01  80 F0 FF FF 7F F0 FF FF    BH..E.........
0010: 7F 66 64 6F 31 02 80 02  03 10 02 80 00 33 00 62  .fdo1........3.b
0020: 03 80 F0 FF FF 7F F0 FF  FF 7F 6D 61 69 6E 02 80  ..........main..
0030: 1C 04 80 1C 05 80 83 1E  17 AA 1E 17 1E 17 1E 17  ................
0040: 1E 17 1E 17 1F 17 1E 17  1E 17 03 04 00 02 80 77  ...............w
0050: 1F 17 04 00 78 45 06 80  F0 FF FF 7F F0 FF FF 7F  ....xE..........
0060: 77 68 69 31 02 80 21 00                           whi1..!.        
```

#### Opcodes

```
  0: 0x0002 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0003 [0x48] [System] [7965*]:
    → "The order has been given by your party leader to enter [Everbloom Hollow/the Ruhotz Silvermines/Ghoyu's Reverie]."
  2: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0017 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0033
  4: 0x001F [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  5: 0x0030 [0x1C] WAIT(90* ticks)
  6: 0x0033 [0x1C] WAIT(60* ticks)
  7: 0x0036 [0x83] Work_Zone_1700[30] = GetGameTime()
  8: 0x0039 [0xAA] VANA_DIEL_TIMESTAMP_CONVERTER(timestamp=Work_Zone_1700[30], year=Work_Zone_1700[30], month=Work_Zone_1700[30], day=Work_Zone_1700[30], weekday=Work_Zone_1700[30], hour=Work_Zone_1700[31], minute=Work_Zone_1700[30], moon=Work_Zone_1700[30])
  9: 0x004A [0x03] ExtData[1]->WorkLocal[4] = 0*
 10: 0x004F [0x77] SET_EVENT_TIME_WEATHER(hour=Work_Zone_1700[31], weather=ExtData[1]->WorkLocal[4])
 11: 0x0054 [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()
 12: 0x0055 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 13: 0x0066 [0x21] END_EVENT
 14: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          37 07 80 08 80 09 80 0A          7.......
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0068 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=219.966*, z=-113.500*, y=-6.000*, direction=270.0°*
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       32 0B 80 1F 00 07  80 0C 80 09 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0072 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0075 [0x1F] MOVE_ENTITY: EventEntity moves to X=219.966*, Z=-109.500*, Y=-6.000*
  2: 0x007D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 37 07 80 0C 80 09 80 0D  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0080 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=219.966*, z=-109.500*, y=-6.000*, direction=90.0°*
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                32 0B 80 1F 00 07            2.....
0090: 80 08 80 09 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x008A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008D [0x1F] MOVE_ENTITY: EventEntity moves to X=219.966*, Z=-113.500*, Y=-6.000*
  2: 0x0095 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          47 00 07 80 0C 80 09 80          G.......
00A0: 0A 80 47 01 00                                    ..G..           
```

#### Opcodes

```
  0: 0x0098 [0x47] UPDATE_PLAYER_POS(219.966*, -109.500*, -6.000*, yaw=270.0°*)
  1: 0x00A2 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                47 00 07  80 08 80 09 80 0D 80 47       G.........G
00B0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00A5 [0x47] UPDATE_PLAYER_POS(219.966*, -113.500*, -6.000*, yaw=90.0°*)
  1: 0x00AF [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       03 05 00 07 7F 1A  2C 01 66 06 00 F8 FF FF    ......,.f.....
00C0: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x00B2 [0x03] ExtData[1]->WorkLocal[5] = Entity->Race
  1: 0x00B7 [0x1A] CALL_SUBROUTINE(address=0x012C)
  2: 0x00BA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[6]
  3: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                03 05 00 07 7F 1A            ......
00D0: 2C 01 66 06 00 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ,.f..........tlk
00E0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x00CA [0x03] ExtData[1]->WorkLocal[5] = Entity->Race
  1: 0x00CF [0x1A] CALL_SUBROUTINE(address=0x012C)
  2: 0x00D2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[6]
  3: 0x00E1 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E2   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:       03 05 00 07 7F 1A  2C 01 66 06 00 F8 FF FF    ......,.f.....
00F0: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0100: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x00E2 [0x03] ExtData[1]->WorkLocal[5] = Entity->Race
  1: 0x00E7 [0x1A] CALL_SUBROUTINE(address=0x012C)
  2: 0x00EA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[6]
  3: 0x00F9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0106 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0107    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      03  05 00 07 7F 1A 2C 01 66         ......,.f
0110: 06 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0120: FF FF 7F F8 FF FF 7F 73  68 61 31 00 03 06 00 05  .......sha1.....
0130: 00 02 06 00 0E 80 05 41  01 08 06 00 03 80 01 46  .......A.......F
0140: 01 08 06 00 0F 80 14 06  00 10 80 07 06 00 11 80  ................
0150: 1B 03 06 00 05 00 02 06  00 0E 80 05 66 01 08 06  ............f...
0160: 00 03 80 01 6B 01 08 06  00 0F 80 14 06 00 10 80  ....k...........
0170: 07 06 00 12 80 1B 03 06  00 05 00 02 06 00 0E 80  ................
0180: 05 8B 01 08 06 00 03 80  01 90 01 08 06 00 0F 80  ................
0190: 14 06 00 10 80 07 06 00  13 80 1B 03 06 00 05 00  ................
01A0: 02 06 00 0E 80 05 B0 01  08 06 00 03 80 01 B5 01  ................
01B0: 08 06 00 0F 80 14 06 00  10 80 07 06 00 14 80 1B  ................
```

#### Opcodes

```
  0: 0x0107 [0x03] ExtData[1]->WorkLocal[5] = Entity->Race
  1: 0x010C [0x1A] CALL_SUBROUTINE(address=0x012C)
  2: 0x010F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[6]
  3: 0x011E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x012B [0x00] END_REQSTACK()

SUBROUTINE_012C:
  5: 0x012C [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[5]
  6: 0x0131 [0x02] IF !(ExtData[1]->WorkLocal[6] > 5*) GOTO 0x0141
  7: 0x0139 [0x08] ExtData[1]->WorkLocal[6] -= 1*
  8: 0x013E [0x01] GOTO 0x0146
  9: 0x0141 [0x08] ExtData[1]->WorkLocal[6] -= 2*

SUBROUTINE_0146:
 10: 0x0146 [0x14] ExtData[1]->WorkLocal[6] *= 10*
 11: 0x014B [0x07] ExtData[1]->WorkLocal[6] += 9*
 12: 0x0150 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0151 [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[5]
     0x0156 [0x02] IF !(ExtData[1]->WorkLocal[6] > 5*) GOTO 0x0166
     0x015E [0x08] ExtData[1]->WorkLocal[6] -= 1*
     0x0163 [0x01] GOTO 0x016B
     0x0166 [0x08] ExtData[1]->WorkLocal[6] -= 2*
     0x016B [0x14] ExtData[1]->WorkLocal[6] *= 10*
     0x0170 [0x07] ExtData[1]->WorkLocal[6] += 70*
     0x0175 [0x1B] RETURN
     0x0176 [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[5]
     0x017B [0x02] IF !(ExtData[1]->WorkLocal[6] > 5*) GOTO 0x018B
     0x0183 [0x08] ExtData[1]->WorkLocal[6] -= 1*
     0x0188 [0x01] GOTO 0x0190
     0x018B [0x08] ExtData[1]->WorkLocal[6] -= 2*
     0x0190 [0x14] ExtData[1]->WorkLocal[6] *= 10*
     0x0195 [0x07] ExtData[1]->WorkLocal[6] += 140*
     0x019A [0x1B] RETURN
     0x019B [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[5]
     0x01A0 [0x02] IF !(ExtData[1]->WorkLocal[6] > 5*) GOTO 0x01B0
     0x01A8 [0x08] ExtData[1]->WorkLocal[6] -= 1*
     0x01AD [0x01] GOTO 0x01B5
     0x01B0 [0x08] ExtData[1]->WorkLocal[6] -= 2*
     0x01B5 [0x14] ExtData[1]->WorkLocal[6] *= 10*
     0x01BA [0x07] ExtData[1]->WorkLocal[6] += 210*
     0x01BF [0x1B] RETURN
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C0   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 59 04 F0 FF FF 7F 15 80  1F 00 16 80 17 80 18 80  Y...............
01D0: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x01C0 [0x59] UPDATE_ENTITY_DATA: Set LocalPlayer main speed = 40* * 0.1
  1: 0x01C8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-109.783*, Z=180.393*, Y=-0.078*
  2: 0x01D0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01D2 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D3   |
| Data Size    | 46 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:          53 3C 42 0A 01  3C 42 0A 01 79 65 73 30     S<B..<B..yes0
01E0: 1C 19 80 1C 1A 80 59 01  F0 FF FF 7F 1B 80 4B F0  ......Y.......K.
01F0: FF FF 7F 1C 80 7B F0 FF  FF 7F 6F 76 F0 FF FF 7F  .....{....ov....
0200: 00                                                .               
```

#### Opcodes

```
  0: 0x01D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "yes0" with entities [Rahal (ID: 17449532/0x010A423C), Rahal (ID: 17449532/0x010A423C)]
  1: 0x01E0 [0x1C] WAIT(30* ticks)
  2: 0x01E3 [0x1C] WAIT(15* ticks)
  3: 0x01E6 [0x59] UPDATE_ENTITY_DATA: Set LocalPlayer turn speed = 80*
  4: 0x01EE [0x4B] UPDATE_ENTITY_YAW(entity=LocalPlayer, yaw=5.3°*)
  5: 0x01F5 [0x7B] LocalPlayer stops talking
  6: 0x01FA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x01FB [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0200 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0201   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:    59 04 F0 FF FF 7F 1D  80 1F 00 1E 80 1F 80 18   Y..............
0210: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0201 [0x59] UPDATE_ENTITY_DATA: Set LocalPlayer main speed = 41* * 0.1
  1: 0x0209 [0x1F] MOVE_ENTITY: EventEntity moves to X=-110.295*, Z=180.183*, Y=-0.078*
  2: 0x0211 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0213 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0214   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:             59 04 F0 FF  FF 7F 1D 80 1F 00 20 80      Y......... .
0220: 21 80 02 80 1F 01 00                              !......         
```

#### Opcodes

```
  0: 0x0214 [0x59] UPDATE_ENTITY_DATA: Set LocalPlayer main speed = 41* * 0.1
  1: 0x021C [0x1F] MOVE_ENTITY: EventEntity moves to X=-110.265*, Z=193.500*, Y=0.000*
  2: 0x0224 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0226 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0227   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                      03  00 00 25 10 03 02 00 27         ...%....'
0230: 10 03 01 00 26 10 03 03  00 28 10 32 15 80 1F 00  ....&....(.2....
0240: 00 00 02 00 01 00 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0227 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x022C [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0231 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0236 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x023B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x023E [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0246 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0248 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0249 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024A   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                03 00 00 25 10 03            ...%..
0250: 02 00 27 10 03 01 00 26  10 03 03 00 28 10 32 0B  ..'....&....(.2.
0260: 80 1F 00 00 00 02 00 01  00 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x024A [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x024F [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0254 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0259 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x025E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x0261 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0269 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x026B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x026C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x026D  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                                         AB 03 AC               ...
0270: 01 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x026D [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x026F [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0273 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0274  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:             AC 01 02 80  AB 04 00                     .......     
```

#### Opcodes

```
  0: 0x0274 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0278 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x027A [0x00] END_REQSTACK()
```
