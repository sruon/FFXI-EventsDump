# 17510704 - QoTav Gate

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Stellar Fulcrum (ID: 179) |
| Block Size       | 92 bytes                  |
| Total Events     | 5                         |
| References Count | 3                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32003](#event-32003)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |      2 |              2 |
| [2](#event-2)            | 0x0029       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0078      |         120 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |

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

### Event 32003

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
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4C 1C 00 80 45 01  80 F0 FF FF 7F F0 FF FF    L...E.........
0010: 7F 66 64 6F 31 02 80 55  01 80 F0 FF FF 7F F0 FF  .fdo1..U........
0020: FF 7F 66 64 6F 31 00                              ..fdo1.         
```

#### Opcodes

```
  0: 0x0002 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0003 [0x1C] WAIT(120* ticks)
  2: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0017 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      4D  00                              M.       
```

#### Opcodes

```
  0: 0x0027 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             21 00                          !.     
```

#### Opcodes

```
  0: 0x0029 [0x21] END_EVENT
  1: 0x002A [0x00] END_REQSTACK()
```
