# 17719336 - Millechairale

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 176 bytes                     |
| Total Events     | 9                             |
| References Count | 9                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [14](#event-14)          | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     14 |              4 |
| [65535.2](#event-655352) | 0x001F       |      6 |              2 |
| [65535.3](#event-655353) | 0x0025       |      6 |              2 |
| [65535.4](#event-655354) | 0x002B       |      6 |              2 |
| [65535.5](#event-655355) | 0x0031       |      6 |              2 |
| [65535.6](#event-655356) | 0x0037       |     16 |              2 |
| [65535.7](#event-655357) | 0x0047       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFCEECC  |  4294766284 |
|       1 | 0x10797     |       67479 |
|       2 | 0xFFFFF448  |  4294964296 |
|       3 | 0x07BC      |        1980 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFCD3CF  |  4294759375 |
|       6 | 0x10AC4     |       68292 |
|       7 | 0xFFFFF47B  |  4294964347 |
|       8 | 0x001B      |          27 |

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

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-201.012*, z=67.479*, y=-3.000*, direction=174.0°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-207.921*, Z=68.292*, Y=-2.949*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1E                 .
0020: 23 60 0E 01 00                                    #`...           
```

#### Opcodes

```
  0: 0x001F [0x1E] EventEntity looks at Phillone (ID: 17719331/0x010E6023) and starts talking
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1E 27 60  0E 01 00                      .'`...     
```

#### Opcodes

```
  0: 0x0025 [0x1E] EventEntity looks at Halver (ID: 17719335/0x010E6027) and starts talking
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   1E 25 60 0E 01             .%`..
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x002B [0x1E] EventEntity looks at Roido (ID: 17719333/0x010E6025) and starts talking
  1: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    1E F0 FF FF 7F 00                               ......         
```

#### Opcodes

```
  0: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      66  08 80 F8 FF FF 7F F8 FF         f........
0040: FF 7F 74 6C 62 30 00                              ..tlb0.         
```

#### Opcodes

```
  0: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      66  08 80 F8 FF FF 7F F8 FF         f........
0050: FF 7F 74 6C 62 31 00                              ..tlb1.         
```

#### Opcodes

```
  0: 0x0047 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
  1: 0x0056 [0x00] END_REQSTACK()
```
