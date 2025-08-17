# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Attohwa Chasm (ID: 7) |
| Block Size       | 76 bytes              |
| Total Events     | 5                     |
| References Count | 3                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [0](#event-0)         | 0x0002       |      1 |              1 |
| [1](#event-1)         | 0x0003       |      1 |              1 |
| [2](#event-2)         | 0x0004       |     22 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0078      |         120 |
|       1 | 0x02D0      |         720 |
|       2 | 0x0001      |           1 |

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

### Event 65534

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

### Event 0

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

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 22 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             20 01 42 1C  00 80 43 00 43 01 1C 01       .B...C.C...
0010: 80 03 01 10 02 80 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x0004 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0007 [0x1C] WAIT(120* ticks)
  3: 0x000A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  4: 0x000C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  5: 0x000E [0x1C] WAIT(720* ticks)
  6: 0x0011 [0x03] Work_Zone[1] = 1*
  7: 0x0016 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0018 [0x21] END_EVENT
  9: 0x0019 [0x00] END_REQSTACK()
```
