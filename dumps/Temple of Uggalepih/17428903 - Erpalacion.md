# 17428903 - Erpalacion

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 316 bytes                     |
| Total Events     | 10                            |
| References Count | 19                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [67](#event-67)          | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     32 |              7 |
| [65535.2](#event-655352) | 0x002E       |     15 |              5 |
| [65535.3](#event-655353) | 0x003D       |     17 |              5 |
| [65535.4](#event-655354) | 0x004E       |     10 |              2 |
| [65535.5](#event-655355) | 0x0058       |     29 |              3 |
| [65535.6](#event-655356) | 0x0075       |      9 |              3 |
| [65535.7](#event-655357) | 0x007E       |     29 |              3 |
| [65535.8](#event-655358) | 0x009B       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xD83F      |       55359 |
|       2 | 0xFFFF003B  |  4294901819 |
|       3 | 0x05C1      |        1473 |
|       4 | 0x01AE      |         430 |
|       5 | 0xDD03      |       56579 |
|       6 | 0xFFFEFBE8  |  4294900712 |
|       7 | 0x05C0      |        1472 |
|       8 | 0xEA5E      |       59998 |
|       9 | 0xFFFEDFBA  |  4294893498 |
|      10 | 0x05D7      |        1495 |
|      11 | 0x0400      |        1024 |
|      12 | 0xE68A      |       59018 |
|      13 | 0xFFFEE97D  |  4294895997 |
|      14 | 0x059F      |        1439 |
|      15 | 0x0000      |           0 |
|      16 | 0x0258      |         600 |
|      17 | 0x001D      |          29 |
|      18 | 0x003C      |          60 |

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

### Event 67

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    32 00 80 37 01 80 02  80 03 80 04 80 00         2..7.........  
```

#### Opcodes

```
  0: 0x0001 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=55.359*, z=-65.477*, y=1.473*, direction=37.8°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 32 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            92 00                ..
0010: F8 FF FF 7F 1F 00 05 80  06 80 07 80 1F 01 6F 4A  ..............oJ
0020: AA F1 09 01 F8 FF FF 7F  1E AA F1 09 01 00        ..............  
```

#### Opcodes

```
  0: 0x000E [0x92] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=56.579*, Z=-66.584*, Y=1.472*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x4A] Unnamed NPC (ID: 17428906/0x0109F1AA) looks at EventEntity
  5: 0x0028 [0x1E] EventEntity looks at Unnamed NPC (ID: 17428906/0x0109F1AA) and starts talking
  6: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            1F 00                ..
0030: 08 80 09 80 0A 80 1F 01  6F 39 0B 80 00           ........o9...   
```

#### Opcodes

```
  0: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=59.998*, Z=-73.798*, Y=1.495*
  1: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0038 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0039 [0x39] SET_ENTITY_DIRECTION(direction=5.6°*)
  4: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1F 00 0C               ...
0040: 80 0D 80 0E 80 1F 01 6F  1E AA F1 09 01 00        .......o......  
```

#### Opcodes

```
  0: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=59.018*, Z=-71.299*, Y=1.439*
  1: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0048 [0x1E] EventEntity looks at Unnamed NPC (ID: 17428906/0x0109F1AA) and starts talking
  4: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            6C A8                l.
0050: F1 09 01 0F 80 10 80 00                           ........        
```

#### Opcodes

```
  0: 0x004E [0x6C] FADE_ENTITY_COLOR(entity_id=Erpalacion (ID: 17428904/0x0109F1A8), end_alpha=0*, fade_time=600*)
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          66 11 80 F8 FF FF 7F F8          f.......
0060: FF FF 7F 74 6C 6B 30 53  F8 FF FF 7F F8 FF FF 7F  ...tlk0S........
0070: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x0058 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0067 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0075  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                5E 69 64  6C 30 1C 12 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x0075 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x007A [0x1C] WAIT(60* ticks)
  2: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            66 11                f.
0080: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 53 F8 FF  .........thk1S..
0090: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x007E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x008D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   66 11 80 F8 FF             f....
00A0: FF 7F F8 FF FF 7F 74 68  6B 32 53 F8 FF FF 7F F8  ......thk2S.....
00B0: FF FF 7F 74 68 6B 32 00                           ...thk2.        
```

#### Opcodes

```
  0: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x00AA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00B7 [0x00] END_REQSTACK()
```
