# 17629803 - Spelunking Sabotender

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Quicksand Caves (ID: 208) |
| Block Size       | 236 bytes                 |
| Total Events     | 12                        |
| References Count | 12                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      5 |              2 |
| [65535.2](#event-655352) | 0x0006       |      5 |              2 |
| [65535.3](#event-655353) | 0x000B       |      9 |              3 |
| [65535.4](#event-655354) | 0x0014       |      5 |              2 |
| [65535.5](#event-655355) | 0x0019       |      5 |              2 |
| [105](#event-105)        | 0x001E       |      7 |              2 |
| [106](#event-106)        | 0x0025       |      7 |              2 |
| [107](#event-107)        | 0x002C       |      1 |              1 |
| [65535.6](#event-655356) | 0x002D       |     14 |              4 |
| [65535.7](#event-655357) | 0x003B       |     49 |              7 |
| [65535.8](#event-655358) | 0x006C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0E0A      |        3594 |
|       1 | 0x0034      |          52 |
|       2 | 0x0050      |          80 |
|       3 | 0x0064      |         100 |
|       4 | 0x0174      |         372 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFEEE27  |  4294897191 |
|       7 | 0x4C064     |      311396 |
|       8 | 0xFFFF4CD0  |  4294921424 |
|       9 | 0x00C8      |         200 |
|      10 | 0x0018      |          24 |
|      11 | 0x0000      |           0 |

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

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 00 00 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3594*)
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   B6 00  01 80 00                       .....     
```

#### Opcodes

```
  0: 0x0006 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   B6 00 00 80 B6             .....
0010: 0F 02 80 00                                       ....            
```

#### Opcodes

```
  0: 0x000B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3594*)
  1: 0x000F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=80*)
  2: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             B6 0F 03 80  00                           .....       
```

#### Opcodes

```
  0: 0x0014 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=100*)
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             B6 00 04 80 00                 .....  
```

#### Opcodes

```
  0: 0x0019 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=372*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            92 01                ..
0020: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x001E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x0025 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 05 80               2..
0030: 1F 00 06 80 07 80 08 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=-70.105*, Z=311.396*, Y=-45.872*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 49 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1C 09 80 32 05             ...2.
0040: 80 1F 00 06 80 07 80 08  80 1F 01 D5 0A 80 6B 02  ..............k.
0050: 0D 01 6B 02 0D 01 69 6E  30 30 0B 80 D6 0A 80 6B  ..k...in00.....k
0060: 02 0D 01 6B 02 0D 01 69  6E 30 30 00              ...k...in00.    
```

#### Opcodes

```
  0: 0x003B [0x1C] WAIT(200* ticks)
  1: 0x003E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=-70.105*, Z=311.396*, Y=-45.872*
  3: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x004B [0xD5] LOAD_EVENT_SCHEDULER_ALT8: Load scheduler "in" with entities [Spelunking Sabotender (ID: 17629803/0x010D026B), Spelunking Sabotender (ID: 17629803/0x010D026B)], work=ExtData[1]->WorkLocal[11]
  5: 0x005C [0xD6] WAIT_LOAD_SCHEDULER_ALT6: Wait for scheduler "in00" with entities [Spelunking Sabotender (ID: 17629803/0x010D026B), Spelunking Sabotender (ID: 17629803/0x010D026B)], work=24*
  6: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      32 05 80 1F              2...
0070: 00 06 80 07 80 08 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x006C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=-70.105*, Z=311.396*, Y=-45.872*
  2: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0079 [0x00] END_REQSTACK()
```
