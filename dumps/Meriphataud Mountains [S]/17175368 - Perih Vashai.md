# 17175368 - Perih Vashai

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 272 bytes                          |
| Total Events     | 18                                 |
| References Count | 11                                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [3](#event-3)              | 0x0001       |      1 |              1 |
| [4](#event-4)              | 0x0002       |      1 |              1 |
| [5](#event-5)              | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |      3 |              2 |
| [65535.2](#event-655352)   | 0x0007       |     19 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0024       |     10 |              2 |
| [65535.5](#event-655355)   | 0x002E       |     14 |              4 |
| [65535.6](#event-655356)   | 0x003C       |      1 |              1 |
| [65535.7](#event-655357)   | 0x003D       |     18 |              4 |
| [65535.8](#event-655358)   | 0x004F       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0059       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0062       |      9 |              3 |
| [65535.11](#event-6553511) | 0x006B       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0075       |     10 |              2 |
| [65535.13](#event-6553513) | 0x007F       |      5 |              2 |
| [65535.14](#event-6553514) | 0x0084       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x082C      |        2092 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0080      |         128 |
|       5 | 0x0028      |          40 |
|       6 | 0x6245B     |      402523 |
|       7 | 0x11A5D     |       72285 |
|       8 | 0xFFFFC306  |  4294951686 |
|       9 | 0x005D      |          93 |
|      10 | 0x0064      |         100 |

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

### Event 3

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

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             A4 01 00                                  ...         
```

#### Opcodes

```
  0: 0x0004 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      1C  00 80 5B 01 80 F8 FF FF         ...[.....
0010: 7F F8 FF FF 7F 74 6C 61  30 00                    .....tla0.      
```

#### Opcodes

```
  0: 0x0007 [0x1C] WAIT(20* ticks)
  1: 0x000A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=2092*
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                6C F8 FF FF 7F 02            l.....
0020: 80 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             6C F8 FF FF  7F 04 80 03 80 00            l.........  
```

#### Opcodes

```
  0: 0x0024 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            32 05                2.
0030: 80 1F 00 06 80 07 80 08  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x002E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=402.523*, Z=72.285*, Y=-15.610*
  2: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         22 00 2F               "./
0040: 00 F8 FF FF 7F 6C F8 FF  FF 7F 02 80 03 80 00     .....l......... 
```

#### Opcodes

```
  0: 0x003D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x003F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0045 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               6C                 l
0050: F8 FF FF 7F 04 80 03 80  00                       .........       
```

#### Opcodes

```
  0: 0x004F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0059  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             22 00 2F 00 F8 FF FF           "./....
0060: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0059 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x005B [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0062  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       22 01 2F 01 F8 FF  FF 7F 00                   "./......     
```

#### Opcodes

```
  0: 0x0062 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0064 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   6C F8 FF FF 7F             l....
0070: 02 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x006B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                6C F8 FF  FF 7F 04 80 03 80 00          l......... 
```

#### Opcodes

```
  0: 0x0075 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007F  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               B6                 .
0080: 0F 09 80 00                                       ....            
```

#### Opcodes

```
  0: 0x007F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=93*)
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             B6 0F 0A 80  00                           .....       
```

#### Opcodes

```
  0: 0x0084 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=100*)
  1: 0x0088 [0x00] END_REQSTACK()
```
