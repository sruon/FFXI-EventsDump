# 17510703 - QeIov Gate

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Stellar Fulcrum (ID: 179) |
| Block Size       | 220 bytes                 |
| Total Events     | 12                        |
| References Count | 6                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [6](#event-6)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     21 |              3 |
| [1](#event-1)            | 0x0017       |     26 |              8 |
| [65535.2](#event-655352) | 0x0031       |     34 |              4 |
| [65535.3](#event-655353) | 0x0053       |     18 |              4 |
| [65535.4](#event-655354) | 0x0065       |      5 |              3 |
| [5](#event-5)            | 0x006A       |      1 |              1 |
| [0](#event-0)            | 0x006B       |      1 |              1 |
| [65535.5](#event-655355) | 0x006C       |     21 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002D      |          45 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x00F0      |         240 |
|       4 | 0x01E0      |         480 |
|       5 | 0x0032      |          50 |

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

### Event 6

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
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1C 00 80 45 01 80  F0 FF FF 7F F0 FF FF 7F    ...E..........
0010: 66 64 6F 31 02 80 00                              fdo1...         
```

#### Opcodes

```
  0: 0x0002 [0x1C] WAIT(45* ticks)
  1: 0x0005 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0016 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      2D  F0 FF FF 7F F0 FF FF 7F         -........
0020: 64 72 30 31 1C 03 80 4C  1C 04 80 4D 1C 05 80 21  dr01...L...M...!
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "dr01" with entities [LocalPlayer, LocalPlayer]
  1: 0x0024 [0x1C] WAIT(240* ticks)
  2: 0x0027 [0x4C] EventEntity->StatusEvent = 8 // Open door
  3: 0x0028 [0x1C] WAIT(480* ticks)
  4: 0x002B [0x4D] EventEntity->StatusEvent = 9 // Close door
  5: 0x002C [0x1C] WAIT(50* ticks)
  6: 0x002F [0x21] END_EVENT
  7: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    45 01 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31   E..........fdo1
0040: 02 80 55 01 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
0050: 31 4D 00                                          1M.             
```

#### Opcodes

```
  0: 0x0031 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  1: 0x0042 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  2: 0x0051 [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          2D F0 FF FF 7F  F0 FF FF 7F 64 72 30 31     -........dr01
0060: 1C 03 80 4C 00                                    ...L.           
```

#### Opcodes

```
  0: 0x0053 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "dr01" with entities [LocalPlayer, LocalPlayer]
  1: 0x0060 [0x1C] WAIT(240* ticks)
  2: 0x0063 [0x4C] EventEntity->StatusEvent = 8 // Open door
  3: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0065  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                4D 1C 05  80 00                         M....      
```

#### Opcodes

```
  0: 0x0065 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0066 [0x1C] WAIT(50* ticks)
  2: 0x0069 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                00                           .     
```

#### Opcodes

```
  0: 0x006A [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   00                         .    
```

#### Opcodes

```
  0: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      3B 25 31 0B              ;%1.
0070: 01 00 00 01 00 02 00 37  00 00 01 00 02 00 02 80  .......7........
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x006C [0x3B] GET_ENTITY_POSITION(entity=Zeid (ID: 17510693/0x010B3125), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x0077 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=0.0°*
  2: 0x0080 [0x00] END_REQSTACK()
```
