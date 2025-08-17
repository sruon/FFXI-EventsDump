# 17670774 - Justinius

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 48 bytes                   |
| Total Events     | 2                          |
| References Count | 2                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [343](#event-343)     | 0x0001       |     14 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2065      |        8293 |

## String References

- **8293**: I swore a vow. I will fight on until the last. For myself, and those I have lost...

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

### Event 343

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 21 00      ...........#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(20* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8293*)
    → "I swore a vow. I will fight on until the last. For myself, and those I have lost..."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x21] END_EVENT
  5: 0x000E [0x00] END_REQSTACK()
```
