# 17723545 - DoorBastokan Consul

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 48 bytes                      |
| Total Events     | 3                             |
| References Count | 2                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [581](#event-581)        | 0x0001       |      2 |              2 |
| [65535.1](#event-655351) | 0x0003       |      9 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00F0      |         240 |
|       1 | 0x0050      |          80 |

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

### Event 581

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4D 00                                           M.             
```

#### Opcodes

```
  0: 0x0001 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          4C 1C 00 80 4D  1C 01 80 00                 L...M....    
```

#### Opcodes

```
  0: 0x0003 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0004 [0x1C] WAIT(240* ticks)
  2: 0x0007 [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x0008 [0x1C] WAIT(80* ticks)
  4: 0x000B [0x00] END_REQSTACK()
```
