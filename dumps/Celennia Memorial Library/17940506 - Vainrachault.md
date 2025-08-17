# 17940506 - Vainrachault

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Celennia Memorial Library (ID: 284) |
| Block Size       | 64 bytes                            |
| Total Events     | 4                                   |
| References Count | 3                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [24](#event-24)       | 0x0001       |     16 |              9 |
| [2](#event-2)         | 0x0011       |      1 |              1 |
| [5](#event-5)         | 0x0012       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E0C      |        7692 |
|       1 | 0x1E0D      |        7693 |
|       2 | 0x1E0E      |        7694 |

## String References

- **7692**: This particular tome describes a certain type of vegetation labeled by scholars as the "Ulbukan Greatwood."
- **7693**: Supposedly there existed a certain tree of stupendous height some-odd centuries ago. At least that is what leading researchers in the field propose.
- **7694**: They cite the myriad roots of abnormal size scattered across the continent as proof, but I would personally like to see some more evidence before forming my own conclusions...

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

### Event 24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 1D 02 80 23 20 00 21   ...#...#...# .!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7692*)
    → "This particular tome describes a certain type of vegetation labeled by scholars as the "Ulbukan Greatwood.""
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=7693*)
    → "Supposedly there existed a certain tree of stupendous height some-odd centuries ago. At least that is what leading researchers in the field propose."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7694*)
    → "They cite the myriad roots of abnormal size scattered across the continent as proof, but I would personally like to see some more evidence before forming my own conclusions..."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x000F [0x21] END_EVENT
  8: 0x0010 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```
