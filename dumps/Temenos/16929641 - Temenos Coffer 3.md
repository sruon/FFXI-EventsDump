# 16929641 - Temenos Coffer 3

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 64 bytes         |
| Total Events     | 2                |
| References Count | 2                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1029](#event-1029)   | 0x0001       |     31 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x008C      |         140 |

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

### Event 1029

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 31 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 2C F8 FF FF  7F F8 FF FF 7F 6F 70 65    .B,........ope
0010: 6E 1C 00 80 43 00 43 01  1C 01 80 2E 20 00 21 00  n...C.C..... .!.
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "open" with entities [EventEntity, EventEntity]
  3: 0x0011 [0x1C] WAIT(60* ticks)
  4: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0018 [0x1C] WAIT(140* ticks)
  7: 0x001B [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
  8: 0x001C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x001E [0x21] END_EVENT
 10: 0x001F [0x00] END_REQSTACK()
```
