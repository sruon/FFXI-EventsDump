# 16830678 - Awoken Ariri Samariri

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Mine Shaft #2716 (ID: 13) |
| Block Size       | 108 bytes                 |
| Total Events     | 6                         |
| References Count | 4                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      7 |              3 |
| [65535.2](#event-655352) | 0x0008       |      7 |              3 |
| [8](#event-8)            | 0x000F       |      7 |              2 |
| [32001](#event-32001)    | 0x0016       |      7 |              2 |
| [65535.3](#event-655353) | 0x001D       |     21 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0168      |         360 |
|       3 | 0x0017      |          23 |

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
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    AB 03 AC 01 00 80 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0003 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          AC 01 01 80 AB 04 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x000C [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x000E [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               92                 .
0010: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         1C 02 80               ...
0020: D0 03 80 F8 FF FF 7F F8  FF FF 7F 6F 30 30 33 01  ...........o003.
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x001D [0x1C] WAIT(360* ticks)
  1: 0x0020 [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "o003" with entities [EventEntity, EventEntity], work=[23*, 0*]
  2: 0x0031 [0x00] END_REQSTACK()
```
