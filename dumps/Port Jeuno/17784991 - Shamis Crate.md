# 17784991 - Shamis Crate

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 60 bytes             |
| Total Events     | 2                    |
| References Count | 2                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [452](#event-452)     | 0x0001       |     25 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x005A      |          90 |

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

### Event 452

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2C F8 FF FF 7F F8 FF  FF 7F 6F 70 65 6E 1C 00   ,........open..
0010: 80 43 00 43 01 1C 01 80  21 00                    .C.C....!.      
```

#### Opcodes

```
  0: 0x0001 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "open" with entities [EventEntity, EventEntity]
  1: 0x000E [0x1C] WAIT(30* ticks)
  2: 0x0011 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0013 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0015 [0x1C] WAIT(90* ticks)
  5: 0x0018 [0x21] END_EVENT
  6: 0x0019 [0x00] END_REQSTACK()
```
