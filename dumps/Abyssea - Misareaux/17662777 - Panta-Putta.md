# 17662777 - Panta-Putta

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - Misareaux (ID: 216) |
| Block Size       | 52 bytes                      |
| Total Events     | 2                             |
| References Count | 2                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [259](#event-259)     | 0x0001       |     16 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2171      |        8561 |
|       1 | 0x2172      |        8562 |

## String References

- **8561**: Whoa! Is this a new toy!?
- **8562**: It is a new toy! And it's all mine mine mine! Hahaha! All my friends are going to be jealous-wealous of me now!

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

### Event 259

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 42 1D  00 80 23 1D 01 80 23 21   .....B...#...#!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=8561*)
    → "Whoa! Is this a new toy!?"
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=8562*)
    → "It is a new toy! And it's all mine mine mine! Hahaha! All my friends are going to be jealous-wealous of me now!"
  5: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000F [0x21] END_EVENT
  7: 0x0010 [0x00] END_REQSTACK()
```
