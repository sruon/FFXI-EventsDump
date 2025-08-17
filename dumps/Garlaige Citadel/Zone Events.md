# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Garlaige Citadel (ID: 200) |
| Block Size       | 1132 bytes                 |
| Total Events     | 13                         |
| References Count | 49                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |    185 |             37 |
| [6](#event-6)            | 0x00E0       |     10 |              2 |
| [7](#event-7)            | 0x00EA       |     14 |              4 |
| [8](#event-8)            | 0x00F8       |     10 |              2 |
| [9](#event-9)            | 0x0102       |     14 |              4 |
| [12](#event-12)          | 0x0110       |     13 |              3 |
| [13](#event-13)          | 0x011D       |     13 |              3 |
| [14](#event-14)          | 0x012A       |    406 |             54 |
| [60](#event-60)          | 0x02C0       |    148 |             20 |
| [65535.3](#event-655353) | 0x0354       |     13 |              3 |

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
|       8 | 0x222B8     |      139960 |
|       9 | 0x1F29F     |      127647 |
|      10 | 0xFFFFE890  |  4294961296 |
|      11 | 0x0C00      |        3072 |
|      12 | 0x000D      |          13 |
|      13 | 0x222B3     |      139955 |
|      14 | 0x20343     |      131907 |
|      15 | 0x222BA     |      139962 |
|      16 | 0x1F861     |      129121 |
|      17 | 0xFFFFE891  |  4294961297 |
|      18 | 0x03EB      |        1003 |
|      19 | 0x222B9     |      139961 |
|      20 | 0x1E9EF     |      125423 |
|      21 | 0x0429      |        1065 |
|      22 | 0x00C8      |         200 |
|      23 | 0x0000      |           0 |
|      24 | 0x007B      |         123 |
|      25 | 0x0013      |          19 |
|      26 | 0xFFFD7A52  |  4294802002 |
|      27 | 0x36CC3     |      224451 |
|      28 | 0x0FF8      |        4088 |
|      29 | 0x00CF      |         207 |
|      30 | 0x0020      |          32 |
|      31 | 0x0078      |         120 |
|      32 | 0x0040      |          64 |
|      33 | 0x001E      |          30 |
|      34 | 0x1CBD      |        7357 |
|      35 | 0x1CBE      |        7358 |
|      36 | 0x005A      |          90 |
|      37 | 0x1CBF      |        7359 |
|      38 | 0x00F0      |         240 |
|      39 | 0xFFFA3662  |  4294588002 |
|      40 | 0x5E15A     |      385370 |
|      41 | 0xFFFFD7F7  |  4294957047 |
|      42 | 0x0422      |        1058 |
|      43 | 0x00B4      |         180 |
|      44 | 0x1D29      |        7465 |
|      45 | 0xFFFD4152  |  4294787410 |
|      46 | 0xF53B      |       62779 |
|      47 | 0xFFFFF34E  |  4294964046 |
|      48 | 0x0400      |        1024 |

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

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 37 08 80 09 80 0A 80 0B  80 00                    7.........      
```

#### Opcodes

```
  0: 0x00E0 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=139.960*, z=127.647*, y=-6.000*, direction=270.0°*
  1: 0x00E9 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EA   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                32 0C 80 1F 00 0D            2.....
00F0: 80 0E 80 0A 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x00EA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00ED [0x1F] MOVE_ENTITY: EventEntity moves to X=139.955*, Z=131.907*, Y=-6.000*
  2: 0x00F5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F7 [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F8   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          37 0F 80 10 80 11 80 12          7.......
0100: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00F8 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=139.962*, z=129.121*, y=-5.999*, direction=88.2°*
  1: 0x0101 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       32 0C 80 1F 00 13  80 14 80 11 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0102 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0105 [0x1F] MOVE_ENTITY: EventEntity moves to X=139.961*, Z=125.423*, Y=-5.999*
  2: 0x010D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x010F [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0110   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 47 00 0D 80 0E 80 0A 80  0B 80 47 01 00           G.........G..   
```

#### Opcodes

```
  0: 0x0110 [0x47] UPDATE_PLAYER_POS(139.955*, 131.907*, -6.000*, yaw=270.0°*)
  1: 0x011A [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x011C [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         47 00 13               G..
0120: 80 14 80 11 80 15 80 47  01 00                    .......G..      
```

#### Opcodes

```
  0: 0x011D [0x47] UPDATE_PLAYER_POS(139.961*, 125.423*, -5.999*, yaw=93.6°*)
  1: 0x0127 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0129 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x012A    |
| Data Size    | 406 bytes |
| Instructions | 54        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                20 01 46 01 42 45             .F.BE
0130: 16 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 17 80  ..........fdo1..
0140: 55 16 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 5C  U..........fdo1\
0150: 00 18 80 5C 01 18 80 38  19 80 37 1A 80 1B 80 17  ...\...8..7.....
0160: 80 1C 80 4E 00 91 81 0C  01 2F 00 91 81 0C 01 92  ...N...../......
0170: 01 91 81 0C 01 6C 91 81  0C 01 17 80 17 80 80 91  .....l..........
0180: 81 0C 01 4A 91 81 0C 01  F0 FF FF 7F 4A F0 FF FF  ...J........J...
0190: 7F 91 81 0C 01 45 1D 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
01A0: 76 30 30 33 17 80 55 1D  80 F0 FF FF 7F F0 FF FF  v003..U.........
01B0: 7F 76 30 30 33 45 16 80  F0 FF FF 7F F0 FF FF 7F  .v003E..........
01C0: 66 64 69 31 17 80 55 16  80 F0 FF FF 7F F0 FF FF  fdi1..U.........
01D0: 7F 66 64 69 31 6C 91 81  0C 01 1E 80 1F 80 92 00  .fdi1l..........
01E0: 91 81 0C 01 6C 91 81 0C  01 20 80 1F 80 1C 21 80  ....l.... ....!.
01F0: 29 03 91 81 0C 01 02 79  00 F0 FF FF 7F 91 81 0C  )......y........
0200: 01 1C 21 80 27 04 91 81  0C 01 05 2B 91 81 0C 01  ..!.'......+....
0210: 22 80 23 29 04 91 81 0C  01 07 2B 91 81 0C 01 23  ".#)......+....#
0220: 80 23 29 05 91 81 0C 01  08 27 03 91 81 0C 01 03  .#)......'......
0230: 1C 24 80 4A F0 FF FF 7F  91 81 0C 01 1C 21 80 45  .$.J.........!.E
0240: 1D 80 F0 FF FF 7F F0 FF  FF 7F 76 30 30 34 17 80  ..........v004..
0250: 55 1D 80 F0 FF FF 7F F0  FF FF 7F 76 30 30 34 2A  U..........v004*
0260: 03 91 81 0C 01 2B 91 81  0C 01 25 80 23 27 04 91  .....+....%.#'..
0270: 81 0C 01 04 6C 91 81 0C  01 17 80 26 80 4E 01 91  ....l......&.N..
0280: 81 0C 01 45 16 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0290: 6F 32 17 80 55 16 80 F0  FF FF 7F F0 FF FF 7F 66  o2..U..........f
02A0: 64 6F 32 5C 00 17 80 5C  01 17 80 46 00 45 16 80  do2\...\...F.E..
02B0: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 17 80 21 00  ........fdi2..!.
```

#### Opcodes

```
  0: 0x012A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x012C [0x46] CAMERA_CONTROL: Disable user control
  2: 0x012E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x012F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0140 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x014F [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 123*
  6: 0x0153 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 123*
  7: 0x0157 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x015A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-165.294*, z=224.451*, y=0.000*, direction=359.3°*
  9: 0x0163 [0x4E] SET_ENTITY_HIDE_FLAG: Show Rainemard (ID: 17596817/0x010C8191)
 10: 0x0169 [0x2F] Rainemard (ID: 17596817/0x010C8191)->Render.Flags0 &= ~0x80000 // Bit 19
 11: 0x016F [0x92] Rainemard (ID: 17596817/0x010C8191)->Render.Flags3 ^= 0x01
 12: 0x0175 [0x6C] FADE_ENTITY_COLOR(entity_id=Rainemard (ID: 17596817/0x010C8191), end_alpha=0*, fade_time=0*)
 13: 0x017E [0x80] LOAD_WAIT(entity=Rainemard (ID: 17596817/0x010C8191))
 14: 0x0183 [0x4A] Rainemard (ID: 17596817/0x010C8191) looks at LocalPlayer
 15: 0x018C [0x4A] LocalPlayer looks at Rainemard (ID: 17596817/0x010C8191)
 16: 0x0195 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "v003" with entities [LocalPlayer, LocalPlayer], work=[207*, 0*]
 17: 0x01A6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "v003" with entities [LocalPlayer, LocalPlayer], work=207*
 18: 0x01B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x01C6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 20: 0x01D5 [0x6C] FADE_ENTITY_COLOR(entity_id=Rainemard (ID: 17596817/0x010C8191), end_alpha=32*, fade_time=120*)
 21: 0x01DE [0x92] Rainemard (ID: 17596817/0x010C8191)->Render.Flags3 = Flags3  // No change (flag=0)
 22: 0x01E4 [0x6C] FADE_ENTITY_COLOR(entity_id=Rainemard (ID: 17596817/0x010C8191), end_alpha=64*, fade_time=120*)
 23: 0x01ED [0x1C] WAIT(30* ticks)
 24: 0x01F0 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Rainemard (ID: 17596817/0x010C8191), tag_num=0x02)
 25: 0x01F7 [0x79] LocalPlayer looks at Rainemard (ID: 17596817/0x010C8191) (Basic look)
 26: 0x0201 [0x1C] WAIT(30* ticks)
 27: 0x0204 [0x27] REQ_SET(priority=0x04, entity_id=Rainemard (ID: 17596817/0x010C8191), tag_num=0x05)
 28: 0x020B [0x2B] Rainemard (ID: 17596817/0x010C8191) [7357*]:
    → "Who are you? I am sorry. Someone killed me and hid my remains here..."
 29: 0x0212 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0213 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Rainemard (ID: 17596817/0x010C8191), tag_num=0x07)
 31: 0x021A [0x2B] Rainemard (ID: 17596817/0x010C8191) [7358*]:
    → "For so long, I have begged for someone to come release my trapped soul. But none heard my pleas..."
 32: 0x0221 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0222 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Rainemard (ID: 17596817/0x010C8191), tag_num=0x08)
 34: 0x0229 [0x27] REQ_SET(priority=0x03, entity_id=Rainemard (ID: 17596817/0x010C8191), tag_num=0x03)
 35: 0x0230 [0x1C] WAIT(90* ticks)
 36: 0x0233 [0x4A] LocalPlayer looks at Rainemard (ID: 17596817/0x010C8191)
 37: 0x023C [0x1C] WAIT(30* ticks)
 38: 0x023F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "v004" with entities [LocalPlayer, LocalPlayer], work=[207*, 0*]
 39: 0x0250 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "v004" with entities [LocalPlayer, LocalPlayer], work=207*
 40: 0x025F [0x2A] GET_REQ_LEVEL(level=3, entity_id=Rainemard (ID: 17596817/0x010C8191))
 41: 0x0265 [0x2B] Rainemard (ID: 17596817/0x010C8191) [7359*]:
    → "Now I am free! You have my thanks, but I have no time. I must go now."
 42: 0x026C [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x026D [0x27] REQ_SET(priority=0x04, entity_id=Rainemard (ID: 17596817/0x010C8191), tag_num=0x04)
 44: 0x0274 [0x6C] FADE_ENTITY_COLOR(entity_id=Rainemard (ID: 17596817/0x010C8191), end_alpha=0*, fade_time=240*)
 45: 0x027D [0x4E] SET_ENTITY_HIDE_FLAG: Hide Rainemard (ID: 17596817/0x010C8191)
 46: 0x0283 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x0294 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 48: 0x02A3 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 49: 0x02A7 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 50: 0x02AB [0x46] CAMERA_CONTROL: Restore default settings
 51: 0x02AD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 52: 0x02BE [0x21] END_EVENT
 53: 0x02BF [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02C0    |
| Data Size    | 148 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0: 42 20 01 46 01 45 02 80  F0 FF FF 7F F0 FF FF 7F  B .F.E..........
02D0: 73 30 34 31 17 80 4E 00  A3 81 0C 01 22 00 37 27  s041..N.....".7'
02E0: 80 28 80 29 80 2A 80 38  19 80 45 16 80 F0 FF FF  .(.).*.8..E.....
02F0: 7F F0 FF FF 7F 66 64 69  31 17 80 1C 2B 80 79 00  .....fdi1...+.y.
0300: A3 81 0C 01 F0 FF FF 7F  2B A3 81 0C 01 2C 80 23  ........+....,.#
0310: 45 16 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 32 17  E..........fdo2.
0320: 80 55 16 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 32  .U..........fdo2
0330: 46 00 52 02 80 F0 FF FF  7F F0 FF FF 7F 73 30 34  F.R..........s04
0340: 31 45 16 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  1E..........fdi1
0350: 17 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x02C0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x02C1 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x02C3 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x02C5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s041" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
  4: 0x02D6 [0x4E] SET_ENTITY_HIDE_FLAG: Show Wanzo-Unzozo (ID: 17596835/0x010C81A3)
  5: 0x02DC [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  6: 0x02DE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-379.294*, z=385.370*, y=-10.249*, direction=93.0°*
  7: 0x02E7 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x02EA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x02FB [0x1C] WAIT(180* ticks)
 10: 0x02FE [0x79] Wanzo-Unzozo (ID: 17596835/0x010C81A3) looks at LocalPlayer (Basic look)
 11: 0x0308 [0x2B] Wanzo-Unzozo (ID: 17596835/0x010C81A3) [7465*]:
    → "There you are! I was starting to get the heeby-weeby-jeebies waiting for you in this creepy-crawly place. Let's skeda-da-daddle!"
 12: 0x030F [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0310 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0321 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 15: 0x0330 [0x46] CAMERA_CONTROL: Restore default settings
 16: 0x0332 [0x52] END_LOAD_SCHEDULER: End scheduler "s041" with entities [LocalPlayer, LocalPlayer], work=2*
 17: 0x0341 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0352 [0x21] END_EVENT
 19: 0x0353 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0354   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0350:             47 00 2D 80  2E 80 2F 80 30 80 47 01      G.-.../.0.G.
0360: 00                                                .               
```

#### Opcodes

```
  0: 0x0354 [0x47] UPDATE_PLAYER_POS(-179.886*, 62.779*, -3.250*, yaw=90.0°*)
  1: 0x035E [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0360 [0x00] END_REQSTACK()
```
