# 17850936 - Ukhu Sichahha

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Foret de Hennetiel (ID: 262) |
| Block Size       | 44 bytes                     |
| Total Events     | 2                            |
| References Count | 2                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [502](#event-502)     | 0x0001       |     10 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F01      |        7937 |
|       1 | 0x1F02      |        7938 |

## String References

- **7937**: Foret de Hennetiel is a mysterious place, even to those of us who have lived in Adoulin our whole lives. All manner of strange plants and hindrances...you've certainly got your work cut out for you.
- **7938**: But Adoulin has placed its faith in you, and so too shall I. Just like a fisherman must wait for hours before finding a catch, so too must you persevere.

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

### Event 502

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 21 00                  ...#...#!.     
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7937*)
    → "Foret de Hennetiel is a mysterious place, even to those of us who have lived in Adoulin our whole lives. All manner of strange plants and hindrances...you've certainly got your work cut out for you."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=7938*)
    → "But Adoulin has placed its faith in you, and so too shall I. Just like a fisherman must wait for hours before finding a catch, so too must you persevere."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x21] END_EVENT
  5: 0x000A [0x00] END_REQSTACK()
```
