# 17531205 - Eshantarl

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 160 bytes                        |
| Total Events     | 8                                |
| References Count | 5                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     22 |              3 |
| [65535.2](#event-655352) | 0x0017       |     14 |              2 |
| [65535.3](#event-655353) | 0x0025       |     16 |              2 |
| [65535.4](#event-655354) | 0x0035       |     14 |              2 |
| [23](#event-23)          | 0x0043       |      7 |              2 |
| [65535.5](#event-655355) | 0x004A       |     10 |              2 |
| [25](#event-25)          | 0x0054       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01C3      |         451 |
|       1 | 0x0000      |           0 |
|       2 | 0x26AC      |        9900 |
|       3 | 0x0BB8      |        3000 |
|       4 | 0x0C00      |        3072 |

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
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    81 00 F8 FF FF 7F 5B  00 80 F8 FF FF 7F F8 FF   ......[........
0010: FF 7F 75 6B 75 30 00                              ..uku0.         
```

#### Opcodes

```
  0: 0x0001 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0007 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "uku0" with entities [EventEntity, EventEntity], work=451*
  2: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0020: 75 6B 75 30 00                                    uku0.           
```

#### Opcodes

```
  0: 0x0017 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "uku0" with entities [EventEntity, EventEntity]
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
0030: 75 6B 75 31 00                                    uku1.           
```

#### Opcodes

```
  0: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "uku1" with entities [EventEntity, EventEntity], work=451*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                53 F8 FF  FF 7F F8 FF FF 7F 75 6B       S........uk
0040: 75 31 00                                          u1.             
```

#### Opcodes

```
  0: 0x0035 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "uku1" with entities [EventEntity, EventEntity]
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0043 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                37 01 80 02 80 03            7.....
0050: 80 04 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=9.900*, y=3.000*, direction=270.0°*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0054 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005A [0x00] END_REQSTACK()
```
