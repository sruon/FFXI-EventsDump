# 17776838 - Mokop-Sankop

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 668 bytes             |
| Total Events     | 10                    |
| References Count | 31                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10214](#event-10214)    | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |    384 |             51 |
| [65535.2](#event-655352) | 0x0188       |     22 |              6 |
| [65535.3](#event-655353) | 0x019E       |     14 |              4 |
| [10151](#event-10151)    | 0x01AC       |      7 |              2 |
| [10209](#event-10209)    | 0x01B3       |      7 |              2 |
| [10211](#event-10211)    | 0x01BA       |      7 |              2 |
| [65535.4](#event-655354) | 0x01C1       |     22 |              6 |
| [65535.5](#event-655355) | 0x01D7       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0029      |          41 |
|       1 | 0x0028      |          40 |
|       2 | 0x0096      |         150 |
|       3 | 0xFFFFFC18  |  4294966296 |
|       4 | 0x001E      |          30 |
|       5 | 0x000A      |          10 |
|       6 | 0x0050      |          80 |
|       7 | 0x0001      |           1 |
|       8 | 0x4650      |       18000 |
|       9 | 0x0000      |           0 |
|      10 | 0x02BC      |         700 |
|      11 | 0x000F      |          15 |
|      12 | 0xFFFC1117  |  4294709527 |
|      13 | 0xFFFECEA8  |  4294889128 |
|      14 | 0xFFFFC93B  |  4294953275 |
|      15 | 0x0144      |         324 |
|      16 | 0x00BF      |         191 |
|      17 | 0x003C      |          60 |
|      18 | 0x004D      |          77 |
|      19 | 0x0041      |          65 |
|      20 | 0x000D      |          13 |
|      21 | 0xFFFA872B  |  4294608683 |
|      22 | 0xFFFD5AFA  |  4294793978 |
|      23 | 0xFFFFD8EE  |  4294957294 |
|      24 | 0xFFFA7D05  |  4294606085 |
|      25 | 0xFFFD3D47  |  4294786375 |
|      26 | 0xFFFFD6FB  |  4294956795 |
|      27 | 0xFFFF2BE7  |  4294912999 |
|      28 | 0x192CA     |      103114 |
|      29 | 0xFFFE85FA  |  4294870522 |
|      30 | 0x297A4     |      169892 |

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

### Event 10214

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0008    |
| Data Size    | 384 bytes |
| Instructions | 51        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          66 00 80 C6 40 0F 01 C6          f...@...
0010: 40 0F 01 73 77 61 31 53  C6 40 0F 01 C6 40 0F 01  @..swa1S.@...@..
0020: 73 77 61 31 33 01 03 00  00 00 7F 03 01 00 02 7F  swa13...........
0030: 03 02 00 01 7F 03 03 00  03 7F 03 04 00 01 7F 66  ...............f
0040: 01 80 F8 FF FF 7F F8 FF  FF 7F 6A 6D 70 30 53 F8  ..........jmp0S.
0050: FF FF 7F F8 FF FF 7F 6A  6D 70 30 66 01 80 F8 FF  .......jmp0f....
0060: FF 7F F8 FF FF 7F 6A 6D  70 33 06 05 00 03 06 00  ......jmp3......
0070: 02 80 02 05 00 03 80 04  AA 00 03 02 00 04 00 07  ................
0080: 02 00 05 00 37 00 00 01  00 02 00 03 00 02 06 00  ....7...........
0090: 04 80 04 9A 00 08 06 00  05 80 07 00 00 06 80 08  ................
00A0: 05 00 06 00 1C 07 80 01  72 00 06 07 00 02 05 00  ........r.......
00B0: 08 80 05 F8 00 02 05 00  09 80 05 C8 00 02 07 00  ................
00C0: 09 80 00 C8 00 05 07 00  03 02 00 04 00 07 02 00  ................
00D0: 05 00 37 00 00 01 00 02  00 03 00 02 06 00 0A 80  ..7.............
00E0: 05 E8 00 07 06 00 0B 80  07 00 00 06 80 07 05 00  ................
00F0: 06 00 1C 07 80 01 AD 00  37 0C 80 0D 80 0E 80 0F  ........7.......
0100: 80 80 F8 FF FF 7F 45 10  80 F8 FF FF 7F F8 FF FF  ......E.........
0110: 7F 6B 61 6E 74 09 80 66  01 80 F8 FF FF 7F F8 FF  .kant..f........
0120: FF 7F 77 61 69 30 5B 09  80 25 40 0F 01 25 40 0F  ..wai0[..%@..%@.
0130: 01 74 6C 6B 30 5B 11 80  B7 40 0F 01 B7 40 0F 01  .tlk0[...@...@..
0140: 74 6C 6B 30 5B 12 80 0D  40 0F 01 0D 40 0F 01 6B  tlk0[...@...@..k
0150: 61 6E 30 5B 13 80 C3 40  0F 01 C3 40 0F 01 63 6C  an0[...@...@..cl
0160: 61 30 6E 99 40 0F 01 14  80 99 99 40 0F 01 6E 9A  a0n.@......@..n.
0170: 40 0F 01 14 80 99 9A 40  0F 01 53 F8 FF FF 7F F8  @......@..S.....
0180: FF FF 7F 77 61 69 30 00                           ...wai0.        
```

#### Opcodes

```
  0: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "swa1" with entities [Mokop-Sankop (ID: 17776838/0x010F40C6), Mokop-Sankop (ID: 17776838/0x010F40C6)], work=41*
  1: 0x0017 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "swa1" with entities [Mokop-Sankop (ID: 17776838/0x010F40C6), Mokop-Sankop (ID: 17776838/0x010F40C6)]
  2: 0x0024 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  3: 0x0026 [0x03] ExtData[1]->WorkLocal[0] = ExtData[1]->EventPos[0] * 1000.0
  4: 0x002B [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->EventPos[2] * 1000.0
  5: 0x0030 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->EventPos[1] * 1000.0
  6: 0x0035 [0x03] ExtData[1]->WorkLocal[3] = enDirCli(ExtData[1]->EventDir[1]) * 4096.0 * 0.15915963
  7: 0x003A [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->EventPos[1] * 1000.0
  8: 0x003F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=40*
  9: 0x004E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jmp0" with entities [EventEntity, EventEntity]
 10: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "jmp3" with entities [EventEntity, EventEntity], work=40*
 11: 0x006A [0x06] ExtData[1]->WorkLocal[5] = 0
 12: 0x006D [0x03] ExtData[1]->WorkLocal[6] = 150*
 13: 0x0072 [0x02] IF !(ExtData[1]->WorkLocal[5] < 4294966296*) GOTO 0x00AA
 14: 0x007A [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[4]
 15: 0x007F [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[5]
 16: 0x0084 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
 17: 0x008D [0x02] IF !(ExtData[1]->WorkLocal[6] < 30*) GOTO 0x009A
 18: 0x0095 [0x08] ExtData[1]->WorkLocal[6] -= 10*
 19: 0x009A [0x07] ExtData[1]->WorkLocal[0] += 80*
 20: 0x009F [0x08] ExtData[1]->WorkLocal[5] -= ExtData[1]->WorkLocal[6]
 21: 0x00A4 [0x1C] WAIT(1* ticks)
 22: 0x00A7 [0x01] GOTO 0x0072
 23: 0x00AA [0x06] ExtData[1]->WorkLocal[7] = 0

SUBROUTINE_00AD:
 24: 0x00AD [0x02] IF !(ExtData[1]->WorkLocal[5] > 18000*) GOTO 0x00F8
 25: 0x00B5 [0x02] IF !(ExtData[1]->WorkLocal[5] > 0*) GOTO 0x00C8
 26: 0x00BD [0x02] IF !(ExtData[1]->WorkLocal[7] == 0*) GOTO 0x00C8
 27: 0x00C5 [0x05] ExtData[1]->WorkLocal[7] = 1
 28: 0x00C8 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[4]
 29: 0x00CD [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[5]
 30: 0x00D2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
 31: 0x00DB [0x02] IF !(ExtData[1]->WorkLocal[6] > 700*) GOTO 0x00E8
 32: 0x00E3 [0x07] ExtData[1]->WorkLocal[6] += 15*
 33: 0x00E8 [0x07] ExtData[1]->WorkLocal[0] += 80*
 34: 0x00ED [0x07] ExtData[1]->WorkLocal[5] += ExtData[1]->WorkLocal[6]
 35: 0x00F2 [0x1C] WAIT(1* ticks)
 36: 0x00F5 [0x01] GOTO 0x00AD
 37: 0x00F8 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-257.769*, z=-78.168*, y=-14.021*, direction=28.5°*
 38: 0x0101 [0x80] LOAD_WAIT(entity=EventEntity)
 39: 0x0106 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kant" with entities [EventEntity, EventEntity], work=[191*, 0*]
 40: 0x0117 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wai0" with entities [EventEntity, EventEntity], work=40*
 41: 0x0126 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Glyke (ID: 17776677/0x010F4025), Glyke (ID: 17776677/0x010F4025)], work=0*
 42: 0x0135 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Unnamed NPC (ID: 17776823/0x010F40B7), Unnamed NPC (ID: 17776823/0x010F40B7)], work=60*
 43: 0x0144 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kan0" with entities [Osker (ID: 17776653/0x010F400D), Osker (ID: 17776653/0x010F400D)], work=77*
 44: 0x0153 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "cla0" with entities [Wyatt (ID: 17776835/0x010F40C3), Wyatt (ID: 17776835/0x010F40C3)], work=65*
 45: 0x0162 [0x6E] Pembroke (ID: 17776793/0x010F4099) uses emote 13*
 46: 0x0169 [0x99] Wait for Pembroke (ID: 17776793/0x010F4099) animation to complete
 47: 0x016E [0x6E] Pelagia (ID: 17776794/0x010F409A) uses emote 13*
 48: 0x0175 [0x99] Wait for Pelagia (ID: 17776794/0x010F409A) animation to complete
 49: 0x017A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wai0" with entities [EventEntity, EventEntity]
 50: 0x0187 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0188   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                          32 14 80 1F 00 15 80 16          2.......
0190: 80 17 80 1F 01 1E 33 40  0F 01 1C 04 80 00        ......3@......  
```

#### Opcodes

```
  0: 0x0188 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x018B [0x1F] MOVE_ENTITY: EventEntity moves to X=-358.613*, Z=-173.318*, Y=-10.002*
  2: 0x0193 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0195 [0x1E] EventEntity looks at Balkehr (ID: 17776691/0x010F4033) and starts talking
  4: 0x019A [0x1C] WAIT(30* ticks)
  5: 0x019D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                            32 14                2.
01A0: 80 1F 00 18 80 19 80 1A  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x019E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-361.211*, Z=-180.921*, Y=-10.501*
  2: 0x01A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01AB [0x00] END_REQSTACK()
```

### Event 10151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01AC  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                      92 01 F8 FF              ....
01B0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x01AC [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x01B2 [0x00] END_REQSTACK()
```

### Event 10209

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B3  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x01B3 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x01B9 [0x00] END_REQSTACK()
```

### Event 10211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01BA  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                92 01 F8 FF FF 7F            ......
01C0: 00                                                .               
```

#### Opcodes

```
  0: 0x01BA [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x01C0 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C1   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:    32 14 80 1F 00 1B 80  1C 80 09 80 1F 01 1E BD   2..............
01D0: 40 0F 01 1C 04 80 00                              @......         
```

#### Opcodes

```
  0: 0x01C1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01C4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-54.297*, Z=103.114*, Y=0.000*
  2: 0x01CC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01CE [0x1E] EventEntity looks at Laila (ID: 17776829/0x010F40BD) and starts talking
  4: 0x01D3 [0x1C] WAIT(30* ticks)
  5: 0x01D6 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D7   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                      32  14 80 1F 00 1D 80 1E 80         2........
01E0: 09 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x01D7 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01DA [0x1F] MOVE_ENTITY: EventEntity moves to X=-96.774*, Z=169.892*, Y=0.000*
  2: 0x01E2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01E4 [0x00] END_REQSTACK()
```
