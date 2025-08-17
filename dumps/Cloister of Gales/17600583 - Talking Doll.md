# 17600583 - Talking Doll

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Cloister of Gales (ID: 201) |
| Block Size       | 228 bytes                   |
| Total Events     | 10                          |
| References Count | 14                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [32000](#event-32000)    | 0x0027       |      1 |              1 |
| [32001](#event-32001)    | 0x0028       |      1 |              1 |
| [65535.3](#event-655353) | 0x0029       |      1 |              1 |
| [65535.4](#event-655354) | 0x002A       |     47 |              8 |
| [65535.5](#event-655355) | 0x0059       |     10 |              2 |
| [65535.6](#event-655356) | 0x0063       |      1 |              1 |
| [65535.7](#event-655357) | 0x0064       |     16 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FC      |         252 |
|       1 | 0x001E      |          30 |
|       2 | 0x0032      |          50 |
|       3 | 0x0001      |           1 |
|       4 | 0x4936      |       18742 |
|       5 | 0x6BDA      |       27610 |
|       6 | 0xFFFFB9B0  |  4294949296 |
|       7 | 0x0626      |        1574 |
|       8 | 0x0078      |         120 |
|       9 | 0xFFFFB7BC  |  4294948796 |
|      10 | 0x5727      |       22311 |
|      11 | 0x7CB7      |       31927 |
|      12 | 0xFFFFB8F7  |  4294949111 |
|      13 | 0x05AF      |        1455 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 62 72 75 30   [..........bru0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 62 72 75 30 5E 69   S........bru0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      00                                  .        
```

#### Opcodes

```
  0: 0x0027 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          00                               .       
```

#### Opcodes

```
  0: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 47 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                92 01 F8 FF FF 7F            ......
0030: 4E 00 47 90 0C 01 80 47  90 0C 01 6C F8 FF FF 7F  N.G....G...l....
0040: 02 80 03 80 33 01 37 04  80 05 80 06 80 07 80 6C  ....3.7........l
0050: F8 FF FF 7F 08 80 08 80  00                       .........       
```

#### Opcodes

```
  0: 0x002A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0030 [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17600583/0x010C9047)
  2: 0x0036 [0x80] LOAD_WAIT(entity=Talking Doll (ID: 17600583/0x010C9047))
  3: 0x003B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=50*, fade_time=1*)
  4: 0x0044 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  5: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.742*, z=27.610*, y=-18.000*, direction=138.3°*
  6: 0x004F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=120*, fade_time=120*)
  7: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             37 04 80 05 80 09 80           7......
0060: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0059 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.742*, z=27.610*, y=-18.500*, direction=138.3°*
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             92 01 F8 FF  FF 7F 37 0A 80 0B 80 0C      ......7.....
0070: 80 0D 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0064 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=22.311*, z=31.927*, y=-18.185*, direction=127.9°*
  2: 0x0073 [0x00] END_REQSTACK()
```
