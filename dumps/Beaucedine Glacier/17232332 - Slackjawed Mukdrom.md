# 17232332 - Slackjawed Mukdrom

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Beaucedine Glacier (ID: 111) |
| Block Size       | 192 bytes                    |
| Total Events     | 9                            |
| References Count | 2                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [234](#event-234)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     16 |              2 |
| [65535.2](#event-655352) | 0x0018       |     14 |              2 |
| [65535.3](#event-655353) | 0x0026       |     16 |              2 |
| [65535.4](#event-655354) | 0x0036       |     14 |              2 |
| [65535.5](#event-655355) | 0x0044       |     16 |              2 |
| [65535.6](#event-655356) | 0x0054       |     14 |              2 |
| [65535.7](#event-655357) | 0x0062       |     32 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0018      |          24 |
|       1 | 0x000F      |          15 |

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

### Event 234

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          5B 00 80 F8 FF FF 7F F8          [.......
0010: FF FF 7F 64 61 69 30 00                           ...dai0.        
```

#### Opcodes

```
  0: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dai0" with entities [EventEntity, EventEntity], work=24*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          53 F8 FF FF 7F F8 FF FF          S.......
0020: 7F 64 61 69 30 00                                 .dai0.          
```

#### Opcodes

```
  0: 0x0018 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dai0" with entities [EventEntity, EventEntity]
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
0030: 7F 64 61 69 31 00                                 .dai1.          
```

#### Opcodes

```
  0: 0x0026 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dai1" with entities [EventEntity, EventEntity], work=24*
  1: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   53 F8  FF FF 7F F8 FF FF 7F 64        S........d
0040: 61 69 31 00                                       ai1.            
```

#### Opcodes

```
  0: 0x0036 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dai1" with entities [EventEntity, EventEntity]
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             5B 00 80 F8  FF FF 7F F8 FF FF 7F 64      [..........d
0050: 61 69 32 00                                       ai2.            
```

#### Opcodes

```
  0: 0x0044 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dai2" with entities [EventEntity, EventEntity], work=24*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             53 F8 FF FF  7F F8 FF FF 7F 64 61 69      S........dai
0060: 32 00                                             2.              
```

#### Opcodes

```
  0: 0x0054 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dai2" with entities [EventEntity, EventEntity]
  1: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       5B 00 80 F8 FF FF  7F F8 FF FF 7F 64 61 69    [..........dai
0070: 33 1C 01 80 53 F8 FF FF  7F F8 FF FF 7F 64 61 69  3...S........dai
0080: 33 00                                             3.              
```

#### Opcodes

```
  0: 0x0062 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dai3" with entities [EventEntity, EventEntity], work=24*
  1: 0x0071 [0x1C] WAIT(15* ticks)
  2: 0x0074 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dai3" with entities [EventEntity, EventEntity]
  3: 0x0081 [0x00] END_REQSTACK()
```
