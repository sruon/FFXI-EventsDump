# 17146569 - Dimensional Portal

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Pashhow Marshlands [S] (ID: 90) |
| Block Size       | 64 bytes                        |
| Total Events     | 4                               |
| References Count | 0                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     28 |              4 |
| [65535.2](#event-655352) | 0x001D       |      1 |              1 |
| [65535.3](#event-655353) | 0x001E       |      1 |              1 |

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
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2C F8 FF FF 7F F0 FF  FF 7F 62 69 6E 64 53 F8   ,........bindS.
0010: FF FF 7F F0 FF FF 7F 62  69 6E 64 21 00           .......bind!.   
```

#### Opcodes

```
  0: 0x0001 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "bind" with entities [EventEntity, LocalPlayer]
  1: 0x000E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bind" with entities [EventEntity, LocalPlayer]
  2: 0x001B [0x21] END_EVENT
  3: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```
