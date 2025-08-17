# 17437008 - Stooge Moogle

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Castle Zvahl Baileys (ID: 161) |
| Block Size       | 264 bytes                      |
| Total Events     | 11                             |
| References Count | 11                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [88](#event-88)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     19 |              5 |
| [65535.2](#event-655352) | 0x0015       |     15 |              5 |
| [65535.3](#event-655353) | 0x0024       |     16 |              2 |
| [65535.4](#event-655354) | 0x0034       |     18 |              2 |
| [65535.5](#event-655355) | 0x0046       |     18 |              2 |
| [65535.6](#event-655356) | 0x0058       |     19 |              3 |
| [65535.7](#event-655357) | 0x006B       |     16 |              2 |
| [65535.8](#event-655358) | 0x007B       |     16 |              2 |
| [65535.9](#event-655359) | 0x008B       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x093C      |        2364 |
|       1 | 0x000F      |          15 |
|       2 | 0x5C44F     |      377935 |
|       3 | 0xFFFFB1E0  |  4294947296 |
|       4 | 0xFFFFD120  |  4294955296 |
|       5 | 0x0A4C      |        2636 |
|       6 | 0x0019      |          25 |
|       7 | 0x0000      |           0 |
|       8 | 0x0A52      |        2642 |
|       9 | 0x00A0      |         160 |
|      10 | 0x003C      |          60 |

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

### Event 88

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
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 B6 00 00 80  92 01 F8 FF FF 7F 94 01    ".............
0010: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2364*)
  2: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000E [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 01 80  1F 00 02 80 03 80 04 80       2..........
0020: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=377.935*, Z=-20.000*, Y=-12.000*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             5B 05 80 F8  FF FF 7F F8 FF FF 7F 69      [..........i
0030: 74 6D 30 00                                       tm0.            
```

#### Opcodes

```
  0: 0x0024 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "itm0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             BB 06 80 F8  FF FF 7F F8 FF FF 7F 73      ...........s
0040: 74 61 74 07 80 00                                 tat...          
```

#### Opcodes

```
  0: 0x0034 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "stat" with entities [EventEntity, EventEntity], work=[25*, 0*]
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   BB 06  80 F8 FF FF 7F F8 FF FF        ..........
0050: 7F 73 74 6F 70 07 80 00                           .stop...        
```

#### Opcodes

```
  0: 0x0046 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "stop" with entities [EventEntity, EventEntity], work=[25*, 0*]
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          5B 08 80 F8 FF FF 7F F8          [.......
0060: FF FF 7F 6F 6A 69 30 1C  09 80 00                 ...oji0....     
```

#### Opcodes

```
  0: 0x0058 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "oji0" with entities [EventEntity, EventEntity], work=2642*
  1: 0x0067 [0x1C] WAIT(160* ticks)
  2: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   5B 05 80 F8 FF             [....
0070: FF 7F F8 FF FF 7F 68 61  70 30 00                 ......hap0.     
```

#### Opcodes

```
  0: 0x006B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   5B 05 80 F8 FF             [....
0080: FF 7F F8 FF FF 7F 74 6C  6B 30 00                 ......tlk0.     
```

#### Opcodes

```
  0: 0x007B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   5B 05 80 F8 FF             [....
0090: FF 7F F8 FF FF 7F 73 74  64 30 1C 0A 80 00        ......std0....  
```

#### Opcodes

```
  0: 0x008B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x009A [0x1C] WAIT(60* ticks)
  2: 0x009D [0x00] END_REQSTACK()
```
