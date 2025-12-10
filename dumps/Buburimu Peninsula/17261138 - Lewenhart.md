# 17261138 - Lewenhart

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Buburimu Peninsula (ID: 118) |
| Block Size       | 240 bytes                    |
| Total Events     | 9                            |
| References Count | 8                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      6 |              3 |
| [0](#event-0)            | 0x0006       |      1 |              1 |
| [65535.1](#event-655351) | 0x0007       |     17 |              5 |
| [65535.2](#event-655352) | 0x0018       |     13 |              4 |
| [65535.3](#event-655353) | 0x0025       |     35 |              4 |
| [65535.4](#event-655354) | 0x0048       |     35 |              4 |
| [65535.5](#event-655355) | 0x006B       |     19 |              3 |
| [65535.6](#event-655356) | 0x007E       |     29 |              3 |
| [65535.7](#event-655357) | 0x009B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFC4316  |  4294722326 |
|       2 | 0xFFFBB78F  |  4294686607 |
|       3 | 0x3E7F      |       15999 |
|       4 | 0xFFFC56EB  |  4294727403 |
|       5 | 0xFFFBC595  |  4294690197 |
|       6 | 0x0000      |           0 |
|       7 | 0x003C      |          60 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 6 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 32 00 80 00                                 ".2...          
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   00                                    .         
```

#### Opcodes

```
  0: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      1F  00 01 80 02 80 03 80 1F         .........
0010: 01 6F 1E 51 62 07 01 00                           .o.Qb...        
```

#### Opcodes

```
  0: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=-244.970*, Z=-280.689*, Y=15.999*
  1: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0012 [0x1E] EventEntity looks at Song Runes (ID: 17261137/0x01076251) and starts talking
  4: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          1F 00 04 80 05 80 03 80          ........
0020: 1F 01 22 01 00                                    .."..           
```

#### Opcodes

```
  0: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=-239.893*, Z=-277.099*, Y=15.999*
  1: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0022 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 35 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                81 00 F8  FF FF 7F 66 06 80 F8 FF       ......f....
0030: FF 7F F8 FF FF 7F 74 68  6B 31 53 F8 FF FF 7F F8  ......thk1S.....
0040: FF FF 7F 74 68 6B 31 00                           ...thk1.        
```

#### Opcodes

```
  0: 0x0025 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=0*
  2: 0x003A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  3: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 35 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          81 01 F8 FF FF 7F 66 06          ......f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 53 F8 FF  .........thk2S..
0060: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x0048 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  1: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=0*
  2: 0x005D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  3: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   66 06 80 F8 FF             f....
0070: FF 7F F8 FF FF 7F 74 6C  6B 30 1C 07 80 00        ......tlk0....  
```

#### Opcodes

```
  0: 0x006B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  1: 0x007A [0x1C] WAIT(60* ticks)
  2: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            66 06                f.
0080: 80 F8 FF FF 7F F8 FF FF  7F 74 65 6E 30 53 F8 FF  .........ten0S..
0090: FF 7F F8 FF FF 7F 74 65  6E 30 00                 ......ten0.     
```

#### Opcodes

```
  0: 0x007E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
  1: 0x008D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ten0" with entities [EventEntity, EventEntity]
  2: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   00                         .    
```

#### Opcodes

```
  0: 0x009B [0x00] END_REQSTACK()
```
