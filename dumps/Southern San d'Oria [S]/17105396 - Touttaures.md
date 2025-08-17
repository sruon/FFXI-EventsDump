# 17105396 - Touttaures

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 80 bytes                         |
| Total Events     | 3                                |
| References Count | 2                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [603](#event-603)     | 0x0001       |     41 |              7 |
| [125](#event-125)     | 0x002A       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2F47      |       12103 |

## String References

- **12103**: Out of nowhere, an enormous worm rose up from the belly of the earth itself. With its huge mouth it effortlessly swallowed up a number of nearby soldiers, who were helpless to react.

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

### Event 603

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 66 00  80 F4 01 05 01 F4 01 05   .....f.........
0010: 01 74 6C 6B 30 1D 01 80  23 66 00 80 F4 01 05 01  .tlk0...#f......
0020: F4 01 05 01 74 6C 6B 31  21 00                    ....tlk1!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Touttaures (ID: 17105396/0x010501F4), Touttaures (ID: 17105396/0x010501F4)], work=20*
  2: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=12103*)
    → "Out of nowhere, an enormous worm rose up from the belly of the earth itself. With its huge mouth it effortlessly swallowed up a number of nearby soldiers, who were helpless to react."
  3: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0019 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Touttaures (ID: 17105396/0x010501F4), Touttaures (ID: 17105396/0x010501F4)], work=20*
  5: 0x0028 [0x21] END_EVENT
  6: 0x0029 [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```
