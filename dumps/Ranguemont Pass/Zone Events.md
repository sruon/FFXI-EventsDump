# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ranguemont Pass (ID: 166) |
| Block Size       | 1352 bytes                |
| Total Events     | 13                        |
| References Count | 46                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     37 |              5 |
| [65535.2](#event-655352)   | 0x0027       |    185 |             37 |
| [8](#event-8)              | 0x00E0       |    761 |             95 |
| [65535.3](#event-655353)   | 0x03D9       |      6 |              2 |
| [65535.4](#event-655354)   | 0x03DF       |      6 |              2 |
| [65535.5](#event-655355)   | 0x03E5       |      6 |              2 |
| [65535.6](#event-655356)   | 0x03EB       |      6 |              2 |
| [65535.7](#event-655357)   | 0x03F1       |     10 |              2 |
| [65535.8](#event-655358)   | 0x03FB       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0405       |     27 |              5 |
| [65535.10](#event-6553510) | 0x0420       |     42 |              6 |

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
|       8 | 0x00C8      |         200 |
|       9 | 0x0000      |           0 |
|      10 | 0x009F      |         159 |
|      11 | 0x0013      |          19 |
|      12 | 0xFFFBAF9F  |  4294684575 |
|      13 | 0x333FE     |      209918 |
|      14 | 0xFFFF4FAF  |  4294922159 |
|      15 | 0x0899      |        2201 |
|      16 | 0x000D      |          13 |
|      17 | 0x00D0      |         208 |
|      18 | 0xFFFBA859  |  4294682713 |
|      19 | 0x3362A     |      210474 |
|      20 | 0xFFFF4F76  |  4294922102 |
|      21 | 0x000F      |          15 |
|      22 | 0x1CCA      |        7370 |
|      23 | 0x0096      |         150 |
|      24 | 0x1CCB      |        7371 |
|      25 | 0x001E      |          30 |
|      26 | 0xFFFBA9D1  |  4294683089 |
|      27 | 0x33E25     |      212517 |
|      28 | 0xFFFF4F00  |  4294921984 |
|      29 | 0x0003      |           3 |
|      30 | 0x0028      |          40 |
|      31 | 0x003C      |          60 |
|      32 | 0x00E4      |         228 |
|      33 | 0x1CC8      |        7368 |
|      34 | 0x1CCC      |        7372 |
|      35 | 0x1CCD      |        7373 |
|      36 | 0x1CCE      |        7374 |
|      37 | 0x00C9      |         201 |
|      38 | 0xFFFD361A  |  4294784538 |
|      39 | 0xFFFD732A  |  4294800170 |
|      40 | 0x1481      |        5249 |
|      41 | 0x0B82      |        2946 |
|      42 | 0xD751      |       55121 |
|      43 | 0xFFFDCA46  |  4294822470 |
|      44 | 0x335E      |       13150 |
|      45 | 0x04BD      |        1213 |

## String References

- **7368**: Mertaire throws his bracelet into the Waters of Oblivion.

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

### Event 8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E0    |
| Data Size    | 761 bytes |
| Instructions | 95        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 20 01 42 46 01 45 08 80  F0 FF FF 7F F0 FF FF 7F   .BF.E..........
00F0: 66 64 6F 31 09 80 55 08  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
0100: 7F 66 64 6F 31 5C 00 0A  80 5C 01 0A 80 38 0B 80  .fdo1\...\...8..
0110: 37 0C 80 0D 80 0E 80 0F  80 32 10 80 45 11 80 F0  7........2..E...
0120: FF FF 7F F0 FF FF 7F 74  30 30 37 09 80 55 11 80  .......t007..U..
0130: F0 FF FF 7F F0 FF FF 7F  74 30 30 37 45 08 80 F0  ........t007E...
0140: FF FF 7F F0 FF FF 7F 66  64 69 31 09 80 55 08 80  .......fdi1..U..
0150: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 1C 03 80 1F  ........fdi1....
0160: 00 12 80 13 80 14 80 1F  01 6F 1C 15 80 2B C4 60  .........o...+.`
0170: 0A 01 16 80 23 4E 00 C4  60 0A 01 4A F0 FF FF 7F  ....#N..`..J....
0180: C4 60 0A 01 27 03 C4 60  0A 01 02 1C 17 80 45 11  .`..'..`......E.
0190: 80 F0 FF FF 7F F0 FF FF  7F 74 30 30 62 09 80 2A  .........t00b..*
01A0: 03 C4 60 0A 01 55 11 80  F0 FF FF 7F F0 FF FF 7F  ..`..U..........
01B0: 74 30 30 62 2B C4 60 0A  01 18 80 23 1C 19 80 27  t00b+.`....#...'
01C0: 03 C4 60 0A 01 03 1F 00  1A 80 1B 80 1C 80 1F 01  ..`.............
01D0: 4A F0 FF FF 7F C4 60 0A  01 2A 03 C4 60 0A 01 4A  J.....`..*..`..J
01E0: F0 FF FF 7F C4 60 0A 01  4A C4 60 0A 01 C3 60 0A  .....`..J.`...`.
01F0: 01 6F 76 C4 60 0A 01 2C  C4 60 0A 01 C4 60 0A 01  .ov.`..,.`...`..
0200: 73 68 69 74 1C 19 80 4A  F0 FF FF 7F C3 60 0A 01  shit...J.....`..
0210: 45 11 80 C4 60 0A 01 C4  60 0A 01 74 30 31 31 09  E...`...`..t011.
0220: 80 55 11 80 C4 60 0A 01  C4 60 0A 01 74 30 31 31  .U...`...`..t011
0230: 1C 03 80 45 08 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  ...E..........ov
0240: 6C 31 09 80 1C 00 80 45  11 80 F0 FF FF 7F F0 FF  l1.....E........
0250: FF 7F 74 30 30 38 09 80  55 11 80 F0 FF FF 7F F0  ..t008..U.......
0260: FF FF 7F 74 30 30 38 28  03 C3 60 0A 01 02 27 03  ...t008(..`...'.
0270: C1 60 0A 01 06 1C 03 80  66 04 80 C4 60 0A 01 C4  .`......f...`...
0280: 60 0A 01 73 68 61 30 06  02 00 02 02 00 08 80 05  `..sha0.........
0290: AE 02 62 1D 80 C3 60 0A  01 C3 60 0A 01 6D 61 69  ..b...`...`..mai
02A0: 6E 09 80 1C 1E 80 07 02  00 1E 80 01 8A 02 2A 03  n.............*.
02B0: C3 60 0A 01 1C 1F 80 45  11 80 F0 FF FF 7F F0 FF  .`.....E........
02C0: FF 7F 74 30 31 30 09 80  55 11 80 F0 FF FF 7F F0  ..t010..U.......
02D0: FF FF 7F 74 30 31 30 03  02 10 20 80 48 21 80 23  ...t010... .H!.#
02E0: 4A F0 FF FF 7F C4 60 0A  01 66 04 80 C4 60 0A 01  J.....`..f...`..
02F0: C4 60 0A 01 73 68 61 31  53 C4 60 0A 01 C4 60 0A  .`..sha1S.`...`.
0300: 01 73 68 61 31 1C 1F 80  2B C4 60 0A 01 22 80 23  .sha1...+.`..".#
0310: 45 11 80 F0 FF FF 7F F0  FF FF 7F 74 30 30 63 09  E..........t00c.
0320: 80 55 11 80 F0 FF FF 7F  F0 FF FF 7F 74 30 30 63  .U..........t00c
0330: 4A C4 60 0A 01 F0 FF FF  7F 6F 76 C4 60 0A 01 45  J.`......ov.`..E
0340: 11 80 F0 FF FF 7F F0 FF  FF 7F 74 30 30 64 09 80  ..........t00d..
0350: 2B C4 60 0A 01 23 80 23  2B C4 60 0A 01 24 80 23  +.`..#.#+.`..$.#
0360: 66 09 80 C4 60 0A 01 C4  60 0A 01 70 61 73 30 53  f...`...`..pas0S
0370: C4 60 0A 01 C4 60 0A 01  70 61 73 30 55 11 80 F0  .`...`..pas0U...
0380: FF FF 7F F0 FF FF 7F 74  30 30 64 45 08 80 F0 FF  .......t00dE....
0390: FF 7F F0 FF FF 7F 66 64  6F 32 09 80 55 08 80 F0  ......fdo2..U...
03A0: FF FF 7F F0 FF FF 7F 66  64 6F 32 45 25 80 F0 FF  .......fdo2E%...
03B0: FF 7F F0 FF FF 7F 71 73  74 63 09 80 5C 00 09 80  ......qstc..\...
03C0: 5C 01 09 80 46 00 45 08  80 F0 FF FF 7F F0 FF FF  \...F.E.........
03D0: 7F 66 64 69 32 09 80 21  00                       .fdi2..!.       
```

#### Opcodes

```
  0: 0x00E0 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00E2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00E3 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x00E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x00F6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0105 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 159*
  6: 0x0109 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 159*
  7: 0x010D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0110 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-282.721*, z=209.918*, y=-45.137*, direction=193.4°*
  9: 0x0119 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 10: 0x011C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "t007" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 11: 0x012D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "t007" with entities [LocalPlayer, LocalPlayer], work=208*
 12: 0x013C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x014D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 14: 0x015C [0x1C] WAIT(10* ticks)
 15: 0x015F [0x1F] MOVE_ENTITY: EventEntity moves to X=-284.583*, Z=210.474*, Y=-45.194*
 16: 0x0167 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 17: 0x0169 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 18: 0x016A [0x1C] WAIT(15* ticks)
 19: 0x016D [0x2B] Mertaire (ID: 17457348/0x010A60C4) [7370*]:
    → "Wait."
 20: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0175 [0x4E] SET_ENTITY_HIDE_FLAG: Show Mertaire (ID: 17457348/0x010A60C4)
 22: 0x017B [0x4A] LocalPlayer looks at Mertaire (ID: 17457348/0x010A60C4)
 23: 0x0184 [0x27] REQ_SET(priority=0x03, entity_id=Mertaire (ID: 17457348/0x010A60C4), tag_num=0x02)
 24: 0x018B [0x1C] WAIT(150* ticks)
 25: 0x018E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "t00b" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 26: 0x019F [0x2A] GET_REQ_LEVEL(level=3, entity_id=Mertaire (ID: 17457348/0x010A60C4))
 27: 0x01A5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "t00b" with entities [LocalPlayer, LocalPlayer], work=208*
 28: 0x01B4 [0x2B] Mertaire (ID: 17457348/0x010A60C4) [7371*]:
    → "I changed my mind. Please, let me throw it in myself."
 29: 0x01BB [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x01BC [0x1C] WAIT(30* ticks)
 31: 0x01BF [0x27] REQ_SET(priority=0x03, entity_id=Mertaire (ID: 17457348/0x010A60C4), tag_num=0x03)
 32: 0x01C6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-284.207*, Z=212.517*, Y=-45.312*
 33: 0x01CE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 34: 0x01D0 [0x4A] LocalPlayer looks at Mertaire (ID: 17457348/0x010A60C4)
 35: 0x01D9 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Mertaire (ID: 17457348/0x010A60C4))
 36: 0x01DF [0x4A] LocalPlayer looks at Mertaire (ID: 17457348/0x010A60C4)
 37: 0x01E8 [0x4A] Mertaire (ID: 17457348/0x010A60C4) looks at Waters of Oblivion (ID: 17457347/0x010A60C3)
 38: 0x01F1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 39: 0x01F2 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Mertaire (ID: 17457348/0x010A60C4) Render.Flags0 and Render.Flags3 conditions are met
 40: 0x01F7 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "shit" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)]
 41: 0x0204 [0x1C] WAIT(30* ticks)
 42: 0x0207 [0x4A] LocalPlayer looks at Waters of Oblivion (ID: 17457347/0x010A60C3)
 43: 0x0210 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "t011" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)], work=[208*, 0*]
 44: 0x0221 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "t011" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)], work=208*
 45: 0x0230 [0x1C] WAIT(10* ticks)
 46: 0x0233 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x0244 [0x1C] WAIT(5* ticks)
 48: 0x0247 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "t008" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 49: 0x0258 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "t008" with entities [LocalPlayer, LocalPlayer], work=208*
 50: 0x0267 [0x28] REQ_SET_WITH_CONDITIONS(priority=0x03, target_entity=Waters of Oblivion (ID: 17457347/0x010A60C3), tag_num=0x02)
 51: 0x026E [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17457345/0x010A60C1), tag_num=0x06)
 52: 0x0275 [0x1C] WAIT(10* ticks)
 53: 0x0278 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)], work=9*
 54: 0x0287 [0x06] ExtData[1]->WorkLocal[2] = 0
 55: 0x028A [0x02] IF !(ExtData[1]->WorkLocal[2] > 200*) GOTO 0x02AE
 56: 0x0292 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Waters of Oblivion (ID: 17457347/0x010A60C3), Waters of Oblivion (ID: 17457347/0x010A60C3)], work=[3*, 0*]
 57: 0x02A3 [0x1C] WAIT(40* ticks)
 58: 0x02A6 [0x07] ExtData[1]->WorkLocal[2] += 40*
 59: 0x02AB [0x01] GOTO 0x028A
 60: 0x02AE [0x2A] GET_REQ_LEVEL(level=3, entity_id=Waters of Oblivion (ID: 17457347/0x010A60C3))
 61: 0x02B4 [0x1C] WAIT(60* ticks)
 62: 0x02B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "t010" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 63: 0x02C8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "t010" with entities [LocalPlayer, LocalPlayer], work=208*
 64: 0x02D7 [0x03] Work_Zone[2] = 228*
 65: 0x02DC [0x48] [System] [7368*]:
    → "Mertaire throws his bracelet into the Waters of Oblivion."
 66: 0x02DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 67: 0x02E0 [0x4A] LocalPlayer looks at Mertaire (ID: 17457348/0x010A60C4)
 68: 0x02E9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)], work=9*
 69: 0x02F8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)]
 70: 0x0305 [0x1C] WAIT(60* ticks)
 71: 0x0308 [0x2B] Mertaire (ID: 17457348/0x010A60C4) [7372*]:
    → "Ten... No, a hundred years from now, if the bracelet is ever found, what will cross their minds? Could it be true that the memories of past owners reside within such things?"
 72: 0x030F [0x23] WAIT_FOR_DIALOG_INTERACTION
 73: 0x0310 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "t00c" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 74: 0x0321 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "t00c" with entities [LocalPlayer, LocalPlayer], work=208*
 75: 0x0330 [0x4A] Mertaire (ID: 17457348/0x010A60C4) looks at LocalPlayer
 76: 0x0339 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 77: 0x033A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Mertaire (ID: 17457348/0x010A60C4) Render.Flags0 and Render.Flags3 conditions are met
 78: 0x033F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "t00d" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 79: 0x0350 [0x2B] Mertaire (ID: 17457348/0x010A60C4) [7373*]:
    → "And when I think how we may yet find such a thing, recovering memories buried under the flow of time, it seems sad."
 80: 0x0357 [0x23] WAIT_FOR_DIALOG_INTERACTION
 81: 0x0358 [0x2B] Mertaire (ID: 17457348/0x010A60C4) [7374*]:
    → "Thank you for helping me. Everything seems much clearer now. Here, take this."
 82: 0x035F [0x23] WAIT_FOR_DIALOG_INTERACTION
 83: 0x0360 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)], work=0*
 84: 0x036F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [Mertaire (ID: 17457348/0x010A60C4), Mertaire (ID: 17457348/0x010A60C4)]
 85: 0x037C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "t00d" with entities [LocalPlayer, LocalPlayer], work=208*
 86: 0x038B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 87: 0x039C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 88: 0x03AB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 89: 0x03BC [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 90: 0x03C0 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 91: 0x03C4 [0x46] CAMERA_CONTROL: Restore default settings
 92: 0x03C6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 93: 0x03D7 [0x21] END_EVENT
 94: 0x03D8 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03D9  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03D0:                             03 02 10 0B 7F 00              ...... 
```

#### Opcodes

```
  0: 0x03D9 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x03DE [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03DF  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03D0:                                               03                 .
03E0: 03 10 0B 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x03DF [0x03] Work_Zone[3] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x03E4 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03E5  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                03 09 10  0B 7F 00                      ......     
```

#### Opcodes

```
  0: 0x03E5 [0x03] Work_Zone[9] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x03EA [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03EB  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                                   03 09 10 07 7F             .....
03F0: 00                                                .               
```

#### Opcodes

```
  0: 0x03EB [0x03] Work_Zone[9] = Entity->Race
  1: 0x03F0 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03F1   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03F0:    37 26 80 27 80 28 80  29 80 00                  7&.'.(.)..     
```

#### Opcodes

```
  0: 0x03F1 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-182.758*, z=-167.126*, y=5.249*, direction=258.9°*
  1: 0x03FA [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03FB   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03F0:                                   37 2A 80 2B 80             7*.+.
0400: 2C 80 2D 80 00                                    ,.-..           
```

#### Opcodes

```
  0: 0x03FB [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=55.121*, z=-144.826*, y=13.150*, direction=106.6°*
  1: 0x0404 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0405   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0400:                03 00 00  07 7F 1A 71 00 0B 01 00       ......q....
0410: 66 01 00 F8 FF FF 7F F8  FF FF 7F 70 61 73 30 00  f..........pas0.
```

#### Opcodes

```
  0: 0x0405 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x040A [0x1A] CALL_SUBROUTINE(address=0x0071)
  2: 0x040D [0x0B] ExtData[1]->WorkLocal[1]++
  3: 0x0410 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  4: 0x041F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0420   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0420: 03 00 00 07 7F 1A 4C 00  66 01 00 F8 FF FF 7F F8  ......L.f.......
0430: FF FF 7F 74 6C 6B 30 1C  1F 80 66 01 00 F8 FF FF  ...tlk0...f.....
0440: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x0420 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0425 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x0428 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0437 [0x1C] WAIT(60* ticks)
  4: 0x043A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  5: 0x0449 [0x00] END_REQSTACK()
```
