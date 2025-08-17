# 17764525 - Valeriano

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 120 bytes                |
| Total Events     | 7                        |
| References Count | 6                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [46](#event-46)       | 0x0001       |      8 |              5 |
| [47](#event-47)       | 0x0009       |      8 |              5 |
| [56](#event-56)       | 0x0011       |      8 |              5 |
| [57](#event-57)       | 0x0019       |      8 |              5 |
| [66](#event-66)       | 0x0021       |      8 |              5 |
| [67](#event-67)       | 0x0029       |      8 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D8B      |        7563 |
|       1 | 0x1D8C      |        7564 |
|       2 | 0x1D95      |        7573 |
|       3 | 0x1D96      |        7574 |
|       4 | 0x1D9F      |        7583 |
|       5 | 0x1DA0      |        7584 |

## String References

- **7563**: Ladies and gentlepeople, horrible and honorable! The Troupe Valeriano is proud to perform in a place as powerful and pleasantly peopled as this!
- **7564**: Welcome to the Troupe Valeriano. Valeriano, at your service! Have a laugh, then spend some cash! Treats and sweets from exotic lands!
- **7573**: Ladies and gentlefolk, welcome to the Troupe Valeriano show! We are enthused to be able to perform in a city of such wealth and fame as Bastok!
- **7574**: Welcome to the Troupe Valeriano. Valeriano, at your service! Have a laugh, then spend some cash! Treats and sweets from exotic lands!
- **7583**: Halfling philosophers and heroine beauties, welcome to the Troupe Valeriano show! And how gorgeous and green this fair town is!
- **7584**: Welcome to the Troupe Valeriano. Valeriano, at your service! Have a laugh, then spend some cash! Treats and sweets from exotic lands!

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

### Event 46

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7563*)
    → "Ladies and gentlepeople, horrible and honorable! The Troupe Valeriano is proud to perform in a place as powerful and pleasantly peopled as this!"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0007 [0x21] END_EVENT
  4: 0x0008 [0x00] END_REQSTACK()
```

### Event 47

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             1D 01 80 23 20 00 21           ...# .!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7564*)
    → "Welcome to the Troupe Valeriano. Valeriano, at your service! Have a laugh, then spend some cash! Treats and sweets from exotic lands!"
  1: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x000F [0x21] END_EVENT
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 56

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1D 02 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7573*)
    → "Ladies and gentlefolk, welcome to the Troupe Valeriano show! We are enthused to be able to perform in a city of such wealth and fame as Bastok!"
  1: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0017 [0x21] END_EVENT
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1D 03 80 23 20 00 21           ...# .!
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7574*)
    → "Welcome to the Troupe Valeriano. Valeriano, at your service! Have a laugh, then spend some cash! Treats and sweets from exotic lands!"
  1: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x001D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x001F [0x21] END_EVENT
  4: 0x0020 [0x00] END_REQSTACK()
```

### Event 66

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1D 04 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=7583*)
    → "Halfling philosophers and heroine beauties, welcome to the Troupe Valeriano show! And how gorgeous and green this fair town is!"
  1: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0025 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0027 [0x21] END_EVENT
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 67

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1D 05 80 23 20 00 21           ...# .!
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7584*)
    → "Welcome to the Troupe Valeriano. Valeriano, at your service! Have a laugh, then spend some cash! Treats and sweets from exotic lands!"
  1: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x002F [0x21] END_EVENT
  4: 0x0030 [0x00] END_REQSTACK()
```
