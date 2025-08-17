# 17818252 - Maabu-Sonbu

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 84 bytes                     |
| Total Events     | 2                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [271](#event-271)     | 0x0001       |     37 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0028      |          40 |
|       2 | 0x2049      |        8265 |
|       3 | 0x204A      |        8266 |
|       4 | 0x204B      |        8267 |

## String References

- **8265**: It feels like another lifetime that I was training at the Orastery. It was all fun and games back then, to be honestaru.
- **8266**: I never imagined I'd one day need to ply my skills for the very survival-wival of mankind.
- **8267**: <Sigh> If only I had known that monsters would overrun the world, I would've applied myself bettaru in class.

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

### Event 271

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 37 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 1D 04 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=8265*)
    → "It feels like another lifetime that I was training at the Orastery. It was all fun and games back then, to be honestaru."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8266*)
    → "I never imagined I'd one day need to ply my skills for the very survival-wival of mankind."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=8267*)
    → "<Sigh> If only I had known that monsters would overrun the world, I would've applied myself bettaru in class."
  8: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0024 [0x21] END_EVENT
 10: 0x0025 [0x00] END_REQSTACK()
```
