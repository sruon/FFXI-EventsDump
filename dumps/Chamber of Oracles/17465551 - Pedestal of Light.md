# 17465551 - Pedestal of Light

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Chamber of Oracles (ID: 168) |
| Block Size       | 84 bytes                     |
| Total Events     | 4                            |
| References Count | 1                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [1](#event-1)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     43 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00A5      |         165 |

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

### Event 0

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

### Event 1

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 43 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          2D F0 FF FF 7F  F0 FF FF 7F 6D 73 64 31     -........msd1
0010: 1C 00 80 2D F0 FF FF 7F  F0 FF FF 7F 6D 73 64 6D  ...-........msdm
0020: 54 F0 FF FF 7F F0 FF FF  7F 6D 73 64 6D 00        T........msdm.  
```

#### Opcodes

```
  0: 0x0003 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "msd1" with entities [LocalPlayer, LocalPlayer]
  1: 0x0010 [0x1C] WAIT(165* ticks)
  2: 0x0013 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "msdm" with entities [LocalPlayer, LocalPlayer]
  3: 0x0020 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "msdm" with entities [LocalPlayer, LocalPlayer]
  4: 0x002D [0x00] END_REQSTACK()
```
