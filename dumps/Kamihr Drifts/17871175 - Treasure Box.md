# 17871175 - Treasure Box

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Kamihr Drifts (ID: 267) |
| Block Size       | 56 bytes                |
| Total Events     | 2                       |
| References Count | 1                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [5006](#event-5006)   | 0x0001       |     24 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |

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

### Event 5006

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 24 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 2C F8 FF FF  7F F8 FF FF 7F 6F 70 65    .B,........ope
0010: 6E 1C 00 80 2E 20 00 21  00                       n.... .!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "open" with entities [EventEntity, EventEntity]
  3: 0x0011 [0x1C] WAIT(200* ticks)
  4: 0x0014 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
  5: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0017 [0x21] END_EVENT
  7: 0x0018 [0x00] END_REQSTACK()
```
