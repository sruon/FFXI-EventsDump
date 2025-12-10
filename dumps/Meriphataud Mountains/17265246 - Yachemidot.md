# 17265246 - Yachemidot

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Meriphataud Mountains (ID: 119) |
| Block Size       | 516 bytes                       |
| Total Events     | 8                               |
| References Count | 19                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [33](#event-33)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     14 |              4 |
| [65535.2](#event-655352) | 0x0019       |     37 |              9 |
| [65535.3](#event-655353) | 0x003E       |     39 |              5 |
| [65535.4](#event-655354) | 0x0065       |     68 |              8 |
| [65535.5](#event-655355) | 0x00A9       |     37 |              5 |
| [65535.6](#event-655356) | 0x00CE       |    185 |             37 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x9DA22     |      645666 |
|       1 | 0x158D      |        5517 |
|       2 | 0xFFFFC0AA  |  4294951082 |
|       3 | 0x098A      |        2442 |
|       4 | 0x000D      |          13 |
|       5 | 0x9CD0B     |      642315 |
|       6 | 0x1FE2      |        8162 |
|       7 | 0xFFFFC1D3  |  4294951379 |
|       8 | 0x001E      |          30 |
|       9 | 0x0018      |          24 |
|      10 | 0x0003      |           3 |
|      11 | 0x0005      |           5 |
|      12 | 0x0001      |           1 |
|      13 | 0x0002      |           2 |
|      14 | 0x000A      |          10 |
|      15 | 0x0009      |           9 |
|      16 | 0x0046      |          70 |
|      17 | 0x008C      |         140 |
|      18 | 0x00D2      |         210 |

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

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=645.666*, z=5.517*, y=-16.214*, direction=214.6°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=642.315*, Z=8.162*, Y=-15.917*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 04 80 3B 5F 72 07           2..;_r.
0020: 01 00 00 01 00 02 00 31  00 00 00 01 00 02 00 08  .......1........
0030: 80 31 01 1C 08 80 1E 5F  72 07 01 6F 70 00        .1....._r..op.  
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x3B] GET_ENTITY_POSITION(entity=Unnamed NPC (ID: 17265247/0x0107725F), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x0027 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2], Time=30*
  3: 0x0031 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  4: 0x0033 [0x1C] WAIT(30* ticks)
  5: 0x0036 [0x1E] EventEntity looks at Unnamed NPC (ID: 17265247/0x0107725F) and starts talking
  6: 0x003B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x003C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 39 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            66 09                f.
0040: 80 F8 FF FF 7F F8 FF FF  7F 31 72 64 79 1C 08 80  .........1rdy...
0050: 66 09 80 F8 FF FF 7F F8  FF FF 7F 31 73 6C 68 7B  f..........1slh{
0060: 5E 72 07 01 00                                    ^r...           
```

#### Opcodes

```
  0: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  1: 0x004D [0x1C] WAIT(30* ticks)
  2: 0x0050 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1slh" with entities [EventEntity, EventEntity], work=24*
  3: 0x005F [0x7B] Yachemidot (ID: 17265246/0x0107725E) stops talking
  4: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 68 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                53 F8 FF  FF 7F F8 FF FF 7F 31 73       S........1s
0070: 6C 68 66 09 80 F8 FF FF  7F F8 FF FF 7F 31 72 74  lhf..........1rt
0080: 6E 53 F8 FF FF 7F F8 FF  FF 7F 31 72 74 6E 3B 5F  nS........1rtn;_
0090: 72 07 01 00 00 01 00 02  00 31 00 00 00 01 00 02  r........1......
00A0: 00 08 80 31 01 1C 08 80  00                       ...1.....       
```

#### Opcodes

```
  0: 0x0065 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1slh" with entities [EventEntity, EventEntity]
  1: 0x0072 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  2: 0x0081 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  3: 0x008E [0x3B] GET_ENTITY_POSITION(entity=Unnamed NPC (ID: 17265247/0x0107725F), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  4: 0x0099 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2], Time=30*
  5: 0x00A3 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  6: 0x00A5 [0x1C] WAIT(30* ticks)
  7: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             03 03 00 0A 80 1A F3           .......
00B0: 00 66 04 00 F8 FF FF 7F  F8 FF FF 7F 73 69 72 30  .f..........sir0
00C0: 53 F8 FF FF 7F F8 FF FF  7F 73 69 72 30 00        S........sir0.  
```

#### Opcodes

```
  0: 0x00A9 [0x03] ExtData[1]->WorkLocal[3] = 3*
  1: 0x00AE [0x1A] CALL_SUBROUTINE(address=0x00F3)
  2: 0x00B1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[4]
  3: 0x00C0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir0" with entities [EventEntity, EventEntity]
  4: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00CE    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            03 03                ..
00D0: 00 0A 80 1A F3 00 66 04  00 F8 FF FF 7F F8 FF FF  ......f.........
00E0: 7F 73 68 61 31 53 F8 FF  FF 7F F8 FF FF 7F 73 68  .sha1S........sh
00F0: 61 31 00 03 04 00 03 00  02 04 00 0B 80 05 08 01  a1..............
0100: 08 04 00 0C 80 01 0D 01  08 04 00 0D 80 14 04 00  ................
0110: 0E 80 07 04 00 0F 80 1B  03 04 00 03 00 02 04 00  ................
0120: 0B 80 05 2D 01 08 04 00  0C 80 01 32 01 08 04 00  ...-.......2....
0130: 0D 80 14 04 00 0E 80 07  04 00 10 80 1B 03 04 00  ................
0140: 03 00 02 04 00 0B 80 05  52 01 08 04 00 0C 80 01  ........R.......
0150: 57 01 08 04 00 0D 80 14  04 00 0E 80 07 04 00 11  W...............
0160: 80 1B 03 04 00 03 00 02  04 00 0B 80 05 77 01 08  .............w..
0170: 04 00 0C 80 01 7C 01 08  04 00 0D 80 14 04 00 0E  .....|..........
0180: 80 07 04 00 12 80 1B                              .......         
```

#### Opcodes

```
  0: 0x00CE [0x03] ExtData[1]->WorkLocal[3] = 3*
  1: 0x00D3 [0x1A] CALL_SUBROUTINE(address=0x00F3)
  2: 0x00D6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[4]
  3: 0x00E5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x00F2 [0x00] END_REQSTACK()

SUBROUTINE_00F3:
  5: 0x00F3 [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[3]
  6: 0x00F8 [0x02] IF !(ExtData[1]->WorkLocal[4] > 5*) GOTO 0x0108
  7: 0x0100 [0x08] ExtData[1]->WorkLocal[4] -= 1*
  8: 0x0105 [0x01] GOTO 0x010D
  9: 0x0108 [0x08] ExtData[1]->WorkLocal[4] -= 2*

SUBROUTINE_010D:
 10: 0x010D [0x14] ExtData[1]->WorkLocal[4] *= 10*
 11: 0x0112 [0x07] ExtData[1]->WorkLocal[4] += 9*
 12: 0x0117 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0118 [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[3]
     0x011D [0x02] IF !(ExtData[1]->WorkLocal[4] > 5*) GOTO 0x012D
     0x0125 [0x08] ExtData[1]->WorkLocal[4] -= 1*
     0x012A [0x01] GOTO 0x0132
     0x012D [0x08] ExtData[1]->WorkLocal[4] -= 2*
     0x0132 [0x14] ExtData[1]->WorkLocal[4] *= 10*
     0x0137 [0x07] ExtData[1]->WorkLocal[4] += 70*
     0x013C [0x1B] RETURN
     0x013D [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[3]
     0x0142 [0x02] IF !(ExtData[1]->WorkLocal[4] > 5*) GOTO 0x0152
     0x014A [0x08] ExtData[1]->WorkLocal[4] -= 1*
     0x014F [0x01] GOTO 0x0157
     0x0152 [0x08] ExtData[1]->WorkLocal[4] -= 2*
     0x0157 [0x14] ExtData[1]->WorkLocal[4] *= 10*
     0x015C [0x07] ExtData[1]->WorkLocal[4] += 140*
     0x0161 [0x1B] RETURN
     0x0162 [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[3]
     0x0167 [0x02] IF !(ExtData[1]->WorkLocal[4] > 5*) GOTO 0x0177
     0x016F [0x08] ExtData[1]->WorkLocal[4] -= 1*
     0x0174 [0x01] GOTO 0x017C
     0x0177 [0x08] ExtData[1]->WorkLocal[4] -= 2*
     0x017C [0x14] ExtData[1]->WorkLocal[4] *= 10*
     0x0181 [0x07] ExtData[1]->WorkLocal[4] += 210*
     0x0186 [0x1B] RETURN
```
