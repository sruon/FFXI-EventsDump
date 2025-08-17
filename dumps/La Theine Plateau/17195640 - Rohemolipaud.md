# 17195640 - Rohemolipaud

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 76 bytes                    |
| Total Events     | 3                           |
| References Count | 1                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [119](#event-119)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     42 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002A      |          42 |

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

### Event 119

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
| Data Size    | 42 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       66 00 80 F8 FF FF  7F F8 FF FF 7F 77 6F 6E    f..........won
0010: 32 2C F8 FF FF 7F F8 FF  FF 7F 6C 63 30 33 53 F8  2,........lc03S.
0020: FF FF 7F F8 FF FF 7F 6C  63 30 33 00              .......lc03.    
```

#### Opcodes

```
  0: 0x0002 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "won2" with entities [EventEntity, EventEntity], work=42*
  1: 0x0011 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "lc03" with entities [EventEntity, EventEntity]
  2: 0x001E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "lc03" with entities [EventEntity, EventEntity]
  3: 0x002B [0x00] END_REQSTACK()
```
