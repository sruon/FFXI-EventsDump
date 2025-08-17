# 17555989 - Tombstone

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | King Ranperre's Tomb (ID: 190) |
| Block Size       | 52 bytes                       |
| Total Events     | 3                              |
| References Count | 2                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2](#event-2)         | 0x0001       |      6 |              4 |
| [3](#event-3)         | 0x0007       |      6 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C67      |        7271 |
|       1 | 0x1C69      |        7273 |

## String References

- **7271**: A waterskin is lying here.
- **7273**: The lost waterskin is back where you first found it...

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

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 21 00                               H..#!.         
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7271*]:
    → "A waterskin is lying here."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      48  01 80 23 21 00                  H..#!.   
```

#### Opcodes

```
  0: 0x0007 [0x48] [System] [7273*]:
    → "The lost waterskin is back where you first found it..."
  1: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000B [0x21] END_EVENT
  3: 0x000C [0x00] END_REQSTACK()
```
