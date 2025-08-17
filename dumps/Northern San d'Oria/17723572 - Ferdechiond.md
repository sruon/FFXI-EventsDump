# 17723572 - Ferdechiond

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 348 bytes                     |
| Total Events     | 10                            |
| References Count | 23                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [50](#event-50)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     29 |              3 |
| [65535.2](#event-655352) | 0x0028       |     29 |              3 |
| [16](#event-16)          | 0x0045       |     10 |              2 |
| [65535.3](#event-655353) | 0x004F       |     19 |              6 |
| [49](#event-49)          | 0x0062       |     16 |              3 |
| [65535.4](#event-655354) | 0x0072       |     52 |             12 |
| [65535.5](#event-655355) | 0x00A6       |     16 |              2 |
| [65535.6](#event-655356) | 0x00B6       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F271     |      127601 |
|       1 | 0x1DD28     |      122152 |
|       2 | 0xFFFFD505  |  4294956293 |
|       3 | 0x01E2      |         482 |
|       4 | 0x001D      |          29 |
|       5 | 0x167B5     |       92085 |
|       6 | 0x15F49     |       89929 |
|       7 | 0x06D5      |        1749 |
|       8 | 0x0232      |         562 |
|       9 | 0x000A      |          10 |
|      10 | 0x0028      |          40 |
|      11 | 0xF9D0      |       63952 |
|      12 | 0xE25D      |       57949 |
|      13 | 0x0000      |           0 |
|      14 | 0x1642C     |       91180 |
|      15 | 0x140EF     |       82159 |
|      16 | 0x0DFA      |        3578 |
|      17 | 0x174D8     |       95448 |
|      18 | 0x15163     |       86371 |
|      19 | 0x1809E     |       98462 |
|      20 | 0x14DF2     |       85490 |
|      21 | 0x2FC6      |       12230 |
|      22 | 0x0018      |          24 |

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

### Event 50

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=127.601*, z=122.152*, y=-11.003*, direction=42.4°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   66 04 80 F8 FF             f....
0010: FF 7F F8 FF FF 7F 74 6C  6B 30 53 F8 FF FF 7F F8  ......tlk0S.....
0020: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x000B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x001A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          66 04 80 F8 FF FF 7F F8          f.......
0030: FF FF 7F 74 6C 6B 31 53  F8 FF FF 7F F8 FF FF 7F  ...tlk1S........
0040: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0044 [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 05 80  06 80 07 80 08 80 00          7......... 
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=92.085*, z=89.929*, y=1.749*, direction=49.4°*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 19 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               1C                 .
0050: 09 80 32 0A 80 1F 00 0B  80 0C 80 0D 80 1F 01 22  ..2............"
0060: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x004F [0x1C] WAIT(10* ticks)
  1: 0x0052 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=63.952*, Z=57.949*, Y=0.000*
  3: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005F [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  5: 0x0061 [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       92 01 F8 FF FF 7F  37 0E 80 0F 80 07 80 10    ......7.......
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0062 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0068 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=91.180*, z=82.159*, y=1.749*, direction=314.5°*
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       1F 00 11 80 12 80  07 80 1F 01 1F 00 13 80    ..............
0080: 14 80 07 80 1F 01 6F 1E  AF 70 0E 01 6F 70 2B B4  ......o..p..op+.
0090: 70 0E 01 15 80 23 66 16  80 F8 FF FF 7F F8 FF FF  p....#f.........
00A0: 7F 31 72 64 79 00                                 .1rdy.          
```

#### Opcodes

```
  0: 0x0072 [0x1F] MOVE_ENTITY: EventEntity moves to X=95.448*, Z=86.371*, Y=1.749*
  1: 0x007A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=98.462*, Z=85.490*, Y=1.749*
  3: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0086 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0087 [0x1E] EventEntity looks at Rainemard (ID: 17723567/0x010E70AF) and starts talking
  6: 0x008C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x008D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x008E [0x2B] Ferdechiond (ID: 17723572/0x010E70B4) [12230*]:
    → "The enemy is here! Knights, to arms!"
  9: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0096 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
 11: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   66 16  80 F8 FF FF 7F F8 FF FF        f.........
00B0: 7F 31 72 74 6E 00                                 .1rtn.          
```

#### Opcodes

```
  0: 0x00A6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   66 16  80 F8 FF FF 7F F8 FF FF        f.........
00C0: 7F 31 72 64 79 00                                 .1rdy.          
```

#### Opcodes

```
  0: 0x00B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  1: 0x00C5 [0x00] END_REQSTACK()
```
