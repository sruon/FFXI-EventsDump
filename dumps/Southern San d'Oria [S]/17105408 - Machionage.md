# 17105408 - Machionage

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 100 bytes                        |
| Total Events     | 4                                |
| References Count | 3                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [619](#event-619)     | 0x0001       |     41 |              7 |
| [28](#event-28)       | 0x002A       |     12 |              6 |
| [120](#event-120)     | 0x0036       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2F59      |       12121 |
|       2 | 0x2ACC      |       10956 |

## String References

- **10956**: This charm is to be delivered to Lieutenant Phillieulais? I shall hold onto it until he returns from the battlefield.
- **12121**: I don't think any had imagined that the scattered beastmen would conspire to align with one another. And then to organize an offensive, of all things! There must be a great and evil charisma at work...

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

### Event 619

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 66 00  80 03 02 05 01 03 02 05   .....f.........
0010: 01 74 6C 6B 30 1D 01 80  23 66 00 80 03 02 05 01  .tlk0...#f......
0020: 03 02 05 01 74 6C 6B 31  21 00                    ....tlk1!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Elnonde (ID: 17105411/0x01050203), Elnonde (ID: 17105411/0x01050203)], work=20*
  2: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=12121*)
    → "I don't think any had imagined that the scattered beastmen would conspire to align with one another. And then to organize an offensive, of all things! There must be a great and evil charisma at work..."
  3: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0019 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Elnonde (ID: 17105411/0x01050203), Elnonde (ID: 17105411/0x01050203)], work=20*
  5: 0x0028 [0x21] END_EVENT
  6: 0x0029 [0x00] END_REQSTACK()
```

### Event 28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                42 1E F0 FF FF 7F            B.....
0030: 1D 02 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x002A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x002B [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=10956*)
    → "This charm is to be delivered to Lieutenant Phillieulais? I shall hold onto it until he returns from the battlefield."
  3: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0034 [0x21] END_EVENT
  5: 0x0035 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0036  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   00                                    .         
```

#### Opcodes

```
  0: 0x0036 [0x00] END_REQSTACK()
```
